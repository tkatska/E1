import pytest
from hangman import get_word

def test_get_word():
    test_words_list = ['skillfactory','testing', 'blackbox']
    element = get_word(test_words_list)
    assert element in test_words_list