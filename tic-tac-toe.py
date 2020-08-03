import functions as fun
import sys

def print_grid (grid):
    for i in range (0, 3):
        print (str(grid[i*3]) + "|" + str(grid[i*3 + 1]) + "|" + str(grid[i*3 + 2]))
        if i < 2:
            print ("-+-+-")

board = ["_"]*9
forbidden_position = []
winner = "_"
player_turn = True
while winner == "_":
    print_grid (board)
    if len(forbidden_position) == 9:
        print ("Draw!")
        sys.exit(0)
    if player_turn:
        inp = input ("Enter the place: ")
        inp = int (inp)
        if fun.posibible_move(inp, forbidden_position):
            fun.move(board, inp - 1, "O")
            player_turn = not player_turn
            forbidden_position.append(inp)
            winner = fun.winner(board)
        else:
            print ("The move is illegal")
    else:
        move = fun.random_computer_move(forbidden_position)
        fun.move(board, move - 1, "X")
        player_turn = not player_turn
        forbidden_position.append(move)
        winner = fun.winner(board)
print ("The winner is \"" + winner + "\"")

