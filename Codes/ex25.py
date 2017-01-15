# -*- coding: utf-8 -*-

# Exercise 25: Even More Practice
# 练习 练习 再练习
# Learn Python the Hard Way ---- 第二天
# Date： 2017/01/05  14:13

def break_words(stuff):
	""" This fuction will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	""" sorts the words. """
	return sorted(words)

def print_first_word(words):
	""" Prints the first word"""
	word = words.pop(0)
	print word

def print_last_word(words):
	""" Print the last word """
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	""" Takes in a full sentence """
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	""" Print the first and last """
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sort(sentence):
	""" Sorts the words then print first and last """
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	