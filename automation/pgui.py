# Automating downloads from website;
# this is the result after realizing
# that the css-selectors for the site 
# were highly inadequate for bs4.
# (c) 2017 Ali Rassolie

import pyautogui as pg
import time

class Auto:
	def __init__(self):
		time.sleep(2)
		pg.moveTo(530, 265)
		time.sleep(2)
		pg.click()
		self.gen = self.main_page()
		self.download()

	def download(self):
		# Moving the mouse to the center
		x = 30
		for pos in range(20):
			time.sleep(5)
			pg.moveTo(1823,117)
			pg.click()
			time.sleep(2)
			pg.moveTo(1310,667)
			time.sleep(2)
			pg.click()
			pg.moveTo(17,51)
			pg.click()
			time.sleep(4)
			pg.moveTo(530, 265+x)
			pg.click()
			x += 30

	def main_page(self):
		pos = 0
		print("wu")
		while True:
			print("wu")
			yield pg.moveTo(530, 265+pos)
			pos += 30

if __name__ == '__main__':
	a  = Auto()