# -*- coding: utf-8 -*-

# Exercise 31: Making Decisions
# 拔剑吧！少年！
# Learn Python the Hard Way ---- 第二天
# Date： 2017/01/05  15:56

print "You enter a dark room with two doors.Do you go through door #1 or door #2?"

door = raw_input("Have a choice 😏  ")

if door == "1":
	print "The door 1 has been destroy.You can't go through it."
	print "So, now you have two choose:"
	print "1. go back home"
	print "2. choose another door"

	choose1 = raw_input(">")

	if choose1 == "1":
		print "Congratulation! You were eaten by monster! Game Over!"
	elif choose1 == "2":
		print "Wow. This is a giant world! You discover a new land!"
	else:
		print "Sorry...Crash..."

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	choose2 = raw_input("Have a choice 😏")
	if choose2 == "1":
		print "You choose 1,So,You win!"
	elif choose2 == "2":
		print "You choose 2.So,you lose!"
	else:
		print "eh...see you next time."
else:
	print "You must read the guide line carefully first."


