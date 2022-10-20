import pygame as pg
import pygame as pg
import cards
import in_Game

in_game = in_Game.BattleScreen()

class minion(cards.Cards):
    
    events = pg.event.get()
    clicked = False

    keys = in_game.FriendsDict.keys()
    def __init__(self) -> None:
        super().__init__()
        
    def attack(self, events):
        global theOne
        global tempList
        for index, rect in enumerate(in_game.Friends_Rects):
            posx,posy = pg.mouse.get_pos()
            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and rect.collidepoint(posx, posy):
                    self.clicked = True
                    #print("clicked")
                    theOne= in_game.Friends_Rects.index(rect)
            
                    
        if self.clicked:
            x,y  = pg.mouse.get_pos()
            tempList = [x for i,x in enumerate(in_game.Friends_Rects) if i!=theOne]
            in_game.Friends_Rects[theOne].center = x,y
            #print(f"the one is: {theOne}")
            keys = in_game.FriendsDict.keys()
            keys = list(keys)
            for event in events:
                if event.type == pg.MOUSEBUTTONUP:
                    self.clicked = False
                if event.type == pg.MOUSEBUTTONUP and in_game.Friends_Rects[theOne].collidelist(in_game.Enemies_Rects)!=-1 and len(in_game.FriendsDict)>0:
                    target = in_game.Friends_Rects[theOne].collidelist(in_game.Enemies_Rects)
                    #print(f"target is: {theOne}")               
                    self.clicked = False
                    self.played = True
                    self.HEALTH[in_game.Enemies[target]] -= self.DAMGE[in_game.FriendsDict[keys[theOne]]]
                    in_game.f_HEALTH[theOne] -= self.DAMGE[in_game.Enemies[target]]
                    if in_game.f_HEALTH[theOne]<1:
                        in_game.Friends_Rects.pop(theOne)
                        in_game.FriendsDict.pop(keys[theOne])
                        in_game.f_HEALTH.pop(theOne)
                        in_game.Friends.pop(theOne)
                        #print(in_game.FriendsDict)
