# -*- coding: utf-8 -*-

# Exercise 14: Prompting and Passing
# 通过argv来设置user_name 并且通过raw_input()函数输入问题的答案
# Learn Python the Hard Way ---- 第一天
# Date： 2017/01/04
''' -----------------------------------
心得：								  |
这个真的是太好玩了 支持中文输入哦 哈哈哈~  |
------------------------------------''' 


from sys import argv

script, user_name = argv

# prompt = ">" #用于接受输入时的提示符号
prompt = "%s Input Here:" %user_name

print "Hi, I'm the %s script" % user_name
print "I'd like to ask you some questions."

print "Do you like me ? %s " % user_name  # 你喜不喜欢我！
likes = raw_input(prompt)

print "Where do you live? %s" % user_name  # 你家在哪！
lives = raw_input(prompt)

print "What kind of computer do you have?  %s" %user_name 
computer = raw_input(prompt)  # 你的新Mac呢！

print"""
Ok, now I do know you say %s about liking me, you are living on %s,
and you have a %s computer. 你这个逗逼!
""" %(likes,lives,computer)