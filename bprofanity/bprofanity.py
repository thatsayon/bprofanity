import re
import os
from cryptography.fernet import Fernet


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word


class ProfanityChecker:
    def __init__(self):
        self.trie = Trie()
        self.compile_censor_pattern()
        self.root_dir = os.path.abspath(os.path.dirname(__file__))
        self.key = b'MVIXSs6cKkb5rZT7zl2hpD_qOBZ-ouwXKg6Zy_ZOrp0='
        self.load_words()

    def get_data(self, path):
        return os.path.join(self.root_dir, 'data', path)

    def load_words(self):
        filename = self.get_data('wordlist.enc')
        with open(filename, 'rb') as f:
            encrypted_data = f.read()
        fernet = Fernet(self.key)
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        words = decrypted_data.splitlines()
        for word in words:
            self.trie.insert(word.lower())

    def compile_censor_pattern(self):
        self.censor_pattern = re.compile(r'[\w\u0980-\u09FF]+', re.UNICODE)

    def generate_word_combinations(self, words):
        combinations = []
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n + 1):
                combinations.append(' '.join(words[i:j]))
        return combinations

    def censor(self, input_text):
        words = input_text.split()
        word_combinations = self.generate_word_combinations(words)
        censored_text = input_text
        for combination in word_combinations:
            if self.contains_profanity(combination):
                censored_text = censored_text.replace(
                    combination, '*' * len(combination))
        return censored_text

    def contains_profanity(self, input_text):
        words = self.censor_pattern.findall(input_text.lower())
        for word in words:
            if self.trie.search(word):
                return True
        return False

    def censor_count(self, input_text):
        count = 0
        words = self.censor_pattern.findall(input_text.lower())
        for word in words:
            if self.trie.search(word):
                count += 1
        return count

    def get_words(self):
        word_list = []

        def traverse(node, prefix):
            if node.is_end_of_word:
                word_list.append(prefix)
            for char, child_node in node.children.items():
                traverse(child_node, prefix + char)

        traverse(self.trie.root, "")
        return word_list

    def add_word(self, word):
        word = word.lower()
        if not self.trie.search(word):
            self.trie.insert(word)
            self.update_wordlist_file(word)

    def update_wordlist_file(self, word):
        filename = self.get_data('wordlist.enc')
        with open(filename, 'ab') as f:
            fernet = Fernet(self.key)
            encrypted_word = fernet.encrypt(word.encode() + b'\n')
            f.write(encrypted_word)
        f.close()
