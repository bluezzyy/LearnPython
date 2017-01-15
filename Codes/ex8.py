# -*- coding: utf-8 -*-

#ex8: Printing Printing

# Note: 当你使用中文的时候 不能使用%r 应该换成%s

formatter = "%r %r %s %r"
print formatter %(1,2,3,4)
print formatter %("one","two","three","four")
print formatter %(True, False, False, True)
print formatter %(formatter,formatter,formatter,formatter)
print formatter %(
	"I had this thing.",
	"That you could type up right.",
	"But 这个 didn't sing.",
	"So I said goodnight."
	)