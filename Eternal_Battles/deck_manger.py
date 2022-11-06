from definitions import *
import pygame as pg
from animations import Animations
from pygame.sprite import Group
from pygame import Vector2
import random
from deck_and_cards_info import CARDS_STATS_DICT
import math
from deck_and_cards import *
from variables import *
import textbox
   
   
   
class set_deck(Animations):
    
    def __init__(self, groups):
        Animations.__init__(self,groups= groups)
        self.all_cards = list(CARDS_STATS_DICT.keys())
        self.deck_manger_cards = Group()
        self.area = (0.1,0.1)
        self.card_pos = (0.1,0.1)
        self.Xgapper = 0
        self.Ygapper = 0
        for card in self.all_cards:
            CardShowCase(card_id = card , groups = [self.deck_manger_cards] , area = self.area ,center = self.card_pos, color = 'dark green')
            self.Xgapper= self.area[0]+self.card_pos[0]+0.03
            self.card_pos = (self.Xgapper, 0.1)
            
        
    def click_down(self, event):
        for card in self.deck_manger_cards:
            card.click_down(event)
    
        
        
    def click_up(self,event):
        pass
    
    def draw(self, deck_manger_screen):
        for card in self.deck_manger_cards:
            card.draw(deck_manger_screen)

    def update(self):
        for card in self.deck_manger_cards:
            card.update()

       
            
            
            
            

            

            
        
    
    

                
   
   
   
