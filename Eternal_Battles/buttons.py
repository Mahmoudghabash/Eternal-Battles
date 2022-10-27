"""
Buttons class
This class makes buttons_group,
do the click down and up stuffs,
change color when roovered
stuff in general
"""
from variables import *
from definitions import *
from animations import Animations


class Button(Animations):
	def __init__(self , area , center , rect_to_be = None , image: str = None , txt = None , on_click_down = None ,
	             on_click_up = None , colors = None , groups = None):
		"""
		It creates a rect in the screen, and does a action when interacted. If calls update, when hoovered it slightly change the color.
		:param relative_size: a list or tuple with float numbers from 0 to 1.0
		:param action: str with the action to do.
		:param image: str with path to the image
		:param txt: str with what should it show
		:param action_on_click: bool
		:param colors: list of pg.color
		"""
		if colors is None:
			colors = ['orange' , 'orange4' , 'orange2']
		Animations.__init__(self , area = area , rect_to_be = rect_to_be , image_name = image , center = center ,
		                    groups = groups)
		self.on_click_down = on_click_down
		self.image = image
		self.clicked = False
		self.on_click_up = on_click_up
		self.color = 0
		self.colors = colors
		self.txt = txt
		self.fingers_id = set()

	def finger_down(self , event):
		"""
		Check if it is clicked, and it set to do action on click, do the action
		:param center: position of the click
		:return: bool
		"""
		old_click = self.clicked
		p_x = event.x * screen_rect.w
		p_y = event.y * screen_rect.h
		if self.rect.collidepoint((p_x , p_y)):  # cheeck click
			self.clicked = True
			self.color = 1
			self.do_action(on_click_down = True)
			self.fingers_id.add(event.finger_id)
			if old_click != self.clicked:
				if self.clicked:
					self.do_action(on_click_down = True)
		return self.clicked

	def finger_up(self , event):
		"""
		Set itself as not clicked, and it set to do a action, do the action if the mouse it in the rect
		:param event: pg.MOUSEBUTTONUP event
		:return:
		"""
		old_click = self.clicked
		if self.fingers_id:
			p_x = event.x * screen_rect.w
			p_y = event.y * screen_rect.h
			if self.rect.collidepoint((p_x , p_y)):
				self.do_action(on_click_down = False)
				self.fingers_id.discard(event.finger_id)
		self.clicked = bool(self.fingers_id)
		if old_click != self.clicked:
			if not self.clicked:
				self.do_action(on_click_down = False)

	def finger_motion(self , event):
		"""
		check if the button is pressed with the given motion
		:param event: pg.FINGERMOTION
		"""
		old_click = self.clicked
		p_x = event.x * screen_rect.w
		p_y = event.y * screen_rect.h
		if self.rect.collidepoint((p_x , p_y)):
			self.fingers_id.add(event.finger_id)
		else:
			self.fingers_id.discard(event.finger_id)
		self.clicked = bool(self.fingers_id)
		if old_click != self.clicked:
			if self.clicked:
				self.do_action(on_click_down = True)
			else:
				self.do_action(on_click_down = False)

	def draw(self , screen_to_draw):
		"""
		draw itself on the surface given
		:param screen_to_draw: pg.Surface
		:return: None
		"""
		if self.images:
			Animations.draw(self , screen_to_draw = screen_to_draw)
		else:
			pg.draw.rect(screen_to_draw , self.colors[self.color] , self.rect)

		if self.txt:
			button_text = main_menu_font.render(str(self.txt) , True , "black")
			text_rect = button_text.get_rect()
			text_rect.center = self.rect.center
			screen.blit(button_text , text_rect)

	def click_down_edit(self , event , button_pressed = None):
		"""
		create and put buttons_group in place, then print them
		:param event: pg.Event
		:return: boo
		"""
		if self.rect.collidepoint(event.pos):
			if button_pressed:
				ev_btn = button_pressed
			else:
				ev_btn = event.button
			if ev_btn == 1:
				self.clicked = True
				return True

			elif ev_btn == 4:
				self.rect.inflate_ip(10 , 0)

			elif ev_btn == 5:
				self.rect.inflate_ip(-10 , 0)

			elif ev_btn == 7:
				self.rect.inflate_ip(0 , 10)

			elif ev_btn == 6:
				self.rect.inflate_ip(0 , -10)

			elif ev_btn == 3:
				x , y , w , h = self.rect
				x = x / screen_rect.w
				y = y / screen_rect.h
				w = w / screen_rect.w
				h = h / screen_rect.h
				print(f'{x} , {y} , {w} , {h}' , f'"{self.txt}"')
			return True

	def click_down(self , event):
		"""
		Check if it is clicked, and it set to do action on click, do the action
		:param event: pg.MOUSEBUTTONDOWN
		:return: bool
		"""
		if self.rect.collidepoint(event.pos):  # cheeck click
			self.clicked = True
			self.color = 1
			self.do_action(on_click_down = True)
			return self.clicked

	def move(self):
		"""
		move itself in clicked
		:return:
		"""
		if self.clicked:
			self.rect.move_ip(pg.mouse.get_rel())

	def click_up(self , event):
		"""
		Set itself as not clicked, and it set to do a action, do the action if the mouse it in the rect
		:param event: pg.MOUSEBUTTONUP event
		:return:
		"""
		if self.clicked:
			self.clicked = False
			self.color = 0
			if self.on_click_up:
				if self.rect.collidepoint(event.pos):
					self.do_action(on_click_down = False)

	def click_up_edit(self , event):
		"""
		Set itself as not clicked, and it set to do a action, do the action if the mouse it in the rect
		:param event: pg.MOUSEBUTTONUP event
		:return:
		"""
		if self.clicked:
			self.clicked = False
			self.color = 0
			x , y , w , h = self.rect
			x = x / screen_rect.w
			y = y / screen_rect.h
			w = w / screen_rect.w
			h = h / screen_rect.h
			print(f'{x} , {y} , {w} , {h}' , f'"{self.txt}"')
			return True

	def do_action(self , on_click_down = True):
		"""
		Do whatever the action set to do.
		:return: None
		"""
		if on_click_down and self.on_click_down:
			self.on_click_down()
		elif (not on_click_down) and self.on_click_up:
			self.on_click_up()

	def update(self):
		"""
		Just change its color when hoovered or clicked
		:return:
		"""
		if self.clicked:
			self.color = 1
		else:
			self.color = 0