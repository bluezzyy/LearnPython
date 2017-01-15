# -*- coding: utf-8 -*-

# Exercise 19: Functions and Variables
# 函数 与 变量
# Learn Python the Hard Way ---- 第二天
# Date： 2017/01/05  9:54 am

def cheese_and_crackers(cheese_count, box_of_cracker):
	print "You have %d cheese" % cheese_count
	print "You have %d cracker" % box_of_cracker
	print "Man it's enough for the party!"
	print "Let's have a blanket \n"

# there are first way to finish the function
print "there are first way to finish the function"
cheese_and_crackers(20,30)

# there are second way to finish the function
print "we can use variables to finish this function"
cheese_count_two = 20
box_of_cracker_two = 30
cheese_and_crackers(cheese_count_two, box_of_cracker_two)  # use variables

print "there are third way to finish the function"
cheese_and_crackers(10+10,20+10)

print "there are forth way to finish the function"
cheese_and_crackers(cheese_count_two+10, box_of_cracker_two+10)