import pygame,math,time
import settings

from layout import Layout
from polygon import *
from balls import *

pygame.init()
size = settings.General['width'], settings.General['height']
screen = pygame.display.set_mode(size)

class Clock:
	# cambiare la nomenclatura per i nomi lunghi?

	def __init__(self, hours, decamins, mins):
		self.hours = hours
		self.decamins = decamins
		self.mins = mins
	def display_time(self):
		h, m = time.localtime()[3:5]
		self.hours.change_state(h)
		self.decamins.change_state(m / 10)
		self.mins.change_state(m % 10)
	def test_time(self,h,m):
		self.hours.change_state(h)
		self.decamins.change_state(m / 10)
		self.mins.change_state(m % 10)		





if __name__ == "__main__":
	l=Layout(screen)
	c = Clock(l.balls, l.triangle, l.penthagon)
	while True:
		c.display_time()
		l.draw()
		time.sleep(20)
	



# non mi piace molto l'organizzazione, meglio da clock aggiungere gli elementi al layout forse



