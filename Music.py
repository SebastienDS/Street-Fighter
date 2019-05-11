import pygame

class Music:
	def __init__(self):
		self.son = {}
		self.volume = 1

		self.charger_son()


	def charger_son(self):
		self.son["attaque"] = pygame.mixer.Sound("son/47H.wav")
		self.son["attaque2"] = pygame.mixer.Sound("son/48H.wav")
		self.son["fight"] = pygame.mixer.Sound("son/56H.wav")


	def play_background(self, nom):
		pygame.mixer.music.load(nom)
		pygame.mixer.music.play(-1)


	def play_son(self, nom):
		#joue le son 1 fois
		self.son[nom].play()


	def volume_son(self, nbr):
		self.volume += nbr
		for key in self.son.keys():
			self.son[key].set_volume(self.volume)
		pygame.mixer.music.set_volume(self.volume)
