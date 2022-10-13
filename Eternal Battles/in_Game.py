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
    Decks = []
    Friends = []
    Friends_Rects = []
    Enemies= []
    DeckSize = 0
    selected_deck = 0
    clicked = False
    
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
        pg.draw.rect(win.GAME_WIN, colors.GOLD, self.field_rect)
    
    def draw_card(self):
        if len(self.hand_cards) <= self.MAX_HAND_SIZE and self.DeckSize>0:
            self.cards_rects.append(pg.Rect)
            print(str(self.DeckSize))
            self.hand_cards.append(self.game_deck[self.DeckSize-1])
            self.game_deck.pop()
            self.DeckSize -=1

    
    def draw_rects(self):
        for index, rect in enumerate(self.cards_rects):
            pg.draw.rect(win.GAME_WIN, colors.BLACK, rect)
            text.txt_getter.draw_txt(f"{cards_getter.HEALTH[self.hand_cards[index]]}", fonts.font2, colors.RED, win.GAME_WIN, rect.left , rect.top)

        xGapper = 30
        for index, Friendr in enumerate(self.Friends_Rects):
            Friendr = pg.Rect(30+xGapper, self.field_rect.bottom-cards.CARD_HIGHT, 75, 75)
            self.Friends_Rects[index] = Friendr
            pg.draw.rect(win.GAME_WIN, colors.BLACK, Friendr)
            text.txt_getter.draw_txt(f"{cards_getter.HEALTH[self.Friends[index]]}", fonts.font2, colors.RED, win.GAME_WIN, Friendr.left , Friendr.top)
            xGapper+=cards.CARD_WIDTH
            
            
            
            
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
                if event.type == pg.MOUSEBUTTONUP and self.cards_rects[theOne].y>self.field_rect.top and len(self.hand_cards)>0:
                    self.clicked = False
                    self.played = True
                    self.Friends.append(self.hand_cards[theOne])
                    self.Friends_Rects.append(pg.Rect)
                    self.cards_rects.pop(theOne)
                    self.hand_cards.pop(theOne)
                    
         
    def render_cards(self, events):
        xGapper = 0
        for index, card in enumerate(self.cards_rects):
            card = pg.Rect(30+xGapper, cards.CARD_HIGHT//2+self.field_rect.bottom, 75, 75)
            self.cards_rects[index] = card
            xGapper+=30+cards.CARD_WIDTH
   
