import pickle
import time


class Replay:
	def __init__(self):
		self.data_player1 = {
			"posX": [],
			"posY": [],
			"vie": [],
			"direction": [],
			"position": [],
			"action": [],
			"last_direction": [],
			
		}
		self.data_player2 = {
			"posX": [],
			"posY": [],
			"vie": [],
			"direction": [],
			"position": [],
			"action": [],
			"last_direction": [],
		}


	def save_replay(self, name_file):
		data = [self.data_player1, self.data_player2]
		with open("Replay/" + name_file, "wb") as file:
			pickle.dump(data, file)


	def load_replay(self, name_file):
		with open("Replay/" + name_file, "rb") as file:
			data = pickle.load(file)
		self.data_player1 = data[0]
		self.data_player2 = data[1]


	def add_data(self, player1, player2):
		for player, data in [(player1, self.data_player1), (player2, self.data_player2)]:
			data["posX"].append(player.posX)
			data["posY"].append(player.posY)
			data["vie"].append(player.vie)
			data["direction"].append(player.direction)
			data["position"].append(player.position)
			data["action"].append(player.action)
			data["last_direction"].append(player.last_direction)


	def load_data(self, player1, player2):
		try:
			for player, data in [(player1, self.data_player1), (player2, self.data_player2)]:
				player.posX = data["posX"].pop(0)
				player.posY = data["posY"].pop(0)
				player.vie = data["vie"].pop(0)
				player.direction = data["direction"].pop(0)
				player.position = data["position"].pop(0)
				player.action = data["action"].pop(0)
				player.last_direction = data["last_direction"].pop(0)
				player.debut_direction = time.time()
				player.debut_position = time.time()
				player.debut_action = time.time()
		except:
			pass
