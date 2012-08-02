from header import *

initAssets()

width, height = 1000, 400

window(width, height)

minballx = 0
maxballx = width - get_width("ball")
minbally = 0
maxbally = height - get_height("ball")
ballx = 0
bally = 0
bally2 = 0
dx = 3
dy = 0

while 1:
	ballx += dx
	bally += dy
	bally2+= dy2
        dy += .1
	if ballx > maxballx:
		ballx = maxballx
		dx = -dx
	if ballx < minballx:
		ballx = minballx
		dx = -dx
	if bally > maxbally:
		bally = maxbally
		dy = -dy*.9
	draw( [ ("ball", ballx, bally) ] )
