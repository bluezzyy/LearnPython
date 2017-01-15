# -*- coding : utf-8 -*-

# ex13: Parameters, Unpacking, Variables
# 通过raw_input的方式再输出一个参数
# Learn Python By Hard Way ---- 第一天
# Date： 2017/01/04

from sys import argv

script, first, second = argv
third = raw_input("The Third argv:")  # combine argv with raw_input()

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your thrid variable is:", third
