import re
import pygame
import random
import os
import cards
import text
import Winds
import colors
import fonts
import in_Game

##########################################################################################  HANDLE BUTTONS
 
class  Handle_buttons:
        
    Done = False
    buttons = []
    i=0
    def __init__ (self, bx, by, Button_W, Button_H):
        self.buttons.append(pygame.Rect(bx, by, Button_W, Button_H))
        
        
    def create_button(self, events, Place, Color, button_text, font, txtColor,Button_Rect, action= None):
        
        pygame.draw.rect(Place, Color, self.buttons[Button_Rect])
        txtW = text.txt_getter.get_txtW(button_text,font)
        txtH = text.txt_getter.get_txtH(button_text,font)
        text.txt_getter.draw_txt(button_text, font, txtColor, Place, self.buttons[Button_Rect].center[0]-txtW//2, self.buttons[Button_Rect].center[1]-txtH//2)
        posx,posy = pygame.mouse.get_pos()
        for event in events:
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and self.buttons[Button_Rect].collidepoint(posx, posy) and action!= None:
                action()
                
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and self.buttons[Button_Rect].collidepoint(posx, posy):
                posx, posy= pygame.mouse.get_pos()
                self.Done = True
                return True

        
#################################################################################################

def Draw_Background(Color):
    Winds.WIN.fill(Color)
    
card1 = cards.Cards()     

main_GoBack = Handle_buttons(30,500,200,50)     
Create_Deck = Handle_buttons(30,500,200,50)
Save_Deck = Handle_buttons(30,500,200,50)
Go_Back = Handle_buttons(500,500,200,50)

##########################################################################################  MAIN
def main():
    run = True 
    while run:     
        
        with open (card1.deck_name, "r") as game_Deck:
            x=game_Deck.read()
            text.txt_getter.draw_txt(str(x), fonts.font1, colors.BLACK, Winds.WIN, 300,300)
        for rect in card1.Deck:
            pygame.draw.rect(Winds.WIN, colors.BLACK, card1.CARDS_RECTS[rect])
        Winds.clock.tick(Winds.FPS)
        events = pygame.event.get()
        Draw_Background(colors.Light_Yellow) 
        if main_GoBack.create_button(events, Winds.WIN, colors.RED, "Go Back", fonts.font2, colors.BLACK,0):
            main_menu()
        
        for event in events:
            if event.type ==pygame.QUIT:
                exit()
                run = False

            
        pygame.display.update()
        
######################################



BUTTON_W = Winds.SCREEN_WIDTH-200
BUTTON_H = 100

def deck_menu():
    CARD1 = cards.Cards()
    CARD1.set_cards(0,4,4,4, "Soul Eater")
    CARD2 = cards.Cards()
    CARD2.set_cards(1,8,6,6, "Soul Healer")
    CARD3 =cards.Cards()
    CARD3.set_cards(2,6,8,2, "Jesus")
    CARD4 = cards.Cards()
    CARD4.set_cards(3,4,4,9, "Soul Eater")
    CARD5 = cards.Cards()
    CARD5.set_cards(4,8,6,4, "Soul Healer")
    CARD6 =cards.Cards()
    CARD6.set_cards(5,6,8,3, "Jesus")
    CARD7 = cards.Cards()
    CARD7.set_cards(6,4,4,7, "Soul Eater")
    CARD8 = cards.Cards()
    CARD8.set_cards(7,8,6,1, "Soul Healer")
    CARD9 =cards.Cards()
    CARD9.set_cards(8,6,8,6, "Jesus")
    CARD10 =cards.Cards()
    CARD10.set_cards(8,6,8,6, "Jesus")
    CARD11 =cards.Cards()
    CARD11.set_cards(8,6,8,6, "Jesus")
    button_delay = 0
    
    while True:
        Winds.clock.tick(Winds.FPS)
        Winds.DECK_WIN.fill(colors.Light_Yellow)
        events = pygame.event.get()
        text.txt_getter.draw_txt("Make Deck", fonts.font1, colors.BLACK, Winds.DECK_WIN, 30, 50)
        text.txt_getter.draw_txt("Left Click to zoom a card", fonts.font2, colors.BLACK, Winds.DECK_WIN, 30, 20)
        text.txt_getter.draw_txt("right click to unzoom a card", fonts.font2, colors.BLACK, Winds.DECK_WIN, 400, 20)
        if not card1.creating:
            if Create_Deck.create_button(events, Winds.DECK_WIN, colors.GOLD, "Create A Deck", fonts.font2, colors.BLACK, 1):
                card1.creating = True
                button_delay=0

        button_delay+=10
        if card1.creating and button_delay>=1000:
            if Save_Deck.create_button(events, Winds.DECK_WIN, colors.GOLD, "Save Deck", fonts.font2, colors.BLACK, 2):
                card1.creating = False
                card1.added.clear()
                button_delay=0
            DList_Border = pygame.Rect(Winds.SCREEN_WIDTH-238, 0, 230, Winds.SCREEN_HIGHT)
            pygame.draw.rect(Winds.DECK_WIN, colors.BLACK, DList_Border)
            DList_Rect = pygame.Rect(Winds.SCREEN_WIDTH-230, 0, 230, Winds.SCREEN_HIGHT)
            pygame.draw.rect(Winds.DECK_WIN, colors.GRAY, DList_Rect)
              
        if Go_Back.create_button(events, Winds.DECK_WIN, colors.RED, "Go Back", fonts.font2, colors.BLACK, 3):
            card1.CARDS_RECTS.clear()
            card1.HEALTH.clear()
            card1.DAMGE.clear()
            card1.COST.clear()
            card1.CARD_NAME.clear()
            card1.CARD_ID .clear()
            main_menu()
                
        card1.render_cards()
        card1.Touching(events)
        card1.set_deck(events)

        for event in events:
            if event.type ==pygame.QUIT:
                exit()             
              
        pygame.display.update()      
       
    
##########################################################################################  MAIN MENU

def main_menu():
    running = True
    
    while running:
        Winds.clock.tick(Winds.FPS)
        Winds.WIN.fill(colors.Light_Yellow)        
        text.txt_getter.draw_txt("Main Menu", fonts.font1, colors.BLACK, Winds.WIN, 30, 50)
        events = pygame.event.get()
        
        Start_Button = pygame.Rect(100, 150, BUTTON_W, BUTTON_H)
        Deck_Button = pygame.Rect(100, 300, BUTTON_W, BUTTON_H)
        pygame.draw.rect(Winds.WIN, colors.RED, Start_Button)
        pygame.draw.rect(Winds.WIN, colors.RED, Deck_Button)
        txtW, txtH= text.txt_getter.get_txtW("Start A Game", fonts.font1), text.txt_getter.get_txtH("Start A Game", fonts.font1)
        text.txt_getter.draw_txt("Start A Game", fonts.font1, colors.BLACK, Winds.WIN,Start_Button.center[0]-txtW//2, BUTTON_H+txtH)
        text.txt_getter.draw_txt("Create A Deck", fonts.font1, colors.BLACK, Winds.WIN,Deck_Button.center[0]-txtW//2, Deck_Button.center[1]-txtH//2)
        for event in events:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                posx, posy= pygame.mouse.get_pos()
                if Start_Button.collidepoint(posx, posy):
                    select_deck()
                if Deck_Button.collidepoint(posx, posy):
                    deck_menu()
            
        for event in events:
            if event.type ==pygame.QUIT:
                running = False
                pygame.quit()
                exit()
                
        pygame.display.update()
 
def select_deck():
    
    running = True
    decks_rects = []
    
    deckspath = 'Decks/'
    with os.scandir(deckspath) as entries:
        for index , entry in enumerate(entries):
            if entry.is_file():
                decks_rects.append(pygame.Rect)
                card1.Decks.append(entry.name)
                print(str(card1.Decks[index]))
                
    while running:
        events = pygame.event.get()
        Winds.clock.tick(Winds.FPS)
        Winds.SELECT_DECK.fill(colors.Light_Yellow)
        gapper = 0
        
        text.txt_getter.draw_txt("Select A Deck", fonts.font1, colors.BLACK, Winds.SELECT_DECK, 30, 50)
        for index,  rect in enumerate(decks_rects):
            rect = pygame.Rect(30+gapper, 120, 200, 100)
            gapper+=cards.CARD_WIDTH+120
            decks_rects[index] = rect
            pygame.draw.rect(Winds.SELECT_DECK, colors.GOLD, rect)
            txtW = text.txt_getter.get_txtW(str(card1.Decks[index]), fonts.font2)
            txtH = text.txt_getter.get_txtH(str(card1.Decks[index]), fonts.font2)
            text.txt_getter.draw_txt(str(card1.Decks[index]), fonts.font2, colors.BLACK, Winds.SELECT_DECK, rect.center[0]-txtW//2, rect.center[1]-txtH//2)

            for event in events:
                posx, posy = pygame.mouse.get_pos()
                if event.type==pygame.MOUSEBUTTONDOWN and rect.collidepoint(posx, posy):
                    rect_index = decks_rects.index(rect)
                    text.txt_getter.draw_txt(str(index), fonts.font1, colors.BLACK, Winds.SELECT_DECK, 300,300)
                    for card in card1.Decks:
                        deckpath = os.path.join('Decks/', card1.Decks[index])
                        with open (deckpath, 'r') as DeckFile:
                            card1.Deck = DeckFile.readlines()
                    game_screen()
        for event in events:
            if event.type ==pygame.QUIT:
                running = False
                pygame.quit()
                exit()
                
        pygame.display.update()
    
in_game = in_Game.BattleScreen()

def game_screen():
    in_game.game_deck = card1.Deck
    random.shuffle(in_game.game_deck)
    in_game.draw_card()
    in_game.draw_card()
    in_game.draw_card()
    in_game.draw_card()
    in_game.draw_card()

    
    while True:
        Winds.clock.tick(Winds.FPS)
        Winds.GAME_WIN.fill(colors.Light_Yellow)
        events = pygame.event.get()
    
        in_game.render_field()
        if not in_Game.mousebutton[0]:
            in_game.render_cards(events)
        in_game.play_card(events)
        in_game.draw_rects()
        for event in events:
            if event.type ==pygame.QUIT:
                pygame.quit()
                exit()
                
                
        pygame.display.update()
    
        
 
                 
main_menu()             
                
#if _name_ == "_main_menu_":