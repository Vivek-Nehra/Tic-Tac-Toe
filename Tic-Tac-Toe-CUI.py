import sys
from os import system,name
import __future__
board = [[0,0,0],[0,0,0],[0,0,0]]		# Considering a matrix for board


def print_board():		# To print the Tic-Tac-Toe board
	print()
	for i in range(3):

		print("\t\t\t\t",end="")		# end is used to prevent newline on new print method
		for j in range(3):

			print (" --- " , end="")

		print("\n\t\t\t\t",end="")
		for j in range(3):
			print ("| ", end="")

			if board[i][j]==1:
				print("0",end="")

			elif board[i][j]==2:
				print("X",end="")

			else:
				print(" ",end="")

			print (" |", end="")

		print()

	print("\t\t\t\t",end="")
	for j in range(3):
		print (" --- ",end="")
	print()



def pos_acquired(row_no,col_no):		# Check if current position is already acquired or not

	if board[row_no][col_no]== 0:
		return False

	else:
		return True

def check_tie():			# Check if there is a tie or not
	for i in range(3):
		for j in range(3):
			if board[i][j]==0:
				return False		# If some block is left, game can still continue
	return True		# No block is left, and there is no winner


def check_win():			# Check if current player has won or not
	for i in range(3):
		row_product = 1
		col_product = 1
		for j in range(3):
			row_product = row_product * board[i][j]
			col_product = col_product * board[j][i]

		if row_product == 1 or row_product == 8 or col_product == 1 or col_product == 8:
			#print("Row or Col True")			
			return True		# Check for rows and columns

	if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]) and (board[1][1]!=0):
		#print("Diagonal True")
		return True		# Check for diagonals


	return False		# No Winner found



def clear():		# Clears the screen
    # for windows
    if name == 'nt':
        _ = system('cls')		# Command in terminal/DOS

    # for mac and linux
    else:
        _ = system('clear')



def again():			# Resets the game once one is completed
	try:
		play_again=input("\n\n Do you Want to Play again:(Y/N) ")
		if play_again not in "YNyn":
			raise ValueError
		return play_again

	except ValueError:
		print (" Incorrect Input, please type again ")
		play_again = again()
		return play_again


# Main method Area
def main():
	global board
	clear()
	print ("Welcome to Tic-Tac-Toe game.")

	print_board()

	player=[]

	player.append(input("Enter name of player 1 :"))
	print (player[0] + " gets 0")

	player.append(input("Enter name of player 2 :"))
	print (player[1] + " gets X")

	turn_player = 0

	while (True):
		print ("\n\n Current turn : " +  player[turn_player])

		print_board()			# Print the board
		try:
			(row_no, col_no) = input("Enter the row and column number to mark: ").split()		# If values not equal to 2 are provided, ValueError occurs
			row_no,col_no = int(row_no.strip()),int(col_no.strip())

			if pos_acquired(row_no,col_no):
				raise OverflowError			# If current position is acquired, raise an exception

			board[row_no][col_no]= (turn_player+1)			# If row_no and col_no are not within list indices (0-2) , IndexError is caused

			if check_win() or check_tie():		# Check if there is a Win or a tie
				print_board()		# Print winner board ..

				if check_win():		# If there is a win
					print("Congratulations! " + player[turn_player] + " is the Winner!")

				elif check_tie():		# If there is a tie
					print("It's a tie!")


				play_again = again()		# Check if users want to play again

				if play_again  in "Yy":			# If users want to play again
					board=[[0,0,0],[0,0,0],[0,0,0]]
					main()
					
				else:
					break		# Indicates program success termination (Can use break)

			turn_player = (turn_player+1)%2		# Change current player
			clear()				# Clears the screen
		except ValueError:
			print("Invalid Value inputted. Please Enter again")

		except IndexError:
			print("Please specify indices between 0 and 2")

		except OverflowError:
			print("Position is already acquired")

		except:		# For some other errors like EOF
			pass


main ()		# Call to main
