import os
import re

words = None
_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data(path):
    return os.path.join(_ROOT, 'data', path)


def get_words():
    if not words:
        load_words()
    return words


def censor(input_text):
    ret = input_text
    words = get_words()
    for word in words:
        curse_word = re.compile(re.escape(word), re.IGNORECASE)
        cen = '🤬'*len(word)
        ret = curse_word.sub(cen, ret)
    return ret


def load_words(wordlist=None):
    global words
    if not wordlist:
        filename = get_data('wordlist.txt')
        f = open(filename)
        wordlist = f.readlines()
        wordlist = [w.strip() for w in wordlist if w]
    words = wordlist


def contains_profanity(input_text):
    return input_text != censor(input_text)


def censor_count(input_text):
    count = 0
    ret = input_text
    words = get_words()
    for word in words:
        curse_word = re.compile(re.escape(word), re.IGNORECASE)
        count += len(curse_word.findall(ret))
    return count


def add_bad_word(word):
    words = get_words()

    if word not in words:
        wordlist = os.path.join(_ROOT, 'data', 'wordlist.txt')
        with open(wordlist, 'a') as f:
            f.write(word + '\n')
