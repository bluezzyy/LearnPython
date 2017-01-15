# -*- coding: utf-8 -*-

# Exercise 44: Inheritance Versus Composition
# 继承和构成
# Learn Python the Hard Way ---- 第四天
# Date： 2017/01/09  09:17

class Parent(object):
	def override(self):
		print "PARENT override()"

class Other(object):
	"""docstring for Other"""
	def override(self):
		print "OTHER override()"

	def implicit(self):
		print "OTHER implicit()"

	def  altered(self):
		print "OTHER altered()"
		

class Child(object):
	def __init__(self):
		# 初始化为Other类
		self.other = Other()

	def override(self):
		print "CHILD override() before"
		# # 在子类中调用父类方法
		# super(Child,self).override()
		# print "CHILD override() after"

	"""这是python继承的一种用法，在一个类中初始化另外一个类，然后重写方法。
	首先在init方法中初始化，然后自定义方法中调用父类方法。
	最后直接调用子类方法即可实现父类方法。
	"""
	def implicit(self):
		self.other.implicit()

	def altered(self):
		print "child , before other altered()"
		self.other.altered()
		print "child, after other altered()"

# 调用父类方法
son = Child()
son.override()
son.implicit()
son.altered()
	
						