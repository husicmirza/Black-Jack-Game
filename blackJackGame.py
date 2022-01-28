import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
		 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
	
	def __init__(self,suit,rank):
		self.suit=suit
		self.rank=rank
		self.value=values[rank]
	
	def __str__(self):
		return self.rank + ' of ' + self.suit



class Deck:
	
	def __init__(self):
		self.deck = []  
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))
	
	def __str__(self):
		return ' '.join([str(item)for item in self.deck])
				

	def shuffle(self):
		random.shuffle(self.deck)
		
	def deal(self):
		return self.deck.pop()


class Hand:
	def __init__(self):
		self.cards = []  
		self.value = 0   
		self.aces = 0    
	
	def add_card(self,card):
		self.cards.append(card)
		self.value+=values[card.rank]
		if card.rank == 'Ace':
			self.aces+=1
   
	def adjust_for_ace(self):
		while self.value>21 and self.aces:
			self.value-=10
			self.aces-=1
		
	
	def __str__(self):
		return  '[{}]' .format(','.join([str(item)for item in self.cards]))



class Chips:
	
	def __init__(self):
		self.total = 1000  
		self.bet = 0
		
	def win_bet(self):
		self.total+=self.bet
	
	def lose_bet(self):
		self.total-=self.bet



def take_bet(chips):
	print('Total amount of chips: {}'.format(chips.total))
	while True:
		try:
			chips.bet=int(input('Place a bet: '))    
		except:
			continue
		else:
			
			if chips.bet>chips.total:
				print('You don\'t have enough chips! Try again: ')
			else:
				break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        try:
            player_move=int(input('What is your move 1-Hit or 2-Stand\nInput 1 or 2: '))
        except:
            continue
        else:
            if player_move==1:
                hit(deck,hand)
                break
            elif player_move==2:
                playing=False
                break
            else:
                continue


def show_some(player,dealer):
	
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("\nDealer's Hand: ")
    print(" <hidden card>")
    print(' ',dealer.cards[0])
    print('\n')

    
def show_all(player,dealer):
	print("\nPlayer's Hand:", *player.cards, sep='\n ')
	print("\nPlayer's Value: {}".format(player.value))
	print("\nDealer's Hand:", *dealer.cards, sep='\n ')
	print("\nDealer's Value: {}".format(dealer.value))
	print()

def player_busts(chips):
    print('Player busts!')
    chips.lose_bet()        

def player_wins(chips):
	print('Player wins!')
	chips.win_bet()

def dealer_busts(chips):
	print('Dealer busts!')
	chips.win_bet()        

    
def dealer_wins(chips):
	print('Dealer wins!')
	chips.lose_bet()

def replay():

    print('Would you like to play again?')
    choice=''
    while True:
    	try:
    		choice=input('Enter Y or N :' ).upper()
    	except:
    		print('Try again!')
    		continue
    	else:
    	 	if choice=='Y':
    	 		return True
    	 		break
    	 	elif choice=='N':
    	 		return False
    	 		break
    	 	else:
    	 		continue
        	
if __name__ == '__main__':

	chips=Chips()
	while True:

		print("Welcome to Black Jack game!\n")
		deck = Deck()
		deck.shuffle()

		player1 = Hand()
		dealer = Hand()

		take_bet(chips)

		player1.add_card(deck.deal())
		player1.add_card(deck.deal())
		dealer.add_card(deck.deal())
		dealer.add_card(deck.deal())

		show_some(player1,dealer)

		while playing:
			hit_or_stand(deck,player1)
			show_some(player1,dealer)

			if player1.value>21:
				player_busts(chips)
				break
		
		if player1.value<=21:
			
			while dealer.value<17:
				hit(deck,dealer)

			show_all(player1,dealer)

			if dealer.value>21:
				dealer_busts(chips)
			elif dealer.value<player1.value:
				player_wins(chips)
			elif dealer.value>player1.value:	
				dealer_wins(chips)	
			else:
				print("Dealer and Player tie! It's a push.")

		print('Player\'s number of chips: {}\n'.format(chips.total))
		
		if chips.total==0:
			print('Game Over!\nNo more chips!')
			break
		elif replay():
			playing=True
			continue
		else:
			break


		




