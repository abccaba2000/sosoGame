import block_library
import random

class Good_block(block_library.Block):
	def update(self):
		r = random.randint(-3,3)
		self.rect.x += r
		r = random.randint(-3,3)
		self.rect.y += r