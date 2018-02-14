class Animal():
	def __init__(self):
		self.name = ""
		print("An animal has been born.")
		
	def eat(self):
		# Basic report
		print("Munch munch.")
		
	def make_noise(self):
		# Basic report
		print("Grrr says "+self.name+".")
 
class Cat(Animal):
	def __init__(self):
		# Call the parent/super class constructor first
		super().__init__()
		print("A cat has been born.")
 
	def make_noise(self):
		# Basic report
		print("Meow says "+self.name+".")
 
class Dog(Animal):
	def __init__(self):
		# Call the parent/super class constructor first
		super().__init__()
		print("A dog has been born.")
 
	def make_noise(self):
		# Basic report
		print("Bark says "+self.name+".")

cat = Cat()
dog1 = Dog()
dog2 = Dog()
cat.name = 'Lily'
dog1.name = 'Billy'
dog2.name = 'John'
cat.eat()
cat.make_noise()
dog1.eat()
dog1.make_noise()
dog2.eat()
dog2.make_noise()