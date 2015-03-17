#!/usr/bin/env python2
from random import randint
import pygame
from pygame.locals import *


import unittest


# These variables hold the colors that I will be using for text.
black = (0,0,0)
white = (255,255,255)

class Table(object):

	player = []
	dealer = []

	def __init__(self):
		self.score = 0
		self.first_hit_player()

	# These variables hold the numbers that I will be using to determine who won the game.
	player_cap = 21 
	dealer_cap = 17	
	game_cap =  21
	
	# Number
	# Generates a random number from 1-10 and appends the number to the player's hash.
	def deal_to_player(self):
		card = randint(1, 10)
		print "You have been dealt a card with a value of %r." % card
		self.player.append(card)
	# Number
	# Generates a random number from 1-10 and appends the number to the dealer's hash.
	def deal_to_dealer(self):
		card = randint(1, 10)
		print "You have been dealt a card with a value of %r." % card
		self.dealer.append(card)
	
	# Number
	# Adds all the numbers found within the player's hash and returns it.
	def player_score(self):
		return sum(self.player)
		
	# Number	
	# Adds all the numbers found within the dealer's hash and returns it.
	def dealer_score(self):
		return sum(self.dealer)	
	
	# Number
	# Two numbers are generated within the range of 1-10 and are added to the dealer's
	# hash.
	def first_hit_dealer(self):
		first_card = randint(1, 10)
		second_card = randint(1, 10)
		total = first_card + second_card
		self.dealer.append(first_card)
		self.dealer.append(second_card)
		return first_card + second_card
	
	# Number
	# Two numbers are generated within the range of 1-10 and are added to the dealer'score
	# hash.
	def first_hit_player(self):
		first_card = randint(1, 10)
		second_card = randint(1, 10)
		self.player.append(first_card)
		self.player.append(second_card)
		return first_card + second_card
		
			
	def dealer_hand(self):
		self.first_hit_dealer()
		if self.dealer_score() < self.dealer_cap:
			while self.dealer_score() < self.dealer_cap:
				self.deal_to_dealer()
		
			
	
	# String
	# Sum of numbers in player's hash is compared to the player's cap.
	# A string is printed if dealer won.
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
		
	# Stops the game once I click exit.	
	def on_cleanup(self):
		pygame.quit()
		
	# Image
	# Renders two images on both sides of the screen with their appropriate scores.
	def display_player_and_dealer_score(self):
		self.screen.blit(self.font.render("Player Score: {score}".format(score=self.table.player_score()),
						 True, white), 
						 (10, 15))
		self.screen.blit(self.font.render("Dealer Score: {dealers_score}".format(dealers_score=self.table.dealer_score()),
						 True, white),
						 (500, 15))
	
	# Image
	# Displays the cards inside player and dealer's hash.
	def display_player_and_dealer_cards(self):
		self.screen.blit(self.font.render("Cards: {cards}".format(cards=self.table.player), True, white), (10, 40)), self.screen.blit(self.font.render("Cards: {dealers_cards}".format(dealers_cards=self.table.dealer), True, white), (500, 40))
	
	# Image
	# 'Hit' button at the bottom left of the screen. 
	def left_box(self):
		self.rect = pygame.draw.rect(self.screen, (white), (0, 250, 100, 50), 0)
	
	# Image
	# 'Stay' button at the bottom left of the screen.
	def right_box(self):
		self.rect = pygame.draw.rect(self.screen, (white), (555, 250, 100, 50), )

	# String
	# Adds 'hit' and 'stay' to the white boxes at either side at the bottom of the screen.
	def addText(self):
		self.screen.blit(self.font.render('Hit', True, black), (35, 265))
		self.screen.blit(self.font.render('Stay', True, black), (580, 265))
		
	def background_image(self):
		#initialise screen
		screen = pygame.display.set_mode((653, 300))
		pygame.init()
			
	# Number	
	# The sum found within the dealer's hash is compared to dealer's cap, 17, and based
	# on that information, the game decides whether the player or dealer won.
	def dealer_bust(self):
		if self.table.dealer_score() < self.table.player_score() or self.table.dealer_score() > Table.game_cap:
			self.player_won_text()
			return self.table.player_score()
		else: 
			#print "Dealer wins!"
			self.dealer_won_text()
			return self.table.dealer_score()
		
	# String
	# A helper function that produces the string 'Player' if player wins.
	def player_won_text(self):
		self.winner = "Player"
	
	# String
	# A helper function that produces the string 'Dealer' if dealer wins.
	def dealer_won_text(self):
		self.winner = "Dealer"

	# String
	# Declares the winner by printing either "Dealer won!" or "Player won!"
	def show_winners(self):
		self.screen.blit(self.font.render("{winner} Won!".format(winner=self.winner), True, white), (293, 160))
				
	def show_tie(self):
		self.screen.blit(self.font.render("There was a tie!"), True, white), (293, 160)
	# Event
	# Allows for the game to run once the 'hit' or 'stay' buttons are pushed.
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
					self.table.dealer_hand()
					self.dealer_bust()
					

			if self.table.player_score() >= Table.game_cap:
				self.dealer_won_text()
			elif self.table.player_score() == Table.game_cap:
				self.player_won_text()
			elif self.table.dealer_score() == Table.game_cap:
				self.dealer_won_text()
			elif self.table.dealer_score() >= Table.game_cap:
				self.player_won_text()
			elif self.table.dealer_score() == self.table.player_score():
				self.show_tie()
			elif self.table.dealer_score() > 1 & self.table.player_score() > 1:
				if self.table.dealer_score() > self.table.player_score():
					self.dealer_won_text()
				elif self.table.dealer_score() < self.table.player_score():
					self.player_won_text()
			
				
				
		self.mouse_click()
		
	# Event
	# Allows mouse clicks within the Pygame window.
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

		
class MyTest(unittest.TestCase):

	
	def setUp(self):
		""" Setting up for the test """
		print "FooTest:setUP_:begin"
		
		testName = self.shortDescription()
		if (testName == "Test routine A"):
			print "setting up for test A"
			
		print "FooTest:setUp_:end"
		
	def tearDown(self):
		""" Cleaning up after the test """
		print "FooTest:tearDown_:begin"
		
		testName = self.shortDescription()
		if (testName == "Test routine A"):
			print "cleaning up after test A"
			
		print "FooTest:tearDown_:end"
	
	def test_game(self):
		self.table = Table()
		
		deal_to_player = self.table.deal_to_player()
		deal_to_dealer =  self.table.deal_to_dealer()
		
		
		#self.assertEqual((1..10), deal_to_player()) expects a number within the range
		# of 1-10 for the method, deal_to_player
		
		#self.assertEqual((1..10), deal_to_dealer()) expects a number within the range
		# of 1-10 for the method, deal_to_dealer
		
if __name__ == '__main__':
	myGame = Game()
	myGame.on_execute()
	unittest.main()