from xml.dom import minidom
import pygame
import sys

global assets, asset_height, asset_width, screen

def initAssets():
	global assets, asset_height, asset_width
	assetnodes = minidom.parse('assets.xml').getElementsByTagName('asset')
	assets = dict( [\
		(i.attributes["name"].value, pygame.image.load('assets/'+i.attributes["image"].value)) for i in assetnodes\
		] )
	asset_height = dict( [\
		(i, assets[i].get_rect().bottom) for i in assets\
		] )
	asset_width = dict( [\
		(i, assets[i].get_rect().right) for i in assets\
		] )

def get_height(name):
	global asset_height
	return asset_height[name]

def get_width(name):
	global asset_width
	return asset_width[name]

def window(width, height):
	global screen
	pygame.init()
	screen = pygame.display.set_mode((width, height))

def draw(array):
	global assets, screen
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	screen.fill((0, 0, 0))
	for (name, x, y) in array:
		screen.blit(assets[name], (x, y))
	pygame.display.flip()
