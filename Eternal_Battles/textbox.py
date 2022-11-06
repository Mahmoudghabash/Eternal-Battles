"""

"""
# from variables_and_definitions import *
from definitions import *
from variables import *
import pygame as pg
from pygame.sprite import Sprite

# Some Default Font
font_size = int(screen_rect.h / 1)
main_menu_font = pg.font.SysFont("arial" , font_size , False , False)


class TextBox(Sprite):
	""" this will work with short sentences, 1 line only.
	param text : string
	param rect : pg.Rect
	param font : pg.font.SysFont
	param font_color : pg.color
	param bg_color : pg.color
	"""

	def __init__(self , text='' , area = (1,1) , rect_to_be = None , relative_center = None , absolute_center = None , font = None , font_color = "white" , bg_color = "black" , groups = None):
		"""

		It takes a string, a area proportion , a pg.font,
		font color and a background color.


		:param text: str with the text to show
		:param area: list with 2 sizes from 0 to 1 to
		:param rect_to_be: pg.Rect object, where the proportion will be (1,1)
		:param font: pg.Font object
		:param font_color: pg.Color
		:param bg_color: pg.Color or None
		:param groups: list of groups to this object to be, if any.
		"""
		if groups is None:
			groups = []
		if type(groups) not in [set , list , tuple]:
			groups = list(groups)
		super().__init__(*groups)
		if font is None:
			font = main_menu_font
		if rect_to_be is None:
			rect_to_be = screen_rect
		self.text = text
		self.font = font
		self.font_color = font_color
		self.bg_color = bg_color
		self.rect_to_be = rect_to_be
		self.rect = pg.Rect((0,0) , calc_proportional_size(expected = area , max_area = [1,1] , max_rect = self.rect_to_be))

		if (relative_center is None) ^ (absolute_center is None):
			self.relative_center = relative_center
			if self.relative_center is not None:
				self.rect.center = calc_proportional_size(relative_center , max_area = (1,1) , max_rect = self.rect_to_be) + self.rect_to_be.topleft
			elif absolute_center is not None:
				self.rect.center = absolute_center

		self.max_size = self.rect.w*0.9
		self.line_w , self.line_h = self.font.size(str(text))
		self.cliked = False
		self.surface = None
		self.create_image()

	def create_image(self):
		new_surface = pg.Surface((self.line_w , self.line_h)).convert_alpha()
		new_surface.fill([0,0,0,0])
		txt = self.font.render(self.text , True , self.font_color , self.bg_color)
		new_surface.blit(txt , (0,0))
		new_surface = pg.transform.scale(new_surface , self.rect.size)
		self.surface = new_surface
		self.center_image()

	def center_image(self):
		"""
		Check if the image is centered in the rect to be
		:return:
		"""
		if self.relative_center is not None:
			self.rect.center = calc_proportional_size(self.relative_center , max_area = (1 , 1) ,
			                                          max_rect = self.rect_to_be) + self.rect_to_be.topleft


	def draw(self, screen_to_draw , angle = None):
		"""
		Draw the text box in the given surface.
		:param screen_to_draw: pg.Surface Object
		:return: None
		"""
		screen_to_draw.blit(self.surface , self.rect)

	def update(self):
		return

	def change_text(self , new_text = ''):
		"""
		Change the text of this box.
		:param new_text: a string object
		:return:
		"""
		self.text = new_text
		self.line_w , self.line_h = self.font.size(str(self.text))
		self.create_image()


	def resize(self , new_area , rect_to_be = None):
		"""
		Resizes the rect for the new area given,
		:param new_proportional_size:
		:param rect_to_be:
		:return:
		"""
		if rect_to_be is not None:
			self.rect_to_be = rect_to_be

		self.rect = self.rect = pg.Rect((0,0) , calc_proportional_size(expected = new_area , max_area = [1,1] ,
		                                                               max_rect = self.rect_to_be))
		self.create_image()
