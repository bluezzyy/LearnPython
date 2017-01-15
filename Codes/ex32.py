# -*- coding: utf-8 -*-

# Exercise 32: Loops and Lists
# 循环和列表
# 学会通过for循环来添加和输出数据
# Learn Python the Hard Way ---- 第二天
# Date： 2017/01/05  16:29

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop to output data
for i in the_count:
	print "The count is %d" %i

for i in fruits:
	print "I got %r fruit" %i

for i in change:
	print "I got %r in the change."

# build a empty list
element = []

# add elements into the empty list
for i in xrange(1,6):
	print "Adding %d to the list" %i
	element.append(i)

# output the elements
for i in element:
	print "The element is %d" %i



