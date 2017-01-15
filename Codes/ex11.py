# -*- coding: utf-8 -*-

#ex11: Asking Questions
# Learn Python By Hard Way ---- 第一天
# Date： 2017/01/04

print "How old are you?",
age = raw_input()  # raw_input函数是python内置的，用于接收终端输入
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall, %r weight." %(age,height,weight)