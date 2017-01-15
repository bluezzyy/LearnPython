# -*- coding: utf-8 -*-

# Exercise 39: Dictionaries, Oh Lovely Dictionaries
# oh 可爱的蓝精灵~
# Learn Python the Hard Way ---- 第三天
# Date： 2017/01/06  09:14

# Create a mapping
states = {
	'Oregon':'OR',
	'Florida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI'
}

cities = {
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Protland'

#print out some cities
print '-'*30
print "NY state has:", cities['NY']
print "OR state has:", cities['OR']

#print out some states
print '-'*30
print "Michigan's abbreviation is:", states['Michigan']
print "Oregon's abbreviation is:", states['Oregon']

#do it by using the state then cities dict
print '-'*30
print "Michigan has:",cities[states['Michigan']]

# print every state abbreviation
print '-'*30
for state, abbrev in states.items() : # 输出键值对
	print "%s is abbreviated %s" %(state,abbrev)

# print every state abbreviation keys
print '-'*30
for state in states.keys():  # 输出key
	print "%s is the keys" %state

# print every state abbreviation values
print '-' *30
for state in states.values(): # 输出value
	print "%s is the values" %state
