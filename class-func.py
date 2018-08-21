
# CamelCase is not the python_convention

class pet:
	number_of_legs = 0

	def sleep(self):
		print "zzz"

	def count_legs(self):
		print "I have %s legs" % self.number_of_legs

class dog(pet):
	def bark(self):
		print "woof"

bird = pet()
bird.number_of_legs = 2
bird.sleep()
bird.count_legs()

dd = dog()
dd.number_of_legs = 4
dd.bark()
dd.count_legs()
