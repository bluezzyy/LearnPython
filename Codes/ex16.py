# -*- coding: utf-8 -*-

#Exercise 16: Reading and Writing Files
# 文件的读取和写入
# Learn Python the Hard Way ---- 第二天
# Date： 2017/01/05

from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you dont want that,hit CTRL-C."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, "w")  # 清空文件需要 "w" 写入权限

print "Truncating the file. Goodbye!"
target.truncate()  # 首先清空文件中的内容

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")  #再往里添加内容
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()   # 最后关闭文件
