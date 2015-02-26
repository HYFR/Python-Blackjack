from random import *
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
	
	def deal_to_player(self, player):
		card = random.randint(1, 10)
		print "You have been dealt a card with a value of %r." % card
		player.append(card)
	
	def deal_to_dealer(self, dealer):
		card = random.randint(1, 10)
		print "You have been dealt a card with a value of %r." % card
		dealer.append(card)
	
	def player_score(self):
		return sum(self.player)
		
	def dealer_score(self):
		return sum(self.player)	
	
	def first_hit_dealer():
		first_card = random.randint(1, 10)
		second_card = random.randint(1, 10)
		total = first_card + second_card
		dealer.append(first_card)
		dealer.append(second_card)
	
	# Hits player and returns total
	def first_hit_player(self):
		first_card = random.randint(1, 10)
		second_card = random.randint(1, 10)
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
		
		
	def on_init(self):
		pygame.init()
		self._running = True
		
	def on_event(self, event):
		#print event
		if event.type == pygame.QUIT:
			self._running = False
		elif event.type == pygame.MOUSEBUTTONUP:
			print "clicked"
			self.mouse_click()
		
		
	def on_cleanup(self):
		pygame.quit()
		
	def display_player_and_dealer_score(self):
		self.screen.blit(self.font.render("Player Score: {score}".format(score=self.table.player_score()), True, (0, 0, 0)), (10, 15)), self.screen.blit(self.font.render("Dealer Score: {dealers_score}".format(dealers_score=self.table.dealer_score()), True, (0, 0, 0)), (500, 15))
	
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
			self.left_box()
			self.right_box()
			self.addText()
			pygame.display.flip()
		self.on_cleanup()

	
if __name__ == '__main__':
	myGame = Game()
	myGame.on_execute()