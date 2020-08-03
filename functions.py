import random

#Esta función determina si un movimiento es posible. Move es un entero del 1 al 9,
#mientras que forbidden es una lista de número (también enteros del 1 al 9, sin repetir)
def posibible_move (move, forbidden):
    if move > 9 or move in forbidden: #forbidden representa las casillas ya ocupadas, mientras que move representa el movimiento que se quiere realizar
        return False
    else:
        return True

def random_computer_move (forbidden):
    move = random.randint(0, 9) 
    if not posibible_move (move, forbidden):
        return random_computer_move (forbidden)
    else:
        return move

def winner (grid):
    #Primero, verifico las diagonales principales
    if grid[0] == grid[4] and grid[4] == grid[8] and grid[0] != "_":
        return grid[0]
    if grid[2] == grid[4] and grid[4] == grid[6] and grid[2] != "_":
        return grid[2]
    #Después, verifico columnas y filas
    for i in range (0, 2):
        if grid[i] == grid[i + 3] and grid[i + 3] == grid[i + 6] and grid[i] != "_":
            return grid[i]
        if grid[i*3] == grid[i*3 + 1] and grid[i*3 + 1] == grid[i*3 + 2] and grid[i*3] != "_":
            return grid[i*3]
    #Si todo falla, hay empate, que se representa con un "_"
    return "_"

#Esta simple función pone el jugador en su posición
def move (grid, move, player):
    grid[move] = player
    return grid
