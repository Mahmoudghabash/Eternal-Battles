"""
This file contains the several windows that will be on the game
For name some:
	main window
	main game
	pause
	configure windows
"""

"""
Example of dictionary to use in the scene:

exemple_dict = {
		'update': [],
		'move': [],
		'draw': [],
		'click_down': [],
		'click_up': [],
		'key_down': [],
		'key_up': [],
		'multi_gesture': [],
		'finger_down': [],
		'finger_up': [],
		'finger_motion' : []
		}

"""


import pygame as pg
from scenes import Scene
from definitions import *
from buttons import Button
from functools import partial
from pygame.sprite import Group

pg.init()



########################################################################################
                                 #Main Window#
########################################################################################
class MainWindow(Scene):
	def __init__(self):
		# create the groups

		self.buttons = Group()

		dict_to_do = {
			'update': [self.buttons] ,
			'draw': [self.buttons] ,
			'click_down': [self.buttons] ,
		}
		Scene.__init__(self , screen_to_draw = screen , dict_to_do = dict_to_do , background = "light blue" , fps = 45)

	def create_objects(self):
		Button(area = (.6 , .2) , center = (.5 , .3) , rect_to_be = screen_rect ,  image = None , text = 'Start' ,
		       on_click_down = None , on_click_up = partial(self.start_game) , colors = None , groups = [self.buttons])

		Button(area = (.6 , .2) , center = (.5 , .7) , rect_to_be = screen_rect , image = None , text = 'Configs',
		       on_click_down = None , on_click_up = partial(self.start_game) , colors = None , groups = [self.buttons])

	def start_game(self):
		MainGameWindow().run()


########################################################################################
                                  # Main Game#
########################################################################################

class MainGameWindow(Scene):
	def __init__(self):
		# create the groups

		self.buttons = Group()
		self.player = Group()
		self.blocks = Group()

		dict_to_do = {
		'update': [self.buttons],
		'move': [],
		'draw': [self.buttons],
		'click_down': [self.buttons],
		'click_up': [],
		'key_down': [],
		'key_up': [],
		'multi_gesture': [],
		'finger_down': [],
		'finger_up': [],
		'finger_motion' : []
		}
		Scene.__init__(self , screen_to_draw = screen , dict_to_do = dict_to_do , background = "dark blue" , fps = 45)

	def create_objects(self):
		Button(area = (.6 , .2) , center = (.5 , .4) , rect_to_be = screen_rect , image = None , text = 'Start' ,
		       on_click_down = partial(self.start_game) , on_click_up = None , colors = None , groups = self.buttons)

	def start_game(self):
		MainWindow().run()


########################################################################################
                                  # Main Game#
########################################################################################

class ConfigurationWindow(Scene):
	def __init__(self):
		# create the groups

		self.buttons = Group()
		self.player = Group()
		self.blocks = Group()

		dict_to_do = {
		'update': [self.buttons],
		'move': [],
		'draw': [self.buttons],
		'click_down': [self.buttons],
		'click_up': [],
		'key_down': [],
		'key_up': [],
		'multi_gesture': [],
		'finger_down': [],
		'finger_up': [],
		'finger_motion' : []
		}
		Scene.__init__(self , screen_to_draw = screen , dict_to_do = dict_to_do , background = "dark blue" , fps = 45)

	def create_objects(self):
		Button(area = (.6 , .2) , center = (.5 , .4) , rect_to_be = screen_rect , image = None , text = 'Start' ,
		       on_click_down = None , on_click_up = None , colors = None , groups = self.buttons)

	def start_game(self):
		MainWindow().run()


MainWindow().run()