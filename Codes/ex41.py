# -*- coding: utf-8 -*-

# Exercise 41: Learning To Speak Object Oriented
# 学习面向对象的编程思想
# Learn Python the Hard Way ---- 第三天
# Date： 2017/01/06  11:41

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%)": "Make a class named %%% that is %%%",
	"class %%%(object):\n\t def __init__(self,***)":
	"class %%% has-a __init___ that takes self and *** parameters.",
	"class %%%(object):\n\t def ***(self,@@@)":
	"class %%% has-a function named *** that takes slef and @@@ parameters.",
	"*** = @@@()":"set *** to an instance of class @@@",
	"***.***(@@@)":"from *** get *** function and call with self and @@@ parameters.",
	"***.*** = '***'":"from *** get *** attribut and set to ***"
}

#do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASES_FIRST = True
else:
	PHRASES_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	 # strip()函数 复制并移除()中的字符串 例如：'  example  '.strip() = example 
	WORDS.append(word.strip()) 

# capitalize()函数 复制字符串 首字符大写，其余小写
def convert(snippet,phrase):
	class_names = [w.capitalize() for w in 
				random.sample(WORDS,snippet.count("%%%"))]
	# random.sample()函数 返回参数长度
	other_names = random.sample(WORDS,snippet.count("***"))
	results = []
	param_names = []

	for i in range(0,snippet.count("@@@")):
		# random.randint()函数 返回一个随机数N  a< N < b
		param_count = random.randint(1,3)
		param_names.append(",".join(random.sample(WORDS,param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]

        # fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)

        # fake other names
		for word in other_names:
			result = result.replace("***", word, 1)

        # fake parameter lists
		for word in param_names:
 			result = result.replace("@@@", word, 1)

		results.append(result)

	return results

	# keep going until they hit CTRL -D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASES_FIRST:
				question, answer = answer, question

			print question

			raw_input("> ")
			print "ANSWER:  %s\n\n" % answer
except EOFError:
	print "\nBye"
			