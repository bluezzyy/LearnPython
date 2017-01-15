# -*- coding: utf-8 -*-

# Exercise 38: Doing Things to Lists
# 用列表搞事情
# Learn Python the Hard Way ---- 第二天
# Date： 2017/01/05  18:04

ten_things = "Apple Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Bnanna" 
		, "Girl", "Boy"]
# 输出初始化的list长度
length = len(stuff)
print "The origin stuff length is %d " %length
while len(stuff) !=10: 
	next_one = more_stuff.pop()  # 用于移除最后一个元素，并且返回值
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

print "There we go:", stuff

print "Let's do something with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()  # 移除最后一个值
print ' '.join(stuff) #每个值后面加空格
print '#'.join(stuff[3:5])  # 3 - 5之间的值