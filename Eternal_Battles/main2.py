from deck_and_cards import Deck
import pygame as pg
from definitions import *
from scenes import Scene
from pygame.sprite import Group
from buttons import Button
from functools import partial

pg.init()

class MainWindow(Scene):
	def __init__(self , **kwargs):

		# groups to use
		self.buttons = Group()

		# set the dictionary with the to do lists
		dict_to_do = {
			'update': [self.buttons] ,
			'move': [] ,
			'draw': [self.buttons] ,
			'click_down': [self.buttons] ,
			'click_up': [] ,
			'key_down': [] ,
			'key_up': [] ,
			'multi_gesture': [] ,
			'finger_down': [] ,
			'finger_up': [] ,
			'finger_motion': []
		}

		Scene.__init__(self , screen_to_draw = screen , dict_to_do = dict_to_do , **kwargs)


	def create_objects(self):
		# create the buttons
		start_main_battle_btn = Button(txt = 'Battle' , area = [.4 , .1] , center = [.5 , .3] ,
		                               on_click_up = partial(self.run_other , BattleWindow) , groups = self.buttons)

		deck_selection_btn = Button(txt = 'Decks' , area = [.4 , .1] , center = [.5 , .6] ,
		                            on_click_up = partial(self.run_other , BattleWindow) , groups = self.buttons)


class BattleWindow(Scene):
	def __init__(self , **kwargs):
		# groups to use
		self.buttons = Group()
		self.players = Group()

		# set the dictionary with the to do lists
		dict_to_do = {
			'update': [self.buttons , self.players] ,
			'move': [self.players] ,
			'draw': [self.buttons , self.players] ,
			'click_down': [self.buttons , self.players] ,
			'click_up': [] ,
			'key_down': [] ,
			'key_up': [] ,
			'multi_gesture': [] ,
			'finger_down': [] ,
			'finger_up': [] ,
			'finger_motion': []
		}

		Scene.__init__(self , screen_to_draw = screen , dict_to_do = dict_to_do , **kwargs)



	def create_objects(self):
		# create the buttons
		back_btn = Button(txt = 'Back' , area = [.1 , .1] , center = [.9 , .1] , on_click_up = partial(self.stop) ,
		                  groups = self.buttons)

		# create_objects
		deck = Deck([1 , 1 , 1 , 1 , 2 , 2 , 2 , 2] , area = [.2 , .2] , center = [.5 , .8] , groups = self.players)
		deck.shuffle_main_deck()
		deck.main_to_hand(4)



MainWindow().run()