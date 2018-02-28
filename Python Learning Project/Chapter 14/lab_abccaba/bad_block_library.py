import block_library
import random


class Bad_block(block_library.Block):
	def update(self):
		self.rect.y += 1
		import hw_lab_abccaba_collide
		if self.rect.y >= hw_lab_abccaba_collide.HEIGHT:
			self.rect.y = -10