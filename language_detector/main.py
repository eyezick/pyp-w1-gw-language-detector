# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    # implement your solution here
    words = text.split()
    count_dict ={}
    
    def word_count(words,common_words):
        count = 0
        for word in words:
            if word in common_words:
                count+=1
        return count
        
    for elem in LANGUAGES:
        lang = elem['name']
        com_words = elem['common_words']
        common_count = word_count(words,com_words)
        count_dict[lang] = common_count
    
    def language_detector(count_dict):
        max_value = max(count_dict.values())
        for key in count_dict.keys():
            if max_value == count_dict[key]:
                return key
    
    
    return language_detector(count_dict)
    
    # dictionary = {'Spanish': 0, 'Portuguese': 0}
    # for key in dictionary:
    #     dictionary[key] = word_count(words, common_words)
        
    
    
    