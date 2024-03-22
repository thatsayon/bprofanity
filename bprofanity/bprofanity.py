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
        self.censor_pattern = re.compile(r'\b(?:\w+)\b', re.IGNORECASE)

    def censor(self, input_text):
        words = input_text.split()
        censored_text = []
        for word in words:
            if self.trie.search(word.lower()):
                censored_text.append('*' * len(word))
            else:
                censored_text.append(word)
        return ' '.join(censored_text)

    def contains_profanity(self, input_text):
        words = self.censor_pattern.findall(
            input_text.lower())
        for word in words:
            if self.trie.search(word):
                return True
        return False

    def censor_count(self, input_text):
        count = 0
        words = self.censor_pattern.findall(
            input_text.lower())
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
