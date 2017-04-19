# Mandelbrot set
# Fc(z) = z^2 + c; where c is a complex number; c = a + bi, c**2 = a^2-b^2+2abi 
# If we start by iterating this from z=0, then this should 
# not diverge, but it should be bounded by some absolute value. 
# Vad man ska göra är att man ska treata c som pixeln, antagligen,
# gem att sedan se om de är boundade eller om de divergar mot infinity, for each 
# one of them. 

import cmath, math

def setup():
	size(500,500)
	colorMode(RGB)
	background(100, 200,100)

def draw():

	noLoop()
	loadPixels()
	maxit = 20
	w = width
	h = height

	for t in range((w*h)):
		x = t % w
		y = (t - x) / w	
		x = map(x, 0, width, -2.5, 0.5) 
		y = map(y, 0, height, -1.5, 1.5)
		# Det map gör är vldigt viktigt, låt oss säga att du har en value mellan 
		# 0 och din width, vilket är din x value, men du vill ha en korresponderande
		# value mellan en mindre range, som 2.5, 0, då kmr map att hjälpa till, vilket är 
		# bra i detta fallet. 
		c = x + (y * cmath.sqrt(-1))
		fnc = 0
		k = 0
		
		for n in range(maxit):
			fnc = fnc*fnc + c
			
			if fnc.real > 2:
				pixels[t] = color(100)
				break
			pixels[t] = color(k%255, (k*2)%255,(k*3)%255)
			k += 1
		if k > (maxit-5):
			pixels[t] = color(k%255, (k*2)%255,(k*3)%255)

	updatePixels()
	print(frameRate)
	
