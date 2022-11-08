from tokenize import group
from deck_and_cards import Deck
import pygame as pg
from definitions import *
from scenes import Scene
from pygame.sprite import Group
from buttons import Button
from functools import partial
from deck_manger import set_deck
from battlefield import BattleField

pg.init()

############################### Windows of the game ###############################
# Every window is a class and have the objects it will use on that very class
# Create every object it will have in the create_objects() function
###################################################################################

''

############################### Main Window ###############################
# For now: 2 buttons, 1 for the deck selection and 1 for the battle
#
###################################################################################
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
        Button(text = 'Battle' , area = [.4 , .1] , center = [.5 , .3] ,
                                       on_click_up = partial(self.run_other , BattleWindow) , groups = self.buttons)

        Button(text = 'Decks' , area = [.4 , .1] , center = [.5 , .6] ,
                                    on_click_up = partial(self.run_other , DeckManager) , groups = self.buttons)


class BattleWindow(Scene):
    def __init__(self , **kwargs):
        # groups to use
        self.buttons = Group()
        self.players = Group()
        self.battlefields = set()

        # set the dictionary with the to do lists
        dict_to_do = {
            'update': [self.buttons , self.players] ,
            'move': [self.players] ,
            'draw': [self.buttons , self.players , self.battlefields] ,
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
        Button(text = 'Back' , area = [.1 , .1] , center = [.9 , .1] , on_click_up = partial(self.stop) ,
                          groups = self.buttons)

        deck = Deck([1 , 2 , 3 , 4] , area = [.2 , .2] , center = [.1 , .9] , groups = self.players)

        btf = BattleField(deck , self.battlefields)
        deck.set_battlefield(btf)
        

class DeckManager(Scene):
    def __init__(self , **kwargs):
        # groups to use
        self.buttons = Group()
        self.players = Group()

        # set the dictionary with the to do lists
        dict_to_do = {
            'update': [self.buttons , self.players] ,
            'move': [self.players] ,
            'draw': [self.buttons , self.players, buttons_group] ,
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
        Button(text = 'Back' , area = [.1 , .1] , center = [.9 , .1] , on_click_up = partial(self.stop) , groups = self.buttons)
        set_deck(groups=[self.buttons])


main_window = MainWindow().run()
battle_window = BattleWindow()
deck_manager_window = DeckManager()