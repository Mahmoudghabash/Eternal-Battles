import fonts
import colors

class handle_txt:
    txt_Obj = fonts.font1
    
    def _init_(self):
        pass

    def draw_txt(self, text, font, color, surface, x, y):
        txt_Obj = font.render (text, True, color)
        self.txtW = txt_Obj.get_width()
        self.txtH = self.txt_Obj.get_height()
        txt_rect = txt_Obj.get_rect()
        txt_rect.topleft = (x, y)
        surface.blit(txt_Obj, txt_rect)
        
    def get_txtW(self, txt, font):
        toGetW = font.render(txt, False, colors.BLACK) 
        txtW= toGetW.get_width()
        return txtW
    
    def get_txtH(self, txt, font):
        toGetH = font.render(txt, False, colors.BLACK) 
        txtH= toGetH.get_height()
        return txtH
    
txt_getter = handle_txt()