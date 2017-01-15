# -*- coding: utf-8 -*-

# Exercise 18: Names, Variables, Code, Functions
# 名称，变量，代码，函数
# Learn Python the Hard Way ---- 第二天
# Date： 2017/01/05  9:40 am

# this one is like your script with argv
def print_two(*args):  # 多个参数的第一种方法
	arg1, arg2 = args
	print "arg1 : %r, arg2: %r" %(arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):   # 多个参数的第二种方法
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes ont arguments
def print_one(arg1):  
	print "arg1 : %r" %arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Blue","Hobert")
print_two_again("Blue","Hobert")
print_one("Blue")
print_none()
