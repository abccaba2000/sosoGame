==Section 12.4.2==

class Cat :

	def __init__(self) :
		self.name = "foo"
		self.color = "milk"
		self.weight = 50

	def meow(self) :
		print(self.name, "meow~~")

cat = Cat()
cat.meow()


==Section 12.5.2==

1.

	'Class' names should begin with upper case letter.

2.

	'Method' names should begin with lower case letter.

3.

	'Attribute' names should begin with lower case letter.

4.

	'Attributes' should be listed before 'Methods'.

5.

	'Address' is another name for a reference.

6.

	'Pointer' is another name for a instance variable.
	
7.

	'Object' is the name for an instance of a class.

8.

	class Star :

		def __init__(self) :
			print("A star is born")

	new_star = Star()

9.

	class Monster :

		def __init__(self, hp, name) :

			self.hp = hp
			self.name = name

		name = "fine"

	new_monster = Monster(30, "Moo-tongue-O")
	print(new_monster.name, new_monster.hp)
