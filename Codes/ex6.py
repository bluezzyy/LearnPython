# -*- coding: utf-8 -*-

# ex6: String And Text

x = "There are %d types of people" %10
binary = "binary"  # 赋值
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)  #y变量用binary和do_not表示
print x  # 输出x
print y  # 输出y
print "I said %r" %x  
print "I also said %s" %y  # 这种输出没有“”
print "I also said %r" %y  # 这种输出 y变量有“”括起来

w = "This is the left side..."
e = "This is the right string side"

print w+e  # 输出w 和 e两个字符串

