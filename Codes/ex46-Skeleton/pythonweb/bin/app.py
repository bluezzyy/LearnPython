# -*-  coding: utf-8  -*-

import web

# 定义request的路径
urls = (
	'/hello','Index'
	)

app = web.application(urls,globals())

# 模板路径
render = web.template.render('templates/',base="layout")

"""
重要提示！：当前项目的目录为
./bin:           ./docs:   ./pythonweb:     
app.py	app.pyc             __init__.py

./templates:  ./tests:
index.html    __init__.py

因此，必须在顶目录下运行py程序：python bin/app.py
这样才能去templates/目录下找到index模块，否则会报错
"""
class Index(object):
	def GET(self):
		return render.hello_form()
		pass
	def POST(self):
		form = web.input(name="Blue",name1="Hello")
		greeting = "Hello, %s and %s" %(form.name,form.name1)
		return render.index(greeting = greeting)


if __name__ == "__main__":
	app.run()
