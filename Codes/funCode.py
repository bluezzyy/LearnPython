# -*- coding:utf-8 -*-
# Learn Python By Hard Way ---- 第一天
# Date： 2017/01/04

# 这个程序就是不停输出 / - | \ | 组成了一个循环的图案
# 但是同时...这也会导致卡死...
while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" %i,