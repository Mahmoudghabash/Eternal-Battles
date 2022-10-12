import cards


########  Cards get inited first in main.py in  main_menu()
cards_obj = cards.Cards()
def init_cards():
    if not cards_obj.global_cards_init:
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
        cards_obj.global_cards_init = True
