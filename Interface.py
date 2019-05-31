import pygame
import time
import random
import son
from setting import setting

class Interface:
	def __init__(self, ecran):
		self.ecran = ecran
		self.image_map = {}
		self.logo_perso = {}
		self.rect_logo = {}
		self.image_active = None
		self.num_map = None
		self.timer = 120
		self.debut = time.time()
		self.myfont = pygame.font.Font("image/police.ttf", 70)
		self.font_barre_vie = pygame.font.Font("image/police.ttf", 40)
		self.font_menu = pygame.font.Font("image/police.ttf", 100)
		self.label = self.myfont.render(str(self.timer), 1, (0,0,0))
		self.rect = self.label.get_rect()
		self.choix_perso_joueur = [None, None]
		self.validation = [False, False]
		self.choix_actif = "joueur1"
		self.init_ia = False
		self.box_tuto = []
		self.record = None

		self.init_interface()


	def init_interface(self):
		self.charger_images()
		self.agrandir_taille()


	def draw_bg(self):
		self.ecran.blit(self.image_map["map" + str(self.num_map)], [0, 0])


	def charger_images(self):
		self.logo = pygame.transform.scale(pygame.image.load("image/logo.png").convert_alpha(), (500, 200))

		self.image_map["map1"] = pygame.image.load("image/Map/Map1.png").convert_alpha()
		self.image_map["map2"] = pygame.image.load("image/Map/Map2.png").convert_alpha()
		self.image_map["map3"] = pygame.image.load("image/Map/Map3.png").convert_alpha()
		self.image_map["map4"] = pygame.image.load("image/Map/Map4.png").convert_alpha()
		self.image_map["map5"] = pygame.image.load("image/Map/Map5.png").convert_alpha()
		self.image_map["map6"] = pygame.image.load("image/Map/Map6.png").convert_alpha()

		self.logo_perso["ken"] = pygame.transform.scale(pygame.image.load("image/ken/ken.png").convert_alpha(), (50, 70))
		self.logo_perso["ryu"] = pygame.transform.scale(pygame.image.load("image/ryu/ryu.png").convert_alpha(), (50, 70))
		self.logo_perso["cammy"] = pygame.transform.scale(pygame.image.load("image/cammy/cammy.png").convert_alpha(), (50, 70))
		self.logo_perso["t_hawk"] = pygame.transform.scale(pygame.image.load("image/t_hawk/t_hawk.png").convert_alpha(), (50, 70))


	def agrandir_taille(self):
		for key in self.image_map.keys():
			rect_image = self.image_map[key].get_rect()
			self.image_map[key] = pygame.transform.scale(self.image_map[key], [setting["l_ecran"], int((setting["l_ecran"] * 448) / 1242)])


	def temps(self):
		"""afficher le timer en partie"""
		if time.time() - self.debut > 1:
			self.debut = time.time()
			self.timer -= 1
			self.label = self.myfont.render(str(self.timer), 1, (0,0,0))
			self.rect = self.label.get_rect()
		
		if self.timer < 0:
			return True

		rect_ecran = self.ecran.get_rect()
		self.rect.top = rect_ecran.top
		self.rect.centerx = rect_ecran.centerx
		pygame.draw.rect(self.ecran, (255,255,255), self.rect)
		self.ecran.blit(self.label, self.rect)


	def menu_principal(self):
		self.ecran.fill((255,255,255))
		rect_ecran = self.ecran.get_rect()
		play = self.font_menu.render("JOUER", 1, (0,255,0))
		self.rect_play = play.get_rect()
		self.rect_play.x = 200
		self.rect_play.centery = rect_ecran.centery + 100

		quit = self.font_menu.render("QUITTER", 1, (255,0,0))
		self.rect_quit = quit.get_rect()
		self.rect_quit.right = rect_ecran.right - 200
		self.rect_quit.centery = rect_ecran.centery + 100

		pygame.draw.rect(self.ecran, (0,0,0), self.rect_play, 2)
		pygame.draw.rect(self.ecran, (0,0,0), self.rect_quit, 2)
		self.ecran.blit(play, self.rect_play)
		self.ecran.blit(quit, self.rect_quit)

		rect_logo = self.logo.get_rect()
		rect_logo.centerx = rect_ecran.centerx
		rect_logo.y = 50
		self.ecran.blit(self.logo, rect_logo)


	def menu_choix_mode(self):
		self.ecran.fill((255,255,255))
		rect_ecran = self.ecran.get_rect()
		choix = self.font_menu.render("choix mode de jeu", 1, (0,0,0))
		self.rect_choix = choix.get_rect()
		self.rect_choix.centerx = rect_ecran.centerx
		self.rect_choix.y = 40

		duo = self.myfont.render("2 joueurs", 1, (0,0,255))
		self.rect_1v1 = duo.get_rect()
		self.rect_1v1.x = 350
		self.rect_1v1.centery = rect_ecran.centery + 60

		solo = self.myfont.render("1 joueur", 1, (0,0,255))
		self.rect_1vsIA = solo.get_rect()
		self.rect_1vsIA.x = 50
		self.rect_1vsIA.centery = rect_ecran.centery + 60

		replay = self.myfont.render("replay", 1, (0,0,0))
		self.rect_replay = replay.get_rect()
		self.rect_replay.x = rect_ecran.centerx + 80
		self.rect_replay.centery = rect_ecran.centery + 120

		tuto = self.myfont.render("tutoriel", 1, (0,0,0))
		self.rect_tuto = tuto.get_rect()
		self.rect_tuto.right = rect_ecran.right - 50
		self.rect_tuto.centery = rect_ecran.centery + 120

		pygame.draw.rect(self.ecran, (0,0,0), self.rect_1v1, 2)
		pygame.draw.rect(self.ecran, (0,0,0), self.rect_1vsIA, 2)
		pygame.draw.rect(self.ecran, (0,0,0), self.rect_replay, 2)
		pygame.draw.rect(self.ecran, (0,0,0), self.rect_tuto, 2)
		self.ecran.blit(choix, self.rect_choix)
		self.ecran.blit(duo, self.rect_1v1)
		self.ecran.blit(solo, self.rect_1vsIA)
		self.ecran.blit(replay, self.rect_replay)
		self.ecran.blit(tuto, self.rect_tuto)


	def menu_pause(self):
		self.ecran.fill((0,0,0,))
		rect_ecran = self.ecran.get_rect()
		pause = self.font_menu.render("Pause", 1, (255,255,255))
		self.rect_pause = pause.get_rect()
		self.rect_pause.centerx = rect_ecran.centerx
		self.rect_pause.y = 50

		continuer = self.font_menu.render("continuer", 1, (0,255,255))
		self.rect_continuer = continuer.get_rect()
		self.rect_continuer.x = 150
		self.rect_continuer.centery = rect_ecran.centery + 100

		quitter = self.font_menu.render("quitter", 1, (0,255,255))
		self.rect_quitter = quitter.get_rect()
		self.rect_quitter.right = rect_ecran.right - 150
		self.rect_quitter.centery = rect_ecran.centery + 100

		pygame.draw.rect(self.ecran, (255,255,0), self.rect_continuer, 2)
		pygame.draw.rect(self.ecran, (255,255,0), self.rect_quitter, 2)
		self.ecran.blit(pause, self.rect_pause)
		self.ecran.blit(continuer, self.rect_continuer)
		self.ecran.blit(quitter, self.rect_quitter)


	def nom_barre_vie(self, joueur, couleur, position):
		"""dessine le nom des joueurs sur la barre de vie"""
		nom = self.font_barre_vie.render(joueur.nom, 1, couleur)
		rect_nom = nom.get_rect()
		rect_nom.center = position
		self.ecran.blit(nom, rect_nom)
		

	def barre_de_vie(self, joueur1, joueur2):
		rect_ecran = self.ecran.get_rect()
		fond_barre_de_vie = pygame.Rect(50, 20, rect_ecran.centerx * 0.75, 50)
		fond_barre_de_vie2 = pygame.Rect(rect_ecran.width - rect_ecran.centerx * 0.75 - 50, 20, rect_ecran.centerx * 0.75, 50)
		pygame.draw.rect(self.ecran, (0,0,0), fond_barre_de_vie)
		pygame.draw.rect(self.ecran, (0,0,0), fond_barre_de_vie2)

		taille_vie = pygame.Rect(52, 22, ((rect_ecran.centerx * 0.75 - 4) * joueur1.vie)/ 1000, 46)
		taille_vie2 = pygame.Rect(rect_ecran.width - rect_ecran.centerx * 0.75 - 48, 22, ((rect_ecran.centerx * 0.75 - 4) * joueur2.vie)/ 1000, 46)
		
		for perso, barre_vie in [(joueur1, taille_vie), (joueur2, taille_vie2)]:
			couleur = (0,255,0)
			if perso.vie <= setting["vie"] * 0.10:
				couleur = (255,0,0)
			elif perso.vie <= setting["vie"] * 0.4:
				couleur = (255,128,0)
			if perso.vie != 0:
				pygame.draw.rect(self.ecran, couleur, barre_vie)

		self.nom_barre_vie(joueur1, (0,0,255), fond_barre_de_vie.center)
		self.nom_barre_vie(joueur2, (255,0,0), fond_barre_de_vie2.center)


	def fin_de_partie(self, joueur1, joueur2, couleur_save):
		self.ecran.fill((0,0,0))
		rect_ecran = self.ecran.get_rect()
		menu = self.font_menu.render("MENU", 1, (0,255,0))
		self.rect_menu = menu.get_rect()
		self.rect_menu.x = 100
		self.rect_menu.centery = rect_ecran.centery + 125

		quit = self.font_menu.render("QUITTER", 1, (255,0,0))
		self.rect_quit = quit.get_rect()
		self.rect_quit.right = rect_ecran.right - 100
		self.rect_quit.centery = rect_ecran.centery + 125

		pygame.draw.rect(self.ecran, (255,255,255), self.rect_menu, 2)
		pygame.draw.rect(self.ecran, (255,255,255), self.rect_quit, 2)
		self.ecran.blit(menu, self.rect_menu)
		self.ecran.blit(quit, self.rect_quit)

		j1 = joueur1.logo.get_rect()
		j1.centerx = rect_ecran.width * 0.15
		j1.y = 50

		j2 = joueur2.logo.get_rect()
		j2.centerx = rect_ecran.width * 0.85
		j2.y = 50

		self.ecran.blit(joueur1.logo, j1)
		self.ecran.blit(joueur2.logo, j2)

		if joueur1.vie > joueur2.vie :
			win = self.font_menu.render(joueur1.nom + " WIN !", 1, (0,0,255))
			joueur_win = j1
			
		else :
			win = self.font_menu.render(joueur2.nom + " WIN !", 1, (255,0,0))
			joueur_win = j2
		
		joueur_win.width += 10
		joueur_win.height += 10
		joueur_win.x -= 5
		joueur_win.y -= 5

		self.rect_win = win.get_rect()
		self.rect_win.centerx = rect_ecran.centerx
		self.rect_win.y = 50
		#pygame.draw.rect(self.ecran, (255,255,255), self.rect_win)
		self.ecran.blit(win, self.rect_win)

		pygame.draw.rect(self.ecran, (0,255,0), joueur_win, 3) 

		save = self.font_menu.render("save", 1, (255,255,255))
		self.rect_save = save.get_rect()
		self.rect_save.centerx = rect_ecran.centerx
		self.rect_save.centery = rect_ecran.centery + 125
		pygame.draw.rect(self.ecran, couleur_save, self.rect_save, 2)
		self.ecran.blit(save, self.rect_save)



	def transition(self, couleur):
		alpha = 0
		while alpha <= 50:
			fond = pygame.Surface((self.ecran.get_rect().width, self.ecran.get_rect().height))
			fond.set_alpha(alpha)
			fond.fill(couleur)
			self.ecran.blit(fond, (0,0))
			pygame.display.flip()
			alpha += 1
			time.sleep(0.02)
			

	def selecteur_perso(self):
		self.ecran.fill((0,0,0))
		rect_ecran = self.ecran.get_rect()
		selecteur = self.myfont.render("Selecteur de personnage", 1, (255,255,255))
		self.rect_selecteur = selecteur.get_rect()
		self.rect_selecteur.centerx = rect_ecran.centerx
		self.rect_selecteur.y = 25

		ken = ("ken", rect_ecran.centerx - self.logo_perso["ken"].get_rect().width, rect_ecran.bottom - 100)
		ryu = ("ryu", rect_ecran.centerx + self.logo_perso["ryu"].get_rect().width, rect_ecran.bottom - 100)
		cammy = ("cammy", rect_ecran.centerx - self.logo_perso["cammy"].get_rect().width, rect_ecran.bottom - 200)
		t_hawk = ("t_hawk", rect_ecran.centerx + self.logo_perso["t_hawk"].get_rect().width, rect_ecran.bottom - 200)

		for nom, pos_centerx, pos_bottom in [ken, ryu, cammy, t_hawk]:
			self.rect_logo[nom] = self.logo_perso[nom].get_rect()
			self.rect_logo[nom].centerx = pos_centerx
			self.rect_logo[nom].bottom = pos_bottom
			
			self.bordure = self.logo_perso[nom].get_rect()
			self.bordure.width += 10
			self.bordure.height += 10
			self.bordure.x = self.rect_logo[nom].x - 5
			self.bordure.y = self.rect_logo[nom].y - 5

			self.ecran.blit(self.logo_perso[nom], self.rect_logo[nom])
			pygame.draw.rect(self.ecran, (255,255,255), self.bordure, 5)

		self.ecran.blit(selecteur, self.rect_selecteur)


	def perso_selected(self):
		"""si on clique sur un perso, il apparait en grand a coter"""
		rect_ecran = self.ecran.get_rect()
		if self.choix_perso_joueur[0]:
			perso = pygame.transform.scale(self.logo_perso[self.choix_perso_joueur[0]], (160, 200))
			rect_perso = perso.get_rect()
			rect_perso.x = 200
			rect_perso.y = 180
			self.ecran.blit(perso, rect_perso)

		if self.choix_perso_joueur[1]:
			perso = pygame.transform.scale(self.logo_perso[self.choix_perso_joueur[1]], (160, 200))
			rect_perso2 = perso.get_rect()
			rect_perso2.right = rect_ecran.right - 200
			rect_perso2.y = 180
			self.ecran.blit(perso, rect_perso2)


	def bouton_selecteur(self):
		"""bouton joueur1 et joueur2 pouvant etre utiliser pour changer le choix actif si on souhaite selectionner le joueur2 en premier"""
		rect_ecran = self.ecran.get_rect()
		joueur1 = self.font_barre_vie.render("Joueur 1", 1, (0,0,255))
		self.rect_joueur1 = joueur1.get_rect()
		self.rect_joueur1.x = 200
		self.rect_joueur1.y = 120
		self.ecran.blit(joueur1, self.rect_joueur1)

		joueur2 = self.font_barre_vie.render("Joueur 2", 1, (255,0,0))
		self.rect_joueur2 = joueur2.get_rect()
		self.rect_joueur2.right = rect_ecran.right - 220
		self.rect_joueur2.y = 120
		self.ecran.blit(joueur2, self.rect_joueur2)

		if self.choix_actif == "joueur1":
			couleur1 = (0,255,0)
			couleur2 = (255,255,255)
		elif self.choix_actif == "joueur2":
			couleur1 = (255,255,255)
			couleur2 = (0,255,0)
		else:
			couleur1 = (255,255,255)
			couleur2 = (255,255,255)

		pygame.draw.rect(self.ecran, couleur1, self.rect_joueur1, 1)
		pygame.draw.rect(self.ecran, couleur2, self.rect_joueur2, 1)


	def bouton_validation(self):
		"""bouton valider sous les grands image de perso, cadre vert quand le perso est valider"""
		rect_ecran = self.ecran.get_rect()
		valider = self.font_barre_vie.render("valider", 1, (255,255,255))
		self.rect_valider1 = valider.get_rect()
		self.rect_valider1.x = 210
		self.rect_valider1.y = 385
		self.ecran.blit(valider, self.rect_valider1)

		self.rect_valider2 = valider.get_rect()
		self.rect_valider2.right = rect_ecran.right - 220
		self.rect_valider2.y = 385
		self.ecran.blit(valider, self.rect_valider2)

		if not self.validation[0]:
			pygame.draw.rect(self.ecran, (255,255,255), self.rect_valider1, 1)
		else:
			pygame.draw.rect(self.ecran, (0,255,0), self.rect_valider1, 1)
		if not self.validation[1]:	
			pygame.draw.rect(self.ecran, (255,255,255), self.rect_valider2, 1)
		else:
			pygame.draw.rect(self.ecran, (0,255,0), self.rect_valider2, 1)


	def check_validation(self):
		"""si les 2 perso sont validés, bouton OK apparait permet de lancer la partie"""
		if self.validation.count(True) == 2 and not self.choix_perso_joueur.count(None):
			rect_ecran = self.ecran.get_rect()
			valider = self.font_barre_vie.render("OK", 1, (0,255,0))
			self.validation_finale = valider.get_rect()
			self.validation_finale.centerx = rect_ecran.centerx
			self.validation_finale.y = 360
			self.ecran.blit(valider, self.validation_finale)
			pygame.draw.rect(self.ecran, (0,255,0), self.validation_finale, 1)


	def choix_perso_IA(self):
		"""si le mode de jeu est 1 joueur, un perso pour le joueur2 est selectionné et validé automatiquement
			(ce choix peut etre changer par le joueur1)"""
		self.choix_perso_joueur[1] = random.choice(["ken", "ryu", "cammy", "t_hawk"])
		self.validation[1] = True


	def timer_debut_partie(self, joueur1, joueur2):
		"""effectue le decompte de debut de partie"""
		temps = 3
		son_compteur = pygame.mixer.Sound(son.son["compteur"]["compteur" + str(temps)])
		son_compteur.set_volume(son.son["volume"]["volume"])
		son_compteur.play()
		while temps >= 0:
			if time.time() - self.debut > 1:
				self.debut = time.time()
				t_temps = self.font_menu.render(str(temps), 1, (255,0,128))
				r_temps = t_temps.get_rect()
				r_temps.center = self.ecran.get_rect().center
				try:
					son_compteur = pygame.mixer.Sound(son.son["compteur"]["compteur" + str(temps)])
					son_compteur.set_volume(son.son["volume"]["volume"])
					son_compteur.play()
				except Exception as e:
					print(e)
					son_compteur = pygame.mixer.Sound(son.son["compteur"]["fight"])
					son_compteur.set_volume(son.son["volume"]["volume"])
					son_compteur.play()
				temps -= 1

				self.pos_debut_timer(joueur1, joueur2)
				self.ecran.blit(t_temps, r_temps)
				pygame.display.flip()


	def pos_debut_timer(self, joueur1, joueur2):
		"""met les joueurs en position pour demarrer la partie"""
		self.draw_bg()
		self.barre_de_vie(joueur1, joueur2)
		joueur1.victory2()
		joueur2.victory2()
		joueur1.draw()
		joueur2.draw()
		

	def afficher_fin_de_partie(self, joueur1, joueur2):
		temps = 5
		debut = time.time()
		while temps >= 0:
			if time.time() - debut > 0.5:
				debut = time.time()
				temps -= 1
				t_fin = self.font_menu.render("partie terminee", 1, (255,0,128))
				r_fin = t_fin.get_rect()
				r_fin.center = self.ecran.get_rect().center
				r_fin.y -= 50

				self.draw_bg()
				self.barre_de_vie(joueur1, joueur2)
				if joueur1.vie > joueur2.vie:
					joueur1.victory1()
				else:
					joueur2.victory1()
				joueur1.draw()
				joueur2.draw()
				self.ecran.blit(t_fin, r_fin)
				pygame.display.flip()


	def afficher_combo(self, joueur, posx, posy):
		if joueur.combo > 2:
			rect_ecran = self.ecran.get_rect()
			combo = self.myfont.render("combo: " + str(joueur.combo), 1, (255,0,128))
			self.rect_combo = combo.get_rect()
			self.rect_combo.x = posx
			self.rect_combo.y = posy

			self.ecran.blit(combo, self.rect_combo)


	def icone_map(self):
		self.icone_map = {}
		for key in self.image_map.keys():
			self.icone_map[key] = pygame.transform.scale(self.image_map[key], [setting["l_ecran"] // 5, int((setting["l_ecran"] * 448) / 1242) // 5])


	def choix_map(self):
		"""dessine les map en diagonale pour le menu du choix des maps"""
		self.rect_map = []
		for i in range(len(self.icone_map.keys())):
			rect = self.icone_map["map" + str(i + 1)].get_rect()
			rect.x = i * 175 + 30
			rect.y = i * 1.3 * self.icone_map["map" + str(i + 1)].get_rect().centery + 30
			self.rect_map.append(rect)
			cadre_map = self.icone_map["map" + str(i + 1)].get_rect()
			cadre_map.x = i * 175 + 30 - 2
			cadre_map.y = i * 1.3 * self.icone_map["map" + str(i + 1)].get_rect().centery + 30 - 2
			cadre_map.width += 4
			cadre_map.height += 4
			
			if self.num_map == i + 1:
				pygame.draw.rect(self.ecran, (0,255,0), cadre_map)
			self.ecran.blit(self.icone_map["map" + str(i + 1)], rect)


	def afficher_choix_map(self):
		rect_ecran = self.ecran.get_rect()
		choix_map_txt = self.font_menu.render("choix map", 1, (255,255,255))
		self.rect_choix_map = choix_map_txt.get_rect()
		self.rect_choix_map.x = 100
		self.rect_choix_map.bottom = rect_ecran.bottom - 50
		self.ecran.blit(choix_map_txt, self.rect_choix_map)


	def afficher_icone_map_choisie(self): 
		if self.num_map:
			map_choisie = self.icone_map["map" + str(self.num_map)]
			rect = map_choisie.get_rect()
			map_zoomed = pygame.transform.scale(map_choisie, (rect.width * 2, rect.height * 2))
			rect_map = map_zoomed.get_rect()
			rect_map.right = self.ecran.get_rect().right - 10
			rect_map.y = 10
			self.ecran.blit(map_zoomed, rect_map)


	def validation_map(self):
		if self.num_map:
			valider = self.myfont.render("OK", 1, (0,255,0))
			self.validation_finale_map = valider.get_rect()
			self.validation_finale_map.right = self.ecran.get_rect().right - 90
			self.validation_finale_map.y = 200
			self.ecran.blit(valider, self.validation_finale_map)
			pygame.draw.rect(self.ecran, (0,255,0), self.validation_finale_map, 1)


	def afficher_replay(self):
		"""affiche replay dans le jeu pour voir directement qu'un replay est en cours"""
		replay = self.font_menu.render("Replay", 1, (255,0,128))
		rect_replay = replay.get_rect()
		rect_replay.center = self.ecran.get_rect().center
		rect_replay.y -= 100
		self.ecran.blit(replay, rect_replay)


	def choix_replay(self, replay):
		"""3 bouton de replay pour choisir quel replay choisir"""
		if replay.replay_selected:
			couleur = (0,255,0)
		else:
			couleur = (255,255,255)
		self.ecran.fill((0,0,0))
		rect_ecran = self.ecran.get_rect()
		choix_replay = self.font_menu.render("choix replay", 1, (0,255,255))
		replay1 = self.font_menu.render("replay 1", 1, (255,255,255))
		replay2 = self.font_menu.render("replay 2", 1, (255,255,255))
		replay3 = self.font_menu.render("replay 3", 1, (255,255,255))
		bouton_ok = self.font_barre_vie.render("valider", 1, couleur)

		r_choix_replay = choix_replay.get_rect()
		self.r_replay1 = replay1.get_rect()
		self.r_replay2 = replay2.get_rect()
		self.r_replay3 = replay3.get_rect()
		self.bouton_ok = bouton_ok.get_rect()

		r_choix_replay.centerx = rect_ecran.centerx
		r_choix_replay.y = 50
		self.bouton_ok.centerx = rect_ecran.centerx
		self.bouton_ok.bottom = rect_ecran.bottom - 35

		for rect_replay in [self.r_replay1, self.r_replay2, self.r_replay3]:
			rect_replay.centery = rect_ecran.centery + 50
		self.r_replay1.x = 50
		self.r_replay2.centerx = rect_ecran.centerx
		self.r_replay3.right = rect_ecran.right - 50

		pygame.draw.rect(self.ecran, (255,255,255), self.r_replay1, 2)
		pygame.draw.rect(self.ecran, (255,255,255), self.r_replay2, 2)
		pygame.draw.rect(self.ecran, (255,255,255), self.r_replay3, 2)

		self.ecran.blit(choix_replay, r_choix_replay)
		self.ecran.blit(replay1, self.r_replay1)
		self.ecran.blit(replay2, self.r_replay2)
		self.ecran.blit(replay3, self.r_replay3)

		pygame.draw.rect(self.ecran, couleur, self.bouton_ok, 2)
		self.ecran.blit(bouton_ok, self.bouton_ok)


	def create_box(self, nbr):
		"""cree des carrés pour l'entrainement"""
		taille_box = 50
		self.box_tuto = []
		for i in range(nbr):
			x = random.randrange(self.ecran.get_rect().width - taille_box)
			bas = self.ecran.get_rect().height - taille_box
			y = bas - random.choice([0, 50, 100, 150, 200, 250])
			rect = pygame.Rect(x, y, taille_box, taille_box)
			self.box_tuto.append(rect)


	def gerer_box_tuto(self, joueur):
		"""test si l'attaque touche la box"""
		if joueur.attaque_hit_box:
			for hit_box in (joueur.attaque_hit_box):
				x, y, w, h = hit_box
				rect = pygame.Rect(x, y, w, h)
				try:
					if rect.colliderect(self.box_tuto[0]):
						self.box_tuto.pop(0)
				except Exception as e:
					print(e)


	def aide(self):
		"""menu aide avec affichage des touches de chaque joueurs"""
		rect_ecran = self.ecran.get_rect()

		aide = self.font_menu.render("aide", 1, (0,255,0))
		rect_aide = aide.get_rect()
		rect_aide.centerx = rect_ecran.centerx
		rect_aide.y = 75
		self.ecran.blit(aide, rect_aide)

		for num, i in [(1, 125), (2, 775)]:
			joueur = self.myfont.render("joueur " + str(num), 1, (0,0,0))
			rect_joueur = joueur.get_rect()
			rect_joueur.x = i
			self.ecran.blit(joueur, rect_joueur)

		for joueur, couleur, alignement in [("aide_joueur1", (0,0,255), 0), ("aide_joueur2", (255,0,0), 650)]:
			touche_perso = []
			action_touche = []
			for key in setting[joueur].keys():
				touche_perso.append(key)
			for action in setting["touche_joueur1"].keys():
				action_touche.append(action)
			for i in range(len(touche_perso)):
				action = self.font_barre_vie.render(f"{action_touche[i]}:", 1, couleur)
				rect = action.get_rect()
				rect.x = 100 + alignement
				rect.y = 100 + i * 30
				self.ecran.blit(action, rect)

				touche = self.font_barre_vie.render(setting[joueur][touche_perso[i]], 1, (0,0,0))
				rect_touche = touche.get_rect()
				rect_touche.x = rect.x + 175
				rect_touche.y = 100 + i * 30
				self.ecran.blit(touche, rect_touche)


	def bouton_aide(self):
		rect_ecran = self.ecran.get_rect()

		retour = self.font_barre_vie.render("retour", 1, (0,0,0))
		self.r_retour = retour.get_rect()
		self.r_retour.left = rect_ecran.centerx 
		self.r_retour.bottom = rect_ecran.bottom - 50
		self.ecran.blit(retour, self.r_retour)
		pygame.draw.rect(self.ecran, (0,0,0), self.r_retour, 2)

		entrainement = self.font_barre_vie.render("entrainement", 1, (0,0,0))
		self.r_entrainement = entrainement.get_rect()
		self.r_entrainement.right = rect_ecran.centerx - 40
		self.r_entrainement.bottom = rect_ecran.bottom - 50
		self.ecran.blit(entrainement, self.r_entrainement)
		pygame.draw.rect(self.ecran, (0,0,0), self.r_entrainement, 2)


	def tutoriel(self):
		"""affiche le temps actuel de l'entrainement ainsi que le record,
			change la couleur de bleu a rouge si le temps est > au record"""
		rect_ecran = self.ecran.get_rect()

		tuto = self.myfont.render("entrainement", 1, (255,0,128))
		r_tuto = tuto.get_rect()
		r_tuto.centerx = rect_ecran.centerx
		r_tuto.y = 10
		self.ecran.blit(tuto, r_tuto)
	
		if time.time() - self.debut_entrainement < self.record:
			couleur = (0,0,255)
		else:
			couleur = (255,0,0)
		mon_temps = self.myfont.render(f"Temps: {round(time.time() - self.debut_entrainement, 3)}", 1, couleur)
		r_temps = mon_temps.get_rect()
		r_temps.x = 50
		r_temps.y = 75
		self.ecran.blit(mon_temps, r_temps)

		temps_record = self.myfont.render(f"record: {self.record}", 1, couleur)
		r_record = temps_record.get_rect()
		r_record.right = rect_ecran.right - 50
		r_record.y = 75
		self.ecran.blit(temps_record, r_record)


	def nbr_box_restantes(self):
		"""affiche le nbr de box restantes a toucher"""
		rect_ecran = self.ecran.get_rect()

		nbr = self.myfont.render(str(len(self.box_tuto)), 1, (0,255,0))
		r_nbr = nbr.get_rect()
		r_nbr.centerx = rect_ecran.centerx
		r_nbr.y = 100
		self.ecran.blit(nbr, r_nbr)


	def save_record(self):
		if self.temps_entrainement < self.record:
			with open("record.txt", "w") as f:
				f.write(str(self.temps_entrainement))


	def load_record(self):
		with open("record.txt") as f:
			self.record = round(float(f.read()), 3)











	