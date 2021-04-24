'''
Assigning values to the grid
The grid will look like this:
  0,0 | 0,1 | 0,2
  1,0 | 1,1 | 1,2
  2,0 | 2,1 | 2,2
'''
N = 3
dic= {(0, 0): 0, (0, 1): 0, (0, 2): 0, (1, 0): 0, (1, 1): 0, (1, 2): 0, (2, 0): 0, (2, 1): 0, (2, 2): 0}
grid = [['.' for x in range(N)] for y in range(N)]

#This function prints the grid of Tic-Tac-Toe as the game progresses
def print_grid():
    print("Player 1: X  vs  Player 2: O")
    print('--' + '---' * N + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(N):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * N + '--')

#This function checks if row or column or diagonal is full with same characters
def check_win():
 row_1 = grid[0][0]==grid[0][1]==grid[0][2] != "."
 row_2 = grid[1][0]==grid[1][1]==grid[1][2] != "."
 row_3 =  grid[2][0]==grid[2][1]==grid[2][2]!= "."
 column_1 =  grid[0][0]==grid[1][0]==grid[2][0] != "."
 column_2 =  grid[0][1]==grid[1][1]==grid[1][2] != "."
 column_3 =  grid[0][2]==grid[1][2]==grid[2][2] != "."
 diagonal_1 = grid[0][0]==grid[1][1]==grid[2][2] != "."
 diagonal_2 = grid[2][0]==grid[1][1]==grid[0][2] != "."
 if row_1 or row_2 or row_3 or column_1 or column_2 or column_3 or diagonal_1 or diagonal_2 :
      return True
 else:
      return False

#This function checks if row or column or diagonal is full with same characters
def check_tie(mark):
    if dic[(0, 0)]==1 and dic[(0, 1)]==1 and dic[(0, 2)]==1 and dic[(1, 0)]==1 and dic[(1, 1)]==1 and dic[(1, 2)]==1 and dic[(2, 0)]==1 and dic[(2, 1)]==1and dic[(2, 2)]==1: return True
    else: return False
    pass

#This function checks if given cell is empty or not
def check_empty(i, j):
    if dic[(i,j)]==0:
        dic[(i,j)]=1
        return True
    else:return False
    #pass

#This function checks if given position is valid or not
def check_valid_position(i, j):
    if i>=0 and i<=2 and j>=0 and j<=2:return True
    else: return False
    #pass

#This function sets a value to a cell
def set_cell(i, j, mark):
    grid[i][j]=mark
    #pass

#This function clears the grid
def grid_clear():
   dic[(0, 0)]=  0
   dic[(0, 1)]=  0
   dic[(0, 2)] = 0
   dic[(1, 0)] = 0
   dic[(1, 1)] = 0
   dic[(1, 2)] = 0
   dic[(2, 0)] = 0
   dic[(2, 1)] = 0
   dic[(2, 2)] = 0

   for i in range(0,N):
       for j in range(0,N):
           grid[i][j] = '.'
   #pass

#MAIN FUNCTION
def play_game():
    print("Tic-Tac-Toe Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Set mark value based on the player
        mark = 'X' if player == 0 else 'O'
        #Takes input from the user to fill in the grid
        print('Player %s' % mark)
        i, j = map(int, input('Enter the row index and column index: ').split())
        while not check_valid_position(i, j) or not check_empty(i, j):
            i, j = map(int, input('Enter a valid row index and a valid column index: ').split())
        #Set the input position with the mark
        set_cell(i, j, mark)
        #Check if the state of the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            print('Congrats, Player %s is won!' % mark)
            break
        #Check if the state of the grid has a tie state
        if check_tie(mark):
            #Prints the grid
            print_grid()
            print("Woah! That's a tie!")
            break
        #Player number changes after each turn
        player = 1 - player


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
