# coding=utf-8           # -*- coding: utf-8 -*-
import sys
from random import randrange

def are_words_similar(w, w_orig):
    return (w[0] == w_orig[0]) and (w[len(w) - 2] == w_orig[len(w_orig) - 1])

def build_appropriate_word_list(dictionary, original_word):
    list = []
    for word in dictionary:
        if are_words_similar(word, original_word):
            list.append(word.rstrip('\n'))
    return list

def deprofanity(dictionary, str):
    lst = str.split()
    result = ""
    for s in lst:
        if s.find("*") >= 0:
            word_list = build_appropriate_word_list(dictionary, s.strip(",.!?"))
            result = result + ' ' + word_list[randrange(len(word_list))]
            if s.find(",.!?\n") >= 0:
                result = result + s[len(s) - 1]
            result = result + ' '
        else:
            result = result + ' ' + s
    return result
