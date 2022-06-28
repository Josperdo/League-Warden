#For tracking user info when in game
import time

class User:
	def __init__(self, id, game):
		self.id = str(id)
		self.game = game
		self.last_update = time.time()