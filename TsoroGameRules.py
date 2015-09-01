
class TsoroGameRules():

	def __init__(self):
		pass

	def print_rules(self):
		print ("\tSTRUCTURE OF THE GAME")
		print ("-------------------------------------------")
		print ("\t\t* Tsoro is a game that can only be played by 2 players")
		print ("\t\t* The game is played with a 4 x 8 board of pits and 64 paws.")
		print ("\t\t* The territory of the player is the two rows of pits closest to you.")
		print ("\t\t* Each player stars with 4 pawns in each pit in the closest back row of their territory.")
		print ("\t\t* The player can only pick pawns on their side.")
		print ("\t\t* In every tour , the player takes all the pawns of a pit in the choice of his zone of game.")
		print ("""\t\t* By moving anticlockwise he is going to sow his paws one by one in pits 
		following directly the pit of origin of the movement until falling in an empty pit.""")
		print ("\t\t* The player can only pick paws if they are more than one.")
		print ("*" * 100)
	
		print ("\tHOW TO CAPTURE THE PAWNS OF OPPONENT")
		print ("-----------------------------------------------")
		print ("""\t\t* If ever the pit of arrival is in the central row 
		and the two pits opposite to this contain at least a pawn,
		the payer has to eat(take) the pawns of these two opposite cavities.""")
		print ("""\t\t* He is then going to sow these pawns in the sense of the game
		one by one in pits following directly the pits of origin.""")
		print ("\t\t* The greater the number of pawns to capture from the opponent side",
			"the better it is for the player")
		print ("*" * 100)
		
		print ("\tCAPTURE BY REVERSING")
		print ("-----------------------------")
		print ("""\t\t* An exception of moving in an clockwise direction
		is when your last drop results in the capturing of the opponent pawns.""")
		print ("*" * 100)
		
		print ("\tTHE COMPLETION OF THE GAME")
		print ("------------------------------------")
		print ("""\t\t* The normal way to win the game is to be the last player to be able to take the legal move, possible
		by capturing an opponent's pawns or reducing to no more than one pawn in each pit.""")
		print ("""\t\t* Another way is to capture the pawns of the opponent
		in two separate turns before he/she has captured any seeds.""") 
		print ("\t\t* On capturing seeds on both ends of the board during the same turn.")
	
