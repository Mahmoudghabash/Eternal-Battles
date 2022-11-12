"""
This is a container like class,  to call the players, set the possible positions for the cards, manage turns,
attacks and comunication between players.
"""
import random

from definitions import *
import pygame as pg
import random


class BattleField:
	"""
	heve 4 rects:
		hand for each player1
		field for each player1 # just for 1 player1 for now


	"""
	def __init__(self , group = None):
		"""
		This class is the battlefield, and it creates 4 maps where the cards will be played.
		It tells the card where it should be placed.
		:param player1: The deck of that player1 (for now)
		:param group: a group to update in the scenes. It has to be a list or set.
		"""
		self.player1_hand_map = Mapping((0, .75, 1, .25) , None , 'red' , 5)
		self.player1_battlefield_map = Mapping((0, .5, 1, .25) , None , 'white' , 5)
		self.player2_hand_map = Mapping((0 , .0 , 1 , .25) , None , 'red' , 5)
		self.player2_battlefield_map = Mapping((0 , .25 , 1 , .25) , None , 'white' , 5)
		self.player1 = None
		self.player2 = None
		if type(group) == list:
			group.append(self)
		elif type(group) == set:
			group.add(self)

	def set_players(self , player1=None , player2=None):
		if player1 is not None:
			self.player1 = player1
			self.player1.set_battlefield(self)
			self.player1.set_position(calc_proportional_size([.1 , .9]))
		if player2 is not None:
			self.player2 = player2
			self.player2.set_battlefield(self)
			self.player2.set_position(calc_proportional_size([.1 , .1]))

	def draw(self , screen_to_draw):
		"""
		For now it draws rects for debugging the things.
		:param screen_to_draw:
		:return:
		"""
		self.player1_hand_map.draw(screen_to_draw)
		self.player1_battlefield_map.draw(screen_to_draw)
		self.player2_hand_map.draw(screen_to_draw)
		self.player2_battlefield_map.draw(screen_to_draw)

	def place_card_hand(self, deck , card):
		"""
		Put a card in the hand rect.
		:param card: Card
		:return: None
		"""
		if deck is self.player1:
			hand_map = self.player1_hand_map
		else:
			hand_map = self.player2_hand_map
		hand_map.place_card(card)

	def place_card_battle(self, deck , card):
		"""
		Put a card in the battlefield.
		:param card: Card
		:return: None
		"""
		if deck is self.player1:
			hand_map = self.player1_battlefield_map
		else:
			hand_map = self.player2_battlefield_map
		hand_map.place_card(card)

	def can_add_card_to_hand(self, deck):
		"""
		check if there is enought space to add the card in the hand card.
		:return: Boolean, True it there is enought space.
		"""
		if deck is self.player1:
			hand_map = self.player1_hand_map
		else:
			hand_map = self.player2_hand_map
		return hand_map.can_add_card()

	def can_add_card_to_battle(self , deck):
		"""
		check if there is enought space to add the card in the hand card.
		:return: Boolean, True it there is enought space.
		"""
		if deck is self.player1:
			hand_map = self.player1_battlefield_map
		else:
			hand_map = self.player2_battlefield_map
		return hand_map.can_add_card()

	def hand_to_field(self , deck , card):
		"""
		Remove a card from the Hand rect and put it on the field
		:param card: Card
		:return: None
		"""
		if deck is self.player1:
			hand_map = self.player1_hand_map
			battlefield = self.player1_battlefield_map
		else:
			hand_map = self.player2_hand_map
			battlefield = self.player2_battlefield_map
		hand_map.remove_card(card)
		battlefield.place_card(card)

	def check_card_in_field(self, deck , card):
		"""
		Check if the card in the Field list.
		:param card: Card
		:return: Boolean, True if the card is in the field.
		"""
		if deck is self.player1:
			hand_map = self.player1_battlefield_map
		else:
			hand_map = self.player2_battlefield_map
		return hand_map.check_card(card)

	def card_hit_on_field(self, deck , card):
		"""
		Check if the center of the card in the Hand hit the Field rect.
		:param deck: Deck
		:param card: Card
		:return: Boolean, True if the card center hit the Field.
		"""
		if deck is self.player1:
			hand_map = self.player1_battlefield_map
		else:
			hand_map = self.player2_battlefield_map
		return hand_map.check_hit_on_map(card)

	def get_enemies(self , deck):
		if deck is self.player1:
			return self.player2.get_played_cards()
		elif deck is self.player2:
			return self.player1.get_played_cards()

	def get_enemy_rect(self, deck):
		if deck is self.player1:
			return self.player2_battlefield_map.get_rect()
		else:
			return self.player1_battlefield_map.get_rect()

	def remove_cards(self):
		self.player1_hand_map.update_cards()
		self.player1_battlefield_map.update_cards()
		self.player2_hand_map.update_cards()
		self.player2_battlefield_map.update_cards()

class Mapping:
	def __init__(self , proportional_size = None , rect_to_be = None , color = 'red' , max_spaces = 5 , player = None):
		"""
		Create a Container that handle the positions of the cards.
		:param proportional_size: the proportional_size of the rect
		:param rect_to_be: pg.Rect
		:param color: pg.Color
		:param max_spaces: int, maximum number of cards possible in this container.
		:param player: for now, the Deck
		"""
		self.rect = pg.Rect(calc_proportional_size(proportional_size , max_rect = rect_to_be))
		self.card_list = list()
		self.color = color
		self.max_spaces = max_spaces
		self.player = player

######### Update Things
	def update(self):
		"""
		Update itself when a card is placed or removed
		:return: None
		"""

		# check the number of cards, check if killed
		self.update_cards()

		# update the positions for the cards in the game
		self.update_positions()

	def update_cards(self):
		"""
		Remove the cards that aren't in any group
		:return: None
		"""
		to_remove = []
		for card in self.card_list:
			print(card)
			if not card.alive():
				to_remove.append(card)
		if to_remove:
			for card in to_remove:
				self.card_list.remove(card)
			self.update_positions()

	def update_positions(self):
		"""
		check the positions for the cards in the list.
		:return:
		"""
		size = 1 / (len(self.card_list) + 1)
		for idx , card in enumerate(self.card_list):
			pos_x = (idx + 1) * size
			card.set_position(calc_proportional_size([pos_x , .5] , max_rect = self.rect) + self.rect.topleft)

######### Manage Cards
	def place_card(self , card):
		"""
		Place a card in the list for this container, then update the positions.
		:param card: Card
		:return: None
		"""
		self.card_list.append(card)
		self.update_positions()

	def remove_card(self, card):
		"""
		Removes a card from this container, then update the positions.
		:param card: Card
		:return: None
		"""
		self.card_list.remove(card)
		self.update_positions()

	def can_add_card(self):
		"""
		Check if the container has some space yet.
		:return: Boolean, True if there is space
		"""
		return self.max_spaces > len(self.card_list)

######## Handlers
	def draw(self , screen_to_draw):
		"""
		for debugging, draws a rect for the thing.
		:param screen_to_draw: pg.Surface
		:return: None
		"""
		pg.draw.rect(screen_to_draw , self.color , self.rect , 4 , 2)

	def check_card(self, card):
		"""
		Check if the card is in this Container
		:param card: Card
		:return: boolean, True if the card is in this Container.
		"""
		return card in self.card_list

	def check_hit_on_map(self, card):
		"""

		:param card:
		:return:
		"""
		return self.rect.collidepoint(card.rect.center)

######## Seters and Getters
	def get_rect(self):
		return self.rect

