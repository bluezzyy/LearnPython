# -*- coding: utf-8 -*-

# Exercise 15: Reading Files
# 读取文件啦啦啦
# Learn Python the Hard Way ---- 第一天
# Date： 2017/01/04

from sys import argv 
#传入文件名当参数
fileName = raw_input(">")
txt = open(fileName)

print "Here's your file %r:" %fileName
print txt.read()
txt.close()

# 第二次读取文档
print "Type the filename again:"
file_again = raw_input(">")
txt_again = open(file_again)

print txt_again.read()
txt.close()

