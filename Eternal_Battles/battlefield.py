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
		hand for each player
		field for each player # just for 1 player for now


	"""
	def __init__(self , player , group = None):
		"""
		This class is the battlefield, and it creates 4 maps where the cards will be played.
		It tells the card where it should be placed.
		:param player: The deck of that player (for now)
		:param group: a group to update in the scenes. It has to be a list or set.
		"""
		self.player_hand_map = Mapping((0, .75, 1, .25) , None , 'red' , 5)
		self.player_battlefield_map = Mapping((0, .5, 1, .25), None , 'white' , 5)
		player.set_battlefield(self)
		self.player = player
		if type(group) == list:
			group.append(self)
		elif type(group) == set:
			group.add(self)

	def draw(self , screen_to_draw):
		"""
		For now it draws rects for debugging the things.
		:param screen_to_draw:
		:return:
		"""
		self.player_hand_map.draw(screen_to_draw)
		self.player_battlefield_map.draw(screen_to_draw)

	def place_card_hand(self, card):
		"""
		Put a card in the hand rect.
		:param card: Card
		:return: None
		"""
		self.player_hand_map.place_card(card)


	def place_card_battle(self, card):
		"""
		Put a card in the battlefield.
		:param card: Card
		:return: None
		"""
		self.player_battlefield_map.place_card(card)


	def can_add_card_to_hand(self):
		"""
		check if there is enought space to add the card in the hand card.
		:return: Boolean, True it there is enought space.
		"""
		return self.player_hand_map.can_add_card()

	def can_add_card_to_battle(self):
		"""
		check if there is enought space to add the card in the hand card.
		:return: Boolean, True it there is enought space.
		"""
		return self.player_battlefield_map.can_add_card()

	def hand_to_field(self , card):
		"""
		Remove a card from the Hand rect and put it on the field
		:param card: Card
		:return: None
		"""
		self.player_hand_map.remove_card(card)
		self.player_battlefield_map.place_card(card)

	def check_card_in_hand(self, card):
		"""
		Check if the card in the Hand list.
		:param card: Card
		:return: Boolean, True if the card is in the hand.
		"""
		return self.player_hand_map.check_card(card)

	def check_card_in_field(self, card):
		"""
		Check if the card in the Field list.
		:param card: Card
		:return: Boolean, True if the card is in the field.
		"""
		return self.player_battlefield_map.check_card(card)

	def card_hit_on_field(self, card):
		"""
		Check if the center of the card in the Hand hit the Field rect.
		:param card: Card
		:return: Boolean, True if the card center hit the Field.
		"""
		return self.player_battlefield_map.check_hit_on_map(card)


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
			if not card.isalive():
				to_remove.append(card)

		for card in to_remove:
			self.card_list.remove(card)

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

