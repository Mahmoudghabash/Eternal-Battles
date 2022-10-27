from definitions import *
import pygame as pg
from animations import Animations
from pygame.sprite import Group
from pygame import Vector2
import random
from deck_and_cards_info import CARDS_STATS_DICT
import math

MAX_DISTANCE = calc_proportional_size(.1)
MAX_VELOCITY = 20


# there are 2 classes here, 1 for handle the deck and 1 for the cards
# The Deck class has a lot of list in it, and will call the functions on the cards.
# it has 3 decks, the main, the discard_deck , and the hand
# it has click_down and click_up
# update
# move
# shuffle the decks
# transfer a card to other place
# The Card class does the things for the cards that will appear on the screen.
# draw
# update
# click_down and click_up
# move
# kill
#######################
class Deck(Animations):
	"""
	things to do:
		init
		shuffle main deck - ok
		shuffle discard_deck deck - ok
		transfer cards from - ok
			main to discard_deck - ok
			select main to discard_deck - ok
			main to hand - ok
			select main to hand - ok
			discard_deck to hand - ok
			select discard_deck to hand - ok
			discard_deck to main - ok
			select discard_deck to main - ok
			hand to main - ok
			hand to discard_deck - ok
		update - ok
		draw - ok
		move - ok
	"""

	def __init__(self , card_indexes , **kwargs):

		# Creating the main decks
		self.card_indexes = card_indexes  # this is a list with all the cards it has. Each card is a index, where we will use to create the card.
		self.main_deck = card_indexes  # this is the main deck, a list of indexes, we use this to change the cards, take a card, return a card
		self.discard_deck = list()  # this is a list of indexes of the discarded cards, cards that are not in the hand nor the main deck
		self.hand_deck = Group()  # This is a pg.sprite.Group object. It is a set like obj, a container that will get the sprites. Use for the Animations class

		# create pg.Rect and images
		Animations.__init__(self , **kwargs)

	# shuffle things
	def shuffle_main_deck(self):
		"""
		This only shuffles the main deck
		:return: None
		"""
		random.shuffle(self.main_deck)

	def shuffle_discarded_deck(self):
		"""
		This only shuffles the discarded deck
		:return: None
		"""
		random.shuffle(self.discard_deck)

	# move cards in the different decks
	def main_to_hand(self , n_cards = 1):
		"""
		Take the n firsts cards from the main and add them to the hand.
		:param n_cards: int
		:return:
		"""
		for _ in range(n_cards):
			if len(self.main_deck) >= 1:
				self.create_card_in_hand(card_id = self.main_deck.pop(0))  # remove the first card of the deck and add it to the discarded list

			else:
				print('oh no, the deck is over!')  # lets check what to do later
				return

	def select_from_main_to_hand(self , cards_indexes = None):
		"""
		Take the card in the index position of the main and put it on the hand deck.
		:param cards_indexes: list of integers, with the cards' ids
		:return: None
		"""
		if cards_indexes is None:
			cards_indexes = []

		for card in cards_indexes:                      # move the cards
			self.main_deck.remove(card)                 # delete from here
			self.create_card_in_hand(card_id =card)     # append here

	def main_to_discarded(self , n_cards = 1):
		"""
		It takes a integer, and take that many cards from the main deck to discard deck.
		:param n_cards: int
		:return:
		"""
		for _ in range(n_cards):
			if len(self.main_deck) >= 1:
				self.discard_deck.append(self.main_deck.pop(0))  # remove the first card of the deck and add it to the discarded list

			else:
				print('oh no, the deck is over!')  # lets check what to do later
				return

	def select_from_main_to_discard(self , cards_indexes = None):
		"""
		Take the card in the index position of the main and put it on the discard deck.
		:param cards_indexes: list of integers, with the cards' ids.
		:return: None
		"""
		if cards_indexes is None:
			cards_indexes = []

		for card in cards_indexes:          # move the cards
			self.main_deck.remove(card)     # delete from here
			self.discard_deck.append(card)  # append here

	def discard_to_main(self , n_cards = 1):
		"""
		It takes a integer, and take that many cards from discard_deck to the main deck.
		:param n_cards: int
		:return:
		"""
		for _ in range(n_cards):
			if len(self.discard_deck) >= 1:
				self.main_deck.append(self.discard_deck.pop(-1))  # remove the first card of the deck and add it to the discarded list

			else:
				print('oh no, the deck is over!')  # lets check what to do later
				return

	def select_from_discard_to_main(self , cards_indexes = None):
		"""
		Take the card in the index position of the discard_deck and put it on the main deck.
		:param cards_indexes: list of integers, with the cards ids
		:return: None
		"""
		if cards_indexes is None:
			cards_indexes = []    # takes the last card added to the deck


		for card in cards_indexes:                      # move the cards
			self.discard_deck.remove(card)      # delete from here
			self.main_deck.append(card)         # append here

	def discard_to_hand(self , n_cards = 1):
		"""
		Take the n firsts cards from the main and add them to the hand.
		:param n_cards: int
		:return:
		"""
		for _ in range(n_cards):
			if len(self.discard_deck) >= 1:
				self.create_card_in_hand(card_id = self.discard_deck.pop(-1))  # remove the last card of the deck and add it to the hand.

			else:
				print('oh no, the deck is over!')  # lets check what to do later
				return

	def select_from_discard_to_hand(self , cards_indexes = None):
		"""
		Take the card in the index position of the discard_deck and put it on the hand deck.
		:param cards_indexes: list of integers, with the cards' ids
		:return: None
		"""
		if cards_indexes is None:
			cards_indexes = []

		for card in cards_indexes:                      # move the cards
			self.discard_deck.remove(card)              # delete from here
			self.create_card_in_hand(card_id =card)     # append here

	def hand_to_main(self , card):
		card_id = card.get_id()             # select the id of the card
		self.main_deck.append(card_id)      # put the card in the end
		card.kill()                         # delete the card from the groups

	def hand_to_discard(self , card):
		card_id = card.get_id()             # select the id of the card
		self.discard_deck.append(card_id)   # put the card in the end
		card.kill()                         # delete the card from the groups


	# helpers
	def create_card_in_hand(self , card_id):
		"""
		This creates the cards in the hand, the cards that will be shown in the screen
		:param card_id: index for the CARDS_STATS_DICT and CARDS_IMAGES_DICT
		:return: None
		"""
		Card(card_id = card_id , deck = self , groups = [self.hand_deck] ,
		     area = self.get_area() , color = 'dark green')

	def get_hand_deck(self):
		return self.hand_deck

	# handlers
	def update(self , **kwargs):
		"""
		update the images of the deck and all the cards in the hand deck
		:param kwargs: for the Animations.update()
		:return:
		"""
		Animations.update(self)

		for card in self.hand_deck:
			card.update()

	def draw(self , screen_to_draw):
		"""
		draw itself on the screen_to_draw, then draw all the cards in the deck hand
		:param screen_to_draw: pg.Display
		:return:
		"""
		# draw its image or rect
		Animations.draw(self , screen_to_draw = screen_to_draw)

		# draw cards
		for card in self.hand_deck:
			card.draw(screen_to_draw)

	def move(self):
		"""
		move the cards in self.hand_deck around
		:return:
		"""
		for card in self.hand_deck:
			card.move()

	def click_down(self , event):
		"""
		runs through all the cards in self.hand_deck
		:param event: pg.MOUSEBUTTONDOWN event
		:return:
		"""
		if self.rect.collidepoint(event.pos):
			self.main_to_hand()
		for card in self.hand_deck:
			card.click_down(event)

	def click_up(self , event):
		"""
		Call the method click_up() for all the cards in the hand
		:param event: pg.MOUSEBUTTONUP event
		:return:
		"""
		for card in self.hand_deck:
			card.click_up(event)



#######################
class Card(Animations):
	"""
	Things to do:
		init - ok
		click_up
		click_down
		update - ok (animation)
		draw
		move
		kill

	"""

	def __init__(self , card_id , deck , **kwargs):

		# set the card Id for itself to creat its stats
		self.card_id = card_id

		# create rect and images, if any
		Animations.__init__(self , image_name = self.card_id , **kwargs)

		# set its values and things
		self.cost = CARDS_STATS_DICT.get('cost' ,
		                                 2)  # check in the dict for the keyword cost and take the value there. If it don't find, return the second value
		self.health = CARDS_STATS_DICT.get('health' , 10)
		self.damage = CARDS_STATS_DICT.get('damage' , 2)
		self.card_name = CARDS_STATS_DICT.get('card_name' , 'Test')
		self.deck = deck

		# for handle in game things
		self.fixed_position = None  # this is a place (x , y) where the card will be 'attracted' to, in case it is played
		self.velocity = Vector2([0 , 0])
		self.acceleration = Vector2([0 , 0])
		self.clicked = False

	# handlers and updates
	def update(self , **kwargs):
		"""
		updates the things for the card
		:param kwargs: args for the Animations.update()
		:return:
		"""
		self.velocity *= 0.9

		if not self.clicked:
			if self.fixed_position is None:
				self.update_not_played()
			else:
				self.update_played()

		# set the acceleration 0 for the next cycle
		self.acceleration *= 0

		Animations.update(self)

	def update_not_played(self):
		"""
		Calculates the forces to move itself, if hitting other cards.
		:return:
		"""

		# calc the force and angle for each card it is touching
		hand_cards = self.deck.get_hand_deck()  # get a pg.Group with all the cards in the rand

		for card in hand_cards:
			if card != self:  # not checking with itself
				if self.rect.colliderect(card):  # if card collide
					if self.rect.center == card.rect.center:  # move a little bit if 2 rects are the same possition
						self.rect.move_ip(int(random.random() * 10) , 0)
					ang = get_ang(self.rect.center , card.rect.center)  # calcs the angule
					self.acceleration += pg.math.Vector2(-math.cos(ang) * FORCE_TO_CARDS , -math.sin(
						ang) * FORCE_TO_CARDS)  # sums all the vector acc with the new vector from the force for the angule

		# calcs the new velocity
		self.velocity += self.acceleration

	def update_played(self):
		"""
		It calcules the force for the card to get back for the position, for it to
		return in a fluid manner to the fixed position.
		:return: None
		"""
		dist = self.fixed_position.distance_to(self.rect.center)  # calcs the distance
		proportion = min([dist / MAX_DISTANCE , 1])  # set a proportion so that higher the distance, higher velocity
		angle = get_ang(self.rect.center ,
		                self.fixed_position)  # calculates the angle between the rect and the fixed position
		self.acceleration += [math.cos(angle) , math.sin(angle)]  # increase the acceleration to the position
		self.acceleration *= proportion  # multiply by the proportion, to get the velocity, but not a infinity velocity
		self.acceleration *= MAX_VELOCITY  # increase the velocity for it to move

	def move(self):
		"""
		Move the card around
		:return:
		"""
		if self.clicked:
			self.rect.move_ip(pg.mouse.get_rel())
		else:
			self.rect.move_ip(self.velocity)
		self.rect.clamp_ip(self.rect_to_be)

	def click_down(self , event):
		self.clicked = self.rect.collidepoint(event.pos)
		return self.clicked

	def click_up(self , event):
		self.clicked = False

	# setters and getters
	def set_position(self , pos = None):
		"""
		Sets a fixed position for the card, or delete it if the param pos is None.
		:param pos: list (x , y) or None
		:return: None
		"""
		if pos is None:
			self.fixed_position = None
		else:
			self.fixed_position = Vector2(pos)

	def get_id(self):
		return self.card_id

	def get_name(self):
		return self.card_name

	def get_cost(self):
		return self.cost

	def get_hp(self):
		return self.health

	def get_damage(self):
		return self.damage

	def change_hp(self , value = 1):
		self.health += value