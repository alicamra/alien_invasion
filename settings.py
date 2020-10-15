class Settings:
	"""A class to store all settings for Alien Invasion"""
	def __init__(self):
		self.screen_width = 800
		self.screen_height = 500
		self.bg_color = (230, 230, 230)

		self.ship_speed = 0.5

		self.bullet_width = 10
		self.bullet_height = 15
		self.bullet_speed =0.7
		self.bullet_color = (160, 60, 60)
		self.bullet_limit = 10

		self.alien_speed = 0.5
		self.fleet_drop_speed = 10
		self.fleet_direction = 1

		self.ship_limit = 3