# -*- coding: utf-8 -*-

# Exercise 21: Functions Can Return Something
# 函数的返回值
# Learn Python the Hard Way ---- 第二天
# Date： 2017/01/05  11:23 am

def  add(a,b):
	print "ADDING %d and %d :" %(a,b)
	return a+b

def subtract(a,b):
	print "SUBTRACT %d and %d :" %(a,b)
	return a-b

def multiply(a,b):
	print "MUTIPLY %d and %d:" %(a,b)
	return a*b

def divide(a,b):
	print "DIVIDE %d and %d:" %(a,b)
	return a/b

print "Let's do some math with just functions!"

age = add(30,5)
height = subtract(180,10)
weight = multiply(20,6)
iq = divide(200,1.5)

print "Age : %d , Height: %d, Weight: %d, IQ: %d" %(age,height,weight,iq)

print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "The answer is %d" %what
