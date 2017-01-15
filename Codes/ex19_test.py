# -*- coding: utf-8 -*-

# Exercise 19: Functions and Variables
# 函数 与 变量 练习 ---定义一个函数，并且用不同方式运行
# Learn Python the Hard Way ---- 第二天
# Date： 2017/01/05  10:04 am

# Note: 区分变量和字符串 字符串要用"" 变量需要初始化
def myFunc(name, address):
	print "Your name is %r" %name
	print "Your address is %r" %address

# The first way:
myFunc("Blue", "GZ")

# The second way:
name_var = "Blue"
address_var = "GZ"
myFunc(name_var, address_var)

# The third way:
myFunc(name_var+" Hobert",address_var +" LIWAN")

# The forth way:
myFunc(None,None)

