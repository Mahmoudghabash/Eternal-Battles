import enum
from tkinter import Button
import pygame as pg
import cards
import fonts
import colors
import Winds as win
import random

cards_getter = cards.Cards()
mousebutton = pg.mouse.get_pressed()

class BattleScreen:
    
    MAX_HAND_SIZE = 10
    field_Size = (1040,300)
    field_rect = pg.Rect
    events = pg.event.get()
    hand_cards = []
    game_deck = []
    game_deck = []
    cards_rects = []
    cards_inHand = 0
    DeckSize = 0
    clicked = False
    collide = False
    def __init__(self):
        self.field_rect= pg.Rect(win.SCREEN_WIDTH//2-self.field_Size[0]//2, win.SCREEN_HIGHT//2-self.field_Size[1]//2,self.field_Size[0], self.field_Size[1])
    
    def render_field(self):
        pg.draw.rect(win.GAME_WIN, colors.GOLD, self.field_rect)
    
    def draw_card(self):
        if self.cards_inHand <= self.MAX_HAND_SIZE:
            self.cards_rects.append(pg.Rect)
            self.DeckSize = len(self.game_deck)
            self.hand_cards.append(self.game_deck[self.DeckSize-1])
            self.game_deck.pop()
            self.cards_inHand+=1
            print(str(len(self.cards_rects)))
    
    def draw_rects(self):
        for rect in self.cards_rects:
            pg.draw.rect(win.GAME_WIN, colors.BLACK, rect)
    
    def play_card(self, events):
        global mousebutton
        clicking = False
        mousebutton = pg.mouse.get_pressed()
        for index, card in enumerate(self.cards_rects):
            posx,posy = pg.mouse.get_pos()
            self.collide = card.collidepoint(posx, posy)
            if mousebutton[0] and self.collide:
                self.collide = False
                print("clicked")
                self.clicked = True
            else:
                self.clicked = False
                
            if self.clicked and not clicking:
                x,y  = pg.mouse.get_pos()
                self.cards_rects[index].center= x,y
                clicking = True
                print(str(card))

    def render_cards(self, events):
        xGapper = 0
        
        for index, card in enumerate(self.cards_rects):
            card = pg.Rect(30+xGapper, 100, 75, 75)
            self.cards_rects[index] = card
            xGapper+=120



            
    
    
    