import pygame


setting = {
	"l_ecran": 1200,
	"titre": "STREET FIGHTER",
	"fps": 120,
	"slow_fps": 30,

	"speed": 3.5,
	"delai_reset_touche": 0.15,
	"cooldown_attaque": 0.5,
	"degat": 50,
	"vie": 1000,


	"touche_joueur2": {
		"pause": pygame.K_KP0,
		"up": pygame.K_UP,
		"left": pygame.K_LEFT,
		"down": pygame.K_DOWN,
		"right": pygame.K_RIGHT,
		"h_punch": pygame.K_KP1,
		"l_kick": pygame.K_KP2,
		"blocking": pygame.K_KP3,
		"victory1": pygame.K_KP4,
		"victory2": pygame.K_KP5,
	},
	"touche_joueur1": {
		"pause": pygame.K_g,
		"up": pygame.K_w,
		"left": pygame.K_a,
		"down": pygame.K_s,
		"right": pygame.K_d,
		"h_punch": pygame.K_t,
		"l_kick": pygame.K_y,
		"blocking": pygame.K_u,
		"victory1": pygame.K_5,
		"victory2": pygame.K_6,
	},

	"diminution": {
		"ken": 1,
		"ryu": 1,
		"cammy": 1,
		"t_hawk": 1.3,
	},

	"aide_joueur2": {
		str(pygame.K_KP0): "0",
		str(pygame.K_UP): "fleche haut",
		str(pygame.K_LEFT): "fleche gauche",
		str(pygame.K_DOWN): "fleche bas",
		str(pygame.K_RIGHT): "fleche droite",
		str(pygame.K_KP1): "1",
		str(pygame.K_KP2): "2",
		str(pygame.K_KP3): "3",
		str(pygame.K_KP4): "4",
		str(pygame.K_KP5): "5",
	},
	"aide_joueur1": {
		str(pygame.K_g): "g",
		str(pygame.K_w): "z",
		str(pygame.K_q): "q",
		str(pygame.K_s): "s",
		str(pygame.K_d): "d",
		str(pygame.K_t): "t",
		str(pygame.K_y): "y",
		str(pygame.K_u): "u",
		str(pygame.K_5): "(",
		str(pygame.K_6): "-",
	}
}