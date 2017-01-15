from nose.tools import *
from bin.app import
from test.tools import *

def test_index():
	# check that we get a 404 on the / URL
	resp = app.request("/")
	asser_response(resp,status = "404")

	# test our first GET request to /hello
	resp = app.request("/hello")
	asser_response(resp)

	# make sure default values work for the form
	resp = app.request("/hello",method="POST")
	asser_response(resp,contains="Nobody")

	#test that we get expected values
	data = {'name':'Blue','greet':'Hola'}
	resp = app.request("/hello", method="POST",data=data)
	assert_response(resp,contains="Blue")
	