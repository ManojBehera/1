class Parent:
	def __init__(self):
		print "Parent Constructer"
	def parentMethod(self):
		print "parent method"
class child(Parent):
	def __init__(self):
		print "child Constructer"
	def childMethod(self):
		print "child method"
c=child()
c.childMethod()

