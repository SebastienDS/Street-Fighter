import pygame


son = {
	"volume": {
		"volume": 0.5,
		"volume_up": pygame.K_KP_PLUS,
		"volume_down": pygame.K_KP_MINUS,
	},

	"background": {
		"opening_theme": "son/background/opening_theme.wav",
		"character_select": "son/background/character_select.wav",
		"ending_theme": "son/background/ending_theme.wav",
	},

	"map": {
		"Chun_li_stage": "son/map/Chun_li_stage.wav",
		"Guile_stage": "son/map/Guile_stage.wav",
		"Ken_stage": "son/map/Ken_stage.wav",
		"Ryu_stage": "son/map/Ryu_stage.wav",
	},

	"compteur": {
		"fight": "son/56H.wav",
		"compteur1": "son/60H.wav",
		"compteur2": "son/61H.wav",
		"compteur3": "son/62H.wav",
	},
}

def modif_volume(nbr):
	son["volume"]["volume"] += nbr
	pygame.mixer.music.set_volume(son["volume"]["volume"])