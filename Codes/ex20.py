# -*- coding: utf-8 -*-

# Exercise 20: Functions and Files
# 函数 与 文件
# Learn Python the Hard Way ---- 第二天
# Date： 2017/01/05  10:12 am

from sys import argv
script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count,f):
	print line_count, f.readline()

current_file = open(input_file)

print "Fist let's print the whole file:"
print_all(current_file)

print "Now let's rewind,kind of like a tape"
rewind(current_file)

print "Now let's print a line:"
current_line = 1
print_a_line(current_line, current_file)

current_line +=1
print_a_line(current_line,current_file)

current_line +=1
print_a_line(current_line,current_file)