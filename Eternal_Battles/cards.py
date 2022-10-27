import pygame
import os
import Winds
import text
import colors
import fonts
import Winds

CARD_WIDTH, CARD_HIGHT = 100, 100
MAX_DECK_SIZE = 5

DeckText = ""
active = False
Color = colors.RED

    
        
class Cards:
    CARDS = []
    COST = []
    HEALTH = []
    DAMGE = []
    CARD_ID= []
    CARD_NAME = []
    CARDS_RECTS = []
    Deck = []
    Decks = []
    Deck_Size = 0

    global_cards_init = False
    cardsInited= False
    clicked = False
    index=0
    Decks_Num = 0
    added = []
    DoCreate = False
    creating =False
    deck_name = ''
    i=0
    
    def _init_ (self):
        pass
    
########################################################  SET CARDS

    def set_cards(self, id, c, h, d, n):
        self.CARD_ID.append(id)
        self.COST.append(c)
        self.HEALTH.append(h)
        self.DAMGE.append(d)
        self.CARD_NAME.append(n)
        self.CARDS_RECTS.append(pygame.Rect)
        
########################################################  DRAW CARDS
  
    def render_cards(self):
        i = 0
        CARDS_GAP = 30
        y, z =0,1
        yPos = 120
        for rect in self.CARDS_RECTS:
            if i+30>Winds.SCREEN_WIDTH-CARD_WIDTH-245:
                yPos+= CARD_HIGHT+30
                i=0
            rect= pygame.Rect(30+i, yPos, CARD_WIDTH, CARD_HIGHT)
            rect_border= pygame.Rect(25+i, yPos-5, CARD_WIDTH+10, CARD_HIGHT+10)
            self.CARDS_RECTS[y]= pygame.Rect(30+i, yPos, CARD_WIDTH, CARD_HIGHT)
            if not self.cardsInited:
                pygame.draw.rect(Winds.DECK_WIN, colors.BLACK, rect_border)  
                pygame.draw.rect(Winds.DECK_WIN, colors.GOLD, rect)
                
                for c in self.COST[y:z]:
                    text.txt_getter.draw_txt(str(c), fonts.font2, colors.Light_Blue, Winds.DECK_WIN, rect.left, rect.top )
                for h in self.HEALTH[y:z]:
                    txtH= text.txt_getter.get_txtW(str(h), fonts.font2)
                    text.txt_getter.draw_txt(str(h), fonts.font2, colors.RED, Winds.DECK_WIN, rect.right-text.txt_getter.txtW, rect.bottom-txtH-8)
                for d in self.DAMGE[y:z]:
                    text.txt_getter.draw_txt(str(d), fonts.font2, colors.BLACK, Winds.DECK_WIN, rect.left, rect.bottom-txtH-8)
                y+=1
                z+=1
            i+=CARD_WIDTH+CARDS_GAP

########################################################  TOUCHING   
         
    def Touching(self, events): 
        for index, (rect, health) in enumerate(zip(self.CARDS_RECTS, self.HEALTH)):
            for event in events:
                POSx ,POSy= pygame.mouse.get_pos()
                if event.type== pygame.MOUSEBUTTONDOWN and event.button== 1 and rect.collidepoint(POSx ,POSy):
                    self.clicked = True
                    self.index = self.CARDS_RECTS.index(rect)
                    break
                                   
        if self.clicked:
            rect = pygame.Rect.move(rect , Winds.SCREEN_WIDTH//2-rect.x//2,Winds.SCREEN_HIGHT//2-rect.y//2)
            rect = pygame.Rect.inflate(rect, 250, 250)
            pygame.draw.rect(Winds.DECK_WIN, colors.BLACK, rect)
            txtW= text.txt_getter.get_txtW(str(self.HEALTH[self.index]), fonts.font2)
            text.txt_getter.draw_txt(str(self.index), fonts.font2, colors.RED, Winds.DECK_WIN, 100,300)
            text.txt_getter.draw_txt(str(self.DAMGE[self.index]), fonts.font2, colors.GOLD, Winds.DECK_WIN, rect.left, rect.top)
            text.txt_getter.draw_txt(str(self.HEALTH[self.index]), fonts.font2, colors.RED, Winds.DECK_WIN, rect.right-txtW,rect.y)
            for event in events:
                POSx ,POSy= pygame.mouse.get_pos()
                if event.type== pygame.MOUSEBUTTONDOWN and event.button== 3:
                    self.clicked = False
            
        for event in events:
            if event.type ==pygame.QUIT:
                exit()
                          
########################################################  SET DECK

    def set_deck(self, events):
        

        if self.creating:
            self.get_Deck_Name(events)
            for index, rect in enumerate(self.CARDS_RECTS):
                self.added.append(False)
                for event in events:
                    POSx ,POSy= pygame.mouse.get_pos()
                    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and rect.collidepoint(POSx, POSy) and self.Deck_Size<=MAX_DECK_SIZE:
                        if not self.added[index]:
                            self.added[index]= True
                            self.Deck.append(self.CARDS_RECTS.index(rect))
                            self.Deck_Size+=1
                            print(str(self.Deck_Size))
                            deckpath = os.path.join('Decks/', self.deck_name)
                            with open (deckpath, "a") as file_Obj:
                                file_Obj.write(str(self.CARDS_RECTS.index(rect))+ "\n")    
                if self.added[index]==True:
                    pygame.draw.rect(Winds.DECK_WIN, colors.BLACK, rect)

    def get_Deck_Name(self, events):
        
        global DeckText
        global Color
        global active
        
        text_rect = pygame.Rect(300, 600, 400, 50)
        pygame.draw.rect(Winds.DECK_WIN, Color, text_rect)

        if not active:
            txtW = text.txt_getter.get_txtW("Enter The Deck Name", fonts.font2)
            txtH = text.txt_getter.get_txtH("Enter The Deck Name", fonts.font2)
            text.txt_getter.draw_txt("Enter The Deck Name", fonts.font2, colors.BLACK, Winds.DECK_WIN, text_rect.center[0]-txtW//2, text_rect[1]+txtH//2)
        
        for event in events:
            POSx ,POSy= pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and text_rect.collidepoint(POSx, POSy):
                Color = colors.GOLD
                active = True
                DeckText = ""
            elif event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN and len(DeckText)>0:
                    self.deck_name = DeckText
                    self.deck_name+=".txt"
                    active = False
                    Color = colors.RED
                    print(DeckText)
                elif event.key == pygame.K_BACKSPACE:
                    DeckText =  DeckText[:-1]
                else:
                    if len(DeckText)<12:
                        DeckText += event.unicode
        text.txt_getter.draw_txt(DeckText, fonts.font2, colors.BLACK, Winds.DECK_WIN, 400, 400)
        text.txt_getter.draw_txt(self.deck_name, fonts.font2, colors.BLACK, Winds.DECK_WIN, 400, 400)
