# -*- coding: utf-8 -*-

# Exercise 40: Modules, Classes, and Objects
# 模块，类，对象
# Learn Python the Hard Way ---- 第三天
# Date： 2017/01/06  09:37

import ex40_apple # 自定义模块

# 使用说明：输入python 然后improt ex40_apple 再import ex40 搞掂!
# ex40_apple.apple()
# ex40_apple.pen()
# ex40_apple.apple_pen()

# ex40_apple.apple

class Song(object):
	"""docstring for Song"""
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
happy_baby = Song(["Happy brithday to you","I don't want to get sued","So I'll stop right there."])

bulls_on_parade = Song(["They say I'm blue","But I don't think so."])

happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
