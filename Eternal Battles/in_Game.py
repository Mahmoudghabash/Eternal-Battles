import enum
import pygame as pg
import cards
import fonts
import colors
import Winds as win
import cards
import text
import os
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
    cards_rects = []
    cards_inHand = 0
    DeckSize = 0
    clicked = False
    Decks = []
    selected_deck = 0
    
    def __init__(self):
        
        random.shuffle(self.game_deck)
        self.field_rect= pg.Rect(win.SCREEN_WIDTH//2-self.field_Size[0]//2, win.SCREEN_HIGHT//2-self.field_Size[1]//2,self.field_Size[0], self.field_Size[1])
        deckspath = 'Decks/'
        with os.scandir(deckspath) as entries:
            for index , entry in enumerate(entries):
                if entry.is_file():
                    self.Decks.append(entry.name)
        deckpath = os.path.join('Decks/', self.Decks[self.selected_deck])
        with open (deckpath, "r") as game_Deck:
            self.game_deck = game_Deck.readlines()
            self.DeckSize = len(self.game_deck)
            
        for index, card in enumerate(self.game_deck):
            self.game_deck[index] = int(self.game_deck[index])
            
    def render_field(self):
        for index, card in enumerate(self.game_deck):
            text.txt_getter.draw_txt(f"{self.game_deck[index]}", fonts.font2, colors.RED, win.GAME_WIN, 200 , 200)
        pg.draw.rect(win.GAME_WIN, colors.GOLD, self.field_rect)
    
    def draw_card(self):
        if self.cards_inHand <= self.MAX_HAND_SIZE and self.DeckSize>0:
            self.cards_rects.append(pg.Rect)
            print(str(self.DeckSize))
            self.hand_cards.append(self.game_deck[self.DeckSize-1])
            self.game_deck.pop()
            self.DeckSize -=1
            self.cards_inHand+=1

    
    def draw_rects(self):
        for rect in self.cards_rects:
            pg.draw.rect(win.GAME_WIN, colors.BLACK, rect)
    
    def play_card(self, events):
        global mousebutton
        global theOne
        
            
        for index, card in enumerate(self.cards_rects):
            posx,posy = pg.mouse.get_pos()
            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and  card.collidepoint(posx, posy):
                    self.clicked = True
                    theOne= self.cards_rects.index(card)
                    #break
     
        if self.clicked:
            x,y  = pg.mouse.get_pos()
            self.cards_rects[theOne].center = x,y
            for event in events:
                if event.type == pg.MOUSEBUTTONUP:
                    self.clicked = False
                if event.type == pg.MOUSEBUTTONUP and self.cards_rects[theOne].y>self.field_rect.top and len(self.cards_rects)>0:
                    self.clicked = False
                    self.played = True
                    self.cards_rects.pop(theOne)

                        
                    
    def render_cards(self, events):
        xGapper = 0
        print(f"{len(self.game_deck)}")
        for index, card in enumerate(self.cards_rects):
            card = pg.Rect(30+xGapper, 100, 75, 75)
            text.txt_getter.draw_txt(f"{cards_getter.HEALTH[self.hand_cards[index]]}", fonts.font2, colors.RED, win.GAME_WIN, card.left , card.top)
            self.cards_rects[index] = card
            xGapper+=120



            
    
    
    