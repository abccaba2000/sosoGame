import lib_block
import random

class bBlock(lib_block.Block) :


	def update(self):

		self.rect.y += 2

		if self.rect.y + self.rect.height > self.scrsize[1] :
			self.rect.x = random.randrange(0, self.scrsize[0] - self.rect.width + 1)
			self.rect.y = - self.rect.height
