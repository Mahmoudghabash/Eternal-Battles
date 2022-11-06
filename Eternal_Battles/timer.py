"""
Timer Class to create enemies
"""
# from definitions import create_enemies
from datetime import datetime as dt , timedelta
from functools import partial


class Timer:
	def __init__(self , time_var = 5 , recurrent = False , command = None , groups = None):
		self.initial_time = dt.now()
		self.timer = timedelta(seconds = time_var)
		self.recurrent = recurrent
		self.command = command
		if groups is None:
			groups = []
		if type(groups) not in [list , tuple , set]:
			groups = list(groups)
		for group in groups:
			if type(group) == list:
				group.append(self)
			elif type(group) == set:
				group.add(self)
		self.groups = groups

	def set_time_var(self , time_var = 5):
		self.timer = timedelta(seconds = time_var)

	def update(self):
		now = dt.now()
		elapsed_time = now-self.initial_time
		if elapsed_time >= self.timer:
			if self.command:
				self.command()
			if self.recurrent:
				self.initial_time = dt.now()
			else:
				self.kill()
			return True

	def kill(self):
		for group in self.groups:
			if type(group) == list:
				print('list')
				group.remove(self)
			elif type(group) == set:
				print('set')
				group.discard(self)

	def get_elapsed_time_proportion(self):
		"""
		Get the proportion of the elapsed time and the total timer
		:return:
		"""
		return self.get_elapsed_time()/self.timer

	def get_elapsed_time(self):
		now = dt.now()
		return now - self.initial_time

	def get_remaining_time(self):
		now = dt.now()
		elapsed_time = now - self.initial_time
		return self.timer - elapsed_time

	def get_remaining_time_proportion(self):
		return self.get_remaining_time()/self.timer


if __name__ == '__main__':
	a = []
	running = True
	def change_running():
		global running
		print('aconteceu')
		running = False
	b = Timer(time_var = 1 , recurrent = False , command = partial(change_running) , groups = [a])
	while running:
		b.update()