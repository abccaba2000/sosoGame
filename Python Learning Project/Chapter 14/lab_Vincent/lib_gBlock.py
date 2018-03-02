import lib_block
import random

class gBlock(lib_block.Block) :

	def update(self):

		self.rect.x += random.randrange(-3, 4)
		self.rect.y += random.randrange(-3, 4)

		if self.rect.x < 0 :
			self.rect.x = 0

		if self.rect.x + self.rect.width > self.scrsize[0] :
			self.rect.x = self.scrsize[0] - self.rect.width

		if self.rect.y < 0 :
			self.rect.y = 0

		if self.rect.y + self.rect.height > self.scrsize[1] :
			self.rect.y = self.scrsize[1] - self.rect.height
