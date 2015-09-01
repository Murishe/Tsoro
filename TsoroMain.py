from TsoroGameEngine import TsoroGameEngine
from TsoroGameRules import TsoroGameRules
from UnitActionEnum import UnitAction
from random import randrange
import os

def convert_str(s):
	# Convert string to either int or float.
	try:
		ret = int(s)
	except ValueError:
		#Try float.
		ret = float(s)
	return ret

def start():
	start = False
	won = False 
	tsoro = None
	turn_selection = False
	
	while start == False:

		print("Welcome to game Tsoro!")
		rules = TsoroGameRules()
		rules.print_rules()
		
		start_option = input("Please choose the game level and press return: Easy (1) - Medium (2) - Hard (3): ")
		
		level = convert_str(start_option)        
		
		if level in range(1,4):
			tsoro = TsoroGameEngine(level)
		
			os.system('cls')        #clears screen
			#os.system('color c')    #light red console background

			tsoro.print_board()
			
			while turn_selection == False:
				turn =  input("Would you like to start first? Y/N ").upper()  
				if turn == "Y" or turn == "YES":                
					os.system('color a')    #light green console background 
					turn_selection = True                         
					
				elif turn == "N" or turn == "NO":
					tsoro.computer_start()
					turn_selection = True   

				else:
					print('You have chosen an invalid choice!\n')
					print('Try again\n')

			start = True

		else:
			print('You have chosen an invalid level!\n')
			print('Try again\n')
			
	player = tsoro.get_current_player()
	
	while won == False:				
		
		move = {'index_begin': 0, 'action': 0}
		if player == 1:			
			move_index = convert_str(input("Which hole do you want to pick from?"))
			move['index_begin'] = move_index
			move['action'] = UnitAction.ACTION_GO_FORWARD
		else:
			rand = randrange(7, 16)
			move['index_begin'] = rand
			move['action'] = UnitAction.ACTION_GO_FORWARD

		os.system('cls') 
		units = tsoro.action_to_units(player, move)
				
		action = tsoro.execute()
		print(action)
		board = tsoro.get_current_board()
		
		tsoro.print_board()
		player = (2 if player == 1 else 1) 

		won == units
		
		
		
	input("Hit enter to close. ")

start()
