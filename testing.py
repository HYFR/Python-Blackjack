#!/usr/bin/env python2
from random import randint
import pygame
from pygame.locals import *

black = (0,0,0)
white = (255,255,255)

class Table(object):

	player = []
	dealer = []

	def __init__(self):
		self.score = 0

	player_cap = 21 
	dealer_cap = 17	
	
	def deal_to_player(self):
		card = randint(1, 10)
		print "You have been dealt a card with a value of %r." % card
		self.player.append(card)
	
	def deal_to_dealer(self):
		card = randint(1, 10)
		print "You have been dealt a card with a value of %r." % card
		self.dealer.append(card)
	
	def player_score(self):
		return sum(self.player)
		
	def dealer_score(self):
		return sum(self.dealer)	
	
	def first_hit_dealer(self):
		first_card = randint(1, 10)
		second_card = randint(1, 10)
		total = first_card + second_card
		self.dealer.append(first_card)
		self.dealer.append(second_card)
		return first_card + second_card
	
	# Hits player and returns total
	def first_hit_player(self):
		first_card = randint(1, 10)
		second_card = randint(1, 10)
		self.player.append(first_card)
		self.player.append(second_card)
		return first_card + second_card
		
	def dealer_bust(self):
		if dealer_score() < Table.dealer_cap or dealer_score() > Table.dealer_cap:
			print "Player wins!"
			return player_score
		else: 
			print "Dealer wins!"
			return dealer_score
			
		
	def player_bust():
		if player_score() > Table.player_cap:
			print "Dealer won!"

class Game:

	def __init__(self):
		pygame.init()
		self._running = True
		self._display_surf = None
		self.table = Table()
		self.font = pygame.font.SysFont('Arial', 25)
		pygame.display.set_caption("Python Blackjack Game")
		self.screen = pygame.display.set_mode((653, 300))
		self.winner = None
		
		
	def on_init(self):
		pygame.init()
		self._running = True
		
	def on_cleanup(self):
		pygame.quit()
		
	def display_player_and_dealer_score(self):
		self.screen.blit(self.font.render("Player Score: {score}".format(score=self.table.player_score()),
						 True, (0, 0, 0)), 
						 (10, 15))
		self.screen.blit(self.font.render("Dealer Score: {dealers_score}".format(dealers_score=self.table.dealer_score()),
						 True, (0, 0, 0)),
						 (500, 15))
	
	def display_player_and_dealer_cards(self):
		self.screen.blit(self.font.render("Cards: {cards}".format(cards=self.table.player), True, (0, 0, 0)), (10, 40)), self.screen.blit(self.font.render("Cards: {dealers_cards}".format(dealers_cards=self.table.dealer), True, (0, 0, 0)), (500, 40))

	#White box at bottom left of the screen
	def left_box(self):
		self.rect = pygame.draw.rect(self.screen, (white), (0, 250, 100, 50), 0)
	
	#White box at bottom right of screen
	def right_box(self):
		self.rect = pygame.draw.rect(self.screen, (white), (555, 250, 100, 50), )

		
	def addText(self):
		self.screen.blit(self.font.render('Hit', True, (0, 0, 0)), (35, 265))
		self.screen.blit(self.font.render('Stay', True, (0, 0, 0)), (580, 265))
		
	def background_image(self):
		#initialise screen
		screen = pygame.display.set_mode((653, 300))
		pygame.init()
		#Fill Background
		background = pygame.image.load("Blackjack1.jpg")
		
		#Blit everything to the screen
		screen.blit(background, (0, 0))	

	def player_won_text(self):
		self.winner = "Player"
		
	def dealer_won_text(self):
		self.winner = "Dealer"

	def show_winners(self):
		self.screen.blit(self.font.render("{winner} Won!".format(winner=self.winner), True, (0, 0, 0,)), (293, 160))
				
		
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x,y = event.dict["pos"]
			print x,y
			if self.table.player_score() < Table.player_cap:
				if x < 100 and y > 250:
					print "hit"
					self.table.deal_to_player()
				elif x > 550 and y > 250:
					print "stay"
					self.table.deal_to_dealer()

			if self.table.player_score() >= Table.player_cap:
				self.player_won_text()
			elif self.table.dealer_score() >= Table.dealer_cap:
				self.dealer_won_text()
				
				
		self.mouse_click()
		
	
	def mouse_click(self):
		pass
		
	def on_execute(self):
		if self.on_init() == False:
			self._running = False

		while(self._running):
			for event in pygame.event.get():
				self.on_event(event)
			self.background_image()
			self.display_player_and_dealer_score()
			self.display_player_and_dealer_cards()
			if self.winner:
				self.show_winners()
			else:
				self.left_box()
				self.right_box()
				self.addText()
			pygame.display.flip()
		self.on_cleanup()

	
if __name__ == '__main__':
	myGame = Game()
	myGame.on_execute()
