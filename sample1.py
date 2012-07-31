from header import *

initAssets()

width, height = 1000, 400

window(width, height)

paddle1x = 0
paddle2x = width - get_width("paddle")
paddle1y = 0
paddle2y = 0
minballx = get_width("paddle")
maxballx = width - get_width("paddle") - get_width("ball")
minbally = 0
maxbally = height - get_height("ball")
ballx = minballx
bally = 0
dx = 2
dy = 1

while 1:
	ballx += dx
	bally += dy
	if ballx > maxballx:
		ballx = maxballx
		dx = -dx
	if ballx < minballx:
		ballx = minballx
		dx = -dx
	if bally > maxbally:
		bally = maxbally
		dy = -dy
	if bally < minbally:
		bally = minbally
		dy = -dy
	draw( [ ("paddle", paddle1x, bally), ("ball", ballx, bally), ("paddle", paddle2x, bally) ] )
