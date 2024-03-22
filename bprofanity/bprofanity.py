import os
import re

words = set()
_ROOT = os.path.abspath(os.path.dirname(__file__))
censor_pattern = None


def get_data(path):
    return os.path.join(_ROOT, 'data', path)


def get_words():
    global words
    if not words:
        load_words()
    return words


def compile_censor_pattern():
    global censor_pattern
    words = get_words()
    censor_pattern = re.compile(
        r'\b(?:' + '|'.join(re.escape(word) for word in words) + r')\b', re.IGNORECASE)


def censor(input_text):
    global censor_pattern
    if not censor_pattern:
        compile_censor_pattern()
    return censor_pattern.sub('🤬', input_text)


def load_words(wordlist=None):
    global words
    if not wordlist:
        filename = get_data('wordlist.txt')
        with open(filename) as f:
            wordlist = {line.strip() for line in f if line.strip()}
    words = wordlist


def contains_profanity(input_text):
    global censor_pattern
    if not censor_pattern:
        compile_censor_pattern()
    return bool(censor_pattern.search(input_text))


def censor_count(input_text):
    global censor_pattern
    if not censor_pattern:
        compile_censor_pattern()
    return len(censor_pattern.findall(input_text))


def add_bad_word(word):
    words = get_words()

    if word not in words:
        wordlist = os.path.join(_ROOT, 'data', 'wordlist.txt')
        with open(wordlist, 'a') as f:
            f.write(word + '\n')
        words.add(word)
        # Update the censor pattern
        compile_censor_pattern()

