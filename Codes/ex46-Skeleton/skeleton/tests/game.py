# -*- coding: utf-8 -*-

# EExercise 47: Automated Testing
# 自动测试
# Learn Python the Hard Way ---- 第四天
# Date： 2017/01/09  10:19

class Room(object):
	"""docstring for Room"""
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}

	def go(self,direction):
		return self.paths.get(direction,None)

	def add_paths(self,paths):
		self.paths.update(paths)
