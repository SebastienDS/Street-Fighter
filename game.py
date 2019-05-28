import pygame
import time
import os
import sys
import random

import Player
import IA
import Interface
import Replay
import son
from setting import setting



def main():
	pygame.init()
	os.environ['SDL_VIDEO_WINDOW_POS'] = "{}, {}".format(50, 200)   #position la fenetre a un endroit precis pour l'ouverture
	ecran = pygame.display.set_mode([setting["l_ecran"], int((setting["l_ecran"] * 448) / 1242)])			 #cree l'ecran
	pygame.display.set_caption(setting["titre"])			#change le titre de la fenetre

#---------------------------------------------- instanciation onjets ----------------------------------------------------------------------------------------

	interface = Interface.Interface(ecran)
	replay = Replay.Replay()
	pygame.mixer.music.set_volume(son.son["volume"]["volume"])

#-------------------------------------------------- boucle du jeu --------------------------------------------------------------------------------------------

	continuer = True
	menu_principal = True
	menu_choix_mode = False
	selecteur_perso = False
	choix_map = False
	init_player = False
	init_timer_debut = False
	mode = False
	menu_replay = False
	choix_replay = False
	menu_pause = False
	menu_fin_partie = False
	tutoriel = False
	entrainement = False


	while continuer:
		if menu_principal or menu_choix_mode:
			pygame.mixer.music.load(son.son["background"]["opening_theme"])
			pygame.mixer.music.play(-1)
		while menu_principal:
			for event in pygame.event.get():					#recupere les evenements
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == son.son["volume"]["volume_up"]:
						son.modif_volume(0.1)
					elif event.key == son.son["volume"]["volume_down"]:
						son.modif_volume(-0.1)
						
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1: 
						try:	
							if interface.rect_play.collidepoint(event.pos):
								menu_principal = False
								menu_choix_mode = True
							elif interface.rect_quit.collidepoint(event.pos):
								menu_principal = False
								continuer = False
						except Exception as e:
							print(e)

			interface.menu_principal()
			pygame.display.flip()


		while menu_choix_mode:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == son.son["volume"]["volume_up"]:
						son.modif_volume(0.1)
					elif event.key == son.son["volume"]["volume_down"]:
						son.modif_volume(-0.1)
					if event.key == pygame.K_ESCAPE:
						menu_choix_mode = False
						menu_principal = True

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						try:
							if interface.rect_1v1.collidepoint(event.pos):
								menu_choix_mode = False
								selecteur_perso = True
								mode = "1v1"
							elif interface.rect_1vsIA.collidepoint(event.pos):
								menu_choix_mode = False
								selecteur_perso = True
								mode = "1vsIA"						
							elif interface.rect_replay.collidepoint(event.pos):
								menu_choix_mode = False
								choix_replay = True
							elif interface.rect_tuto.collidepoint(event.pos):
								menu_choix_mode = False
								tutoriel = True
						except Exception as e:
							print(e)

			interface.menu_choix_mode()
			pygame.display.flip()


		if selecteur_perso:
			pygame.mixer.music.load(son.son["background"]["character_select"])
			pygame.mixer.music.play(-1)
		while selecteur_perso:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == son.son["volume"]["volume_up"]:
						son.modif_volume(0.1)
					elif event.key == son.son["volume"]["volume_down"]:
						son.modif_volume(-0.1)
					if event.key == pygame.K_ESCAPE:
						selecteur_perso = False
						menu_choix_mode = True
						mode = False
						interface = Interface.Interface(ecran)

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						try:
							if interface.rect_joueur1.collidepoint(event.pos):
								interface.choix_actif = "joueur1"
							elif interface.rect_joueur2.collidepoint(event.pos):
								interface.choix_actif = "joueur2"
							elif interface.rect_valider1.collidepoint(event.pos) and interface.choix_perso_joueur[0]:
								interface.validation[0] = True
								interface.choix_actif = "joueur2"
							elif interface.rect_valider2.collidepoint(event.pos) and interface.choix_perso_joueur[1]:
								interface.validation[1] = True
								interface.choix_actif = "joueur1"
							if interface.choix_actif:
								for perso in interface.rect_logo.keys():
									if interface.rect_logo[perso].collidepoint(event.pos) and interface.choix_actif == "joueur1":
										interface.choix_perso_joueur[0] = perso
										if interface.validation[0]:
											interface.validation[0] = False
									elif interface.rect_logo[perso].collidepoint(event.pos) and interface.choix_actif == "joueur2":
										interface.choix_perso_joueur[1] = perso
										if interface.validation[1]:
											interface.validation[1] = False
						except Exception as e:
							print(e)
						try:
							if interface.validation_finale.collidepoint(event.pos):
								selecteur_perso = False
								init_player = True	
								choix_map = True
						except:
							pass				

			interface.selecteur_perso()
			interface.bouton_selecteur()
			interface.perso_selected()
			interface.bouton_validation()
			interface.check_validation()

			if not interface.init_ia and mode == "1vsIA":
				interface.choix_perso_IA()
				interface.init_ia = True
			pygame.display.flip()


		if init_player:	
			if mode == "1v1":
				joueur1 = Player.Player(ecran, interface.choix_perso_joueur[0], 1, setting["speed"], (0,0,255))
				joueur2 = Player.Player(ecran, interface.choix_perso_joueur[1], 2, setting["speed"], (255,0,0))
				init_player = False
			elif mode == "1vsIA":
				joueur1 = Player.Player(ecran, interface.choix_perso_joueur[0], 1, setting["speed"], (0,0,255))
				joueur2 = IA.IA(ecran, interface.choix_perso_joueur[1], 2, setting["speed"], (255,0,0))
			interface = Interface.Interface(ecran)
			replay.reset_data()
			interface.transition((255,255,255))
			init_player = False

		if choix_map:
			interface.icone_map()
		while choix_map:
			for event in pygame.event.get():					#recupere les evenements
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == son.son["volume"]["volume_up"]:
						son.modif_volume(0.1)
					elif event.key == son.son["volume"]["volume_down"]:
						son.modif_volume(-0.1)
					if event.key == pygame.K_ESCAPE:
						choix_map = False
						selecteur_perso = True
						mode = False

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1: 
						try:
							for i in range(len(interface.rect_map)-1, -1, -1):
								if interface.rect_map[i].collidepoint(event.pos):
									interface.num_map = i + 1
					
							if interface.num_map and interface.validation_finale_map.collidepoint(event.pos):
								choix_map = False
								init_timer_debut = True
						except Exception as e:
							print(e)

			ecran.fill((0,0,0))
			interface.choix_map()
			interface.afficher_choix_map()	
			interface.afficher_icone_map_choisie()	
			interface.validation_map()		
			pygame.display.flip()

			
		if init_timer_debut:
			interface.transition((255,255,255))
			pygame.mixer.music.fadeout(250)	
			interface.timer_debut_partie(joueur1, joueur2)
			pygame.event.clear()

			musique = son.son["map"][random.choice(list(son.son["map"].keys()))]
			init_timer_debut = False
			
		if mode:
			try:
				pygame.mixer.music.fadeout(250)
				pygame.mixer.music.load(musique)
				pygame.mixer.music.set_volume(son.son["volume"]["volume"])
				pygame.mixer.music.play(-1)
			except Exception as e:
				print(e)		
		while mode:
			for event in pygame.event.get():					
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == son.son["volume"]["volume_up"]:
						son.modif_volume(0.1)
					elif event.key == son.son["volume"]["volume_down"]:
						son.modif_volume(-0.1)
					if event.key in [setting["touche_joueur1"]["pause"], setting["touche_joueur2"]["pause"]]:
						menu_pause = True
						mode = False
					if event.key == pygame.K_ESCAPE:
						mode = False
						menu_choix_mode = True

				joueur1.input_player(event)
				joueur2.input_player(event)

			joueur1.recup_action_active()													
			joueur2.recup_action_active()

			joueur1.update_hit_box(joueur2)
			joueur2.update_hit_box(joueur1)
			
			joueur1.gerer_degat(joueur2)
			joueur2.gerer_degat(joueur1)
			joueur1.reset_combo()
			joueur2.reset_combo()

			replay.add_data(joueur1, joueur2)
			#joueur1.afficher()
			#joueur2.afficher()

			interface.draw_bg()
			interface.barre_de_vie(joueur1, joueur2)
			joueur1.draw()
			joueur2.draw()
			
			interface.afficher_combo(joueur1, 50, 75)
			interface.afficher_combo(joueur2, 900, 75)
			quitter = interface.temps()
			pygame.display.flip()
			pygame.time.Clock().tick(setting["fps"])

			if joueur1.vie <= 0 or joueur2.vie <= 0 or quitter:
				menu_fin_partie = True
				mode = False

				interface.afficher_fin_de_partie(joueur1, joueur2)
				if joueur1.vie > joueur2.vie:
					interface.transition(joueur1.couleur)
				else:
					interface.transition(joueur2.couleur)
		pygame.mixer.music.fadeout(250)
	

		if menu_pause:	
			pygame.mixer.music.load(son.son["background"]["character_select"])
			pygame.mixer.music.play(-1)
		while menu_pause:
			for event in pygame.event.get():					
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == son.son["volume"]["volume_up"]:
						son.modif_volume(0.1)
					elif event.key == son.son["volume"]["volume_down"]:
						son.modif_volume(-0.1)

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						if interface.rect_continuer.collidepoint(event.pos):
							mode = True
							menu_pause = False
							
						elif interface.rect_quitter.collidepoint(event.pos):
							menu_pause = False
							menu_principal = True

			interface.menu_pause()
			pygame.display.flip()


		if menu_replay:
			try:
				replay.load_replay("replay" + str(replay.replay_selected), interface, joueur1, joueur2)
			except Exception as e:
				print(e)
				joueur1 = Player.Player(ecran, "ken", 1, setting["speed"], (0,0,255))
				joueur2 = Player.Player(ecran, "ken", 2, setting["speed"], (255,0,0))
				replay.load_replay("replay" + str(replay.replay_selected), interface, joueur1, joueur2)
			interface.transition((255,255,255))
			pygame.mixer.music.fadeout(250)	
			interface.timer_debut_partie(joueur1, joueur2)
			pygame.event.clear()

			try:
				pygame.mixer.music.load(son.son["map"][random.choice(list(son.son["map"].keys()))])
				pygame.mixer.music.set_volume(son.son["volume"]["volume"])
				pygame.mixer.music.play()
			except Exception as e:
				print(e)	
		while menu_replay:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == son.son["volume"]["volume_up"]:
						son.modif_volume(0.1)
					elif event.key == son.son["volume"]["volume_down"]:
						son.modif_volume(-0.1)
					if event.key == pygame.K_ESCAPE:
						menu_replay = False
						choix_replay = True

			replay.load_data(joueur1, joueur2)
			joueur1.recup_action_active()													
			joueur2.recup_action_active()

			interface.draw_bg()
			interface.barre_de_vie(joueur1, joueur2)
			interface.afficher_replay()
			joueur1.draw()
			joueur2.draw()

			pygame.display.flip()

			if len(replay.data_player1["posX"]) > 80:
				pygame.time.Clock().tick(setting["fps"])
			else:
				pygame.time.Clock().tick(setting["slow_fps"])

			if joueur1.vie <= 0 or joueur2.vie <= 0:
				menu_fin_partie = True
				menu_replay = False
				replay.replay_selected = None

				interface.afficher_fin_de_partie(joueur1, joueur2)
				if joueur1.vie > joueur2.vie:
					interface.transition(joueur1.couleur)
				else:
					interface.transition(joueur2.couleur)
		pygame.mixer.music.fadeout(250)


		if menu_fin_partie:
			pygame.mixer.music.load(son.son["background"]["ending_theme"])
			pygame.mixer.music.play(-1)
			if len(replay.data_player1["posX"]):
				couleur_save = (255,255,255)
			elif not(replay.data_player1["posX"]):
				couleur_save = (255,0,0)
		while menu_fin_partie:
			for event in pygame.event.get():					#recupere les evenements
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == son.son["volume"]["volume_up"]:
						son.modif_volume(0.1)
					elif event.key == son.son["volume"]["volume_down"]:
						son.modif_volume(-0.1)
					if event.key == pygame.K_ESCAPE:
						menu_fin_partie = False
						menu_principal = True
						interface.transition((0,0,0))

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1: 
						try:
							if interface.rect_menu.collidepoint(event.pos):
								menu_choix_mode = True
								menu_fin_partie = False
								interface.transition((255,255,255))
							
							elif interface.rect_quit.collidepoint(event.pos):
								menu_fin_partie = False
								continuer = False

							elif interface.rect_save.collidepoint(event.pos):
								if len(replay.data_player1["posX"]):
									menu_fin_partie = False
									choix_replay = "save"

						except Exception as e: 
							print(e)

			interface.fin_de_partie(joueur1, joueur2, couleur_save)
			pygame.display.flip()


		if choix_replay:
			pygame.mixer.music.load(son.son["background"]["ending_theme"])
			pygame.mixer.music.play(-1)
		while choix_replay:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == son.son["volume"]["volume_up"]:
						son.modif_volume(0.1)
					elif event.key == son.son["volume"]["volume_down"]:
						son.modif_volume(-0.1)
					if event.key == pygame.K_ESCAPE:
						if choix_replay == "save":
							choix_replay = False
							menu_fin_partie = True
						else:
							choix_replay = False
							menu_choix_mode = True
							replay.replay_selected = None

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						try:
							if interface.r_replay1.collidepoint(event.pos):
								replay.replay_selected = 1
							elif interface.r_replay2.collidepoint(event.pos):
								replay.replay_selected = 2
							elif interface.r_replay3.collidepoint(event.pos):
								replay.replay_selected = 3
							elif interface.bouton_ok.collidepoint(event.pos) and replay.replay_selected:
								if choix_replay == "save":
									replay.save_replay("replay" + str(replay.replay_selected), interface.num_map, joueur1.nom, joueur2.nom)
									choix_replay = False
									menu_principal = True
									replay.replay_selected = None
								else:
									choix_replay = False
									menu_replay = True
						except Exception as e:
							print(e)

			interface.choix_replay(replay)
			pygame.display.flip()


		if tutoriel:
			pygame.mixer.music.load(son.son["background"]["ending_theme"])
			pygame.mixer.music.play(-1)
		while tutoriel:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == son.son["volume"]["volume_up"]:
						son.modif_volume(0.1)
					elif event.key == son.son["volume"]["volume_down"]:
						son.modif_volume(-0.1)
					if event.key == pygame.K_ESCAPE:
						tutoriel = False
						menu_choix_mode = True

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						try:
							if interface.r_retour.collidepoint(event.pos):
								tutoriel = False
								menu_choix_mode = True
							elif interface.r_entrainement.collidepoint(event.pos):
								tutoriel = False
								entrainement = True
						except Exception as e:
							print(e)

			ecran.fill((255,255,255))
			interface.aide()
			interface.bouton_aide()
			pygame.display.flip()




		if entrainement:
			interface.create_box(15)
			perso = random.choice(["ken", "ryu", "cammy"])
			joueur1 = Player.Player(ecran, perso, 1, setting["speed"], (0,0,255))
			interface.num_map = random.randrange(1, 7)
			interface.load_record()
			interface.transition((255,255,255))
			musique = son.son["map"][random.choice(list(son.son["map"].keys()))]
			try:
				pygame.mixer.music.fadeout(250)
				pygame.mixer.music.load(musique)
				pygame.mixer.music.set_volume(son.son["volume"]["volume"])
				pygame.mixer.music.play(-1)
			except Exception as e:
				print(e)	
			
			interface.debut_entrainement = time.time()
		while entrainement:
			for event in pygame.event.get():					
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == son.son["volume"]["volume_up"]:
						son.modif_volume(0.1)
					elif event.key == son.son["volume"]["volume_down"]:
						son.modif_volume(-0.1)
					if event.key == pygame.K_ESCAPE:
						entrainement = False
						tutoriel = True

				joueur1.input_player(event)

			joueur1.recup_action_active()
			joueur1.update_hit_box(joueur1)		
														
			interface.draw_bg()
			joueur1.draw()
			interface.tutoriel()
			
			pygame.draw.rect(ecran, (0,255,0), interface.box_tuto[0])
			interface.gerer_box_tuto(joueur1)
			interface.nbr_box_restantes()
			

			pygame.display.flip()
			pygame.time.Clock().tick(setting["fps"])

			if not len(interface.box_tuto):
				interface.temps_entrainement = time.time() - interface.debut_entrainement
				interface.save_record()
				entrainement = False
				tutoriel = True
				time.sleep(1)
				interface.transition((255,255,255))
		pygame.mixer.music.fadeout(250)




if __name__ == '__main__':
	main()
