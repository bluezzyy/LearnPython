# -*- coding: utf-8 -*-

# Exercise 17: More Files
# 多个文件
# Learn Python the Hard Way ---- 第二天
# Date： 2017/01/05

from sys import argv
from os.path import exists

# 输入两个参数，分别为 源文件 和 副本文件
script, from_file, to_file = argv

print "Copying from Copying %s to %s" %(from_file, to_file)

# we could do these two on to one line, how?
in_file = open(from_file)   # origin
indata = in_file.read()

# just like this, easy right?
# indata = open(from_file).read()   # 使用一行代码的时候不需要close() python会读取完自动关闭

print "The input file is %d bytes long" %len(indata)   # 输出源文件的字节数

print "Does the output file exits: %r" %exists(to_file)  #判断副本文件是否存在
print "Ready, hit RETURN to continue, CTRL-C to abort."

raw_input("?")
out_file = open(to_file,"w")  # origin
out_file.write(indata)

# out_file = open(to_file, "w").write(indata)  # 往副本文件中写入数据  # modify

print "Alright, all done."
out_file.close()  # 关闭源文件
in_file.close()   # 关闭副本文件