# -*- coding: utf-8 -*-

# use read & script to finish the test
# Learn Python the Hard Way   ----第二天
# Date: 2017/01/05

from sys import argv

script = argv

print "please input the filename:"
filename = raw_input(">")
print "We are open the file %r:" %filename
target = open(filename, "r")  # 打开文件
result = target.read()  # 读取文件

print "%r" %result

