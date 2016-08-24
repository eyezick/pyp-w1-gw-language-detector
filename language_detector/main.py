# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from .languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    # implement your solution here
    words = text.split()
    count_dict ={}
    
    def word_count(words,common_words):
        """ Returns the common word count given the list of words in a given text. """
        count = 0
        for word in words:
            if word in common_words:
                count+=1
        return count
        
    for elem in LANGUAGES:
        """ Loops through each language and calculates the corresponding common word count. """
        lang = elem['name']
        com_words = elem['common_words']
        common_count = word_count(words,com_words)
        count_dict[lang] = common_count
    
    def language_detector(count_dict):
        """ Returns the language that has maximum count. """
        max_value = max(count_dict.values())
        for key in count_dict.keys():
            if max_value == count_dict[key]:
                return key
    
    
    return language_detector(count_dict)
    
    
    