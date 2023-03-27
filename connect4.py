import numpy as np

# Define the dimensions of the game grid
num_hyperlayers = 5
num_layers      = 5
num_columns     = 5
num_rows        = 5
win_length      = 4

# Initialize the game grid as a multidimensional array
game_grid = np.zeros((num_hyperlayers, num_layers, num_columns, num_rows), dtype=int)

# Define a function to print the game grid
def print_game_grid():
    print("\n")
    for l in range(num_layers-1, -1, -1):
        print("".ljust(11), end="")
        for h in range(num_hyperlayers):
            print("H" + str(h+1).ljust(9), end="")
        print("")
        for r in range(num_rows-1, -1, -1):
            print("L" + str(l+1).ljust(4), end=" ")
            for h in range(num_hyperlayers):
                print("  ", end="")
                print(str(game_grid[h][l][0][r]).ljust(2), str(game_grid[h][l][1][r]).ljust(2), str(game_grid[h][l][2][r]).ljust(2), end="")
            print("")
        print("")

    print("\n")

# Define a function to check if a move is valid
def is_valid_move(h, l, c):
    return game_grid[h][l][c][num_rows-1] == 0

# Define a function to make a move
def make_move(h, l, c, player):
    for r in range(num_rows):
        if game_grid[h][l][c][r] == 0:
            game_grid[h][l][c][r] = player
            break

# Define a function to check if a player has won
def check_for_win(player):
    # Check for wins in each hyperlayer
    for h in range(num_hyperlayers):
        # Check for wins in each layer
        for l in range(num_layers):
            # Check for wins in each column
            for c in range(num_columns):
                # Check for wins in each row
                for r in range(num_rows):
                    # Check for a win in the row direction
                    if r <= num_rows - win_length:
                        if all(game_grid[h][l][c][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the column direction
                    if c <= num_columns - win_length:
                        if all(game_grid[h][l][c+i][r] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (top-left to bottom-right)
                    if r <= num_rows - win_length and c <= num_columns - win_length:
                        if all(game_grid[h][l][c+i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (bottom-left to top-right)
                    if r >= win_length - 1 and c <= num_columns - win_length:
                        if all(game_grid[h][l][c+i][r-i] == player for i in range(win_length)):
                            return True
        # Check for wins in each row in the hyperlayer
        for r in range(num_rows):
            # Check for wins in each column in the hyperlayer
            for c in range(num_columns):
                # Check for wins in each layer in the hyperlayer
                for l in range(num_layers):
                    # Check for a win in the layer direction
                    if l <= num_layers - win_length:
                        if all(game_grid[h][l+i][c][r] == player for i in range(win_length)):
                            return True
                    # Check for a win in the column direction
                    if c <= num_columns - win_length:
                        if all(game_grid[h][l][c+i][r] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (layer-column plane)
                    if l <= num_layers - win_length and c <= num_columns - win_length:
                        if all(game_grid[h][l+i][c+i][r] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (layer-row plane)
                    if l <= num_layers - win_length and r <= num_rows - win_length:
                        if all(game_grid[h][l+i][c][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (column-row plane)
                    if c <= num_columns - win_length and r <= num_rows - win_length:
                        if all(game_grid[h][l][c+i][r+i] == player for i in range(win_length)):
                            return True
    # Check for wins in each row in each layer in each column in each hyperlayer along the fourth dimension
    for r in range(num_rows):
        for c in range(num_columns):
            for l in range(num_layers):
                for h in range(num_hyperlayers - win_length + 1):
                    # Check for a win in the fourth dimension
                    if all(game_grid[h+i][l][c][r] == player for i in range(win_length)):
                        return True
                    # Check for a win in the diagonal direction (hyperlayer-layer-column-row)
                    if l <= num_layers - win_length and c <= num_columns - win_length and r <= num_rows - win_length and h <= num_hyperlayers - win_length:
                        if all(game_grid[h+i][l+i][c+i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (hyperlayer-layer-column-top-to-bottom-row)
                    if l <= num_layers - win_length and c <= num_columns - win_length and r <= num_rows - win_length and h >= win_length - 1:
                        if all(game_grid[h-i][l+i][c+i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (hyperlayer-layer-column-bottom-to-top-row)
                    if l <= num_layers - win_length and c <= num_columns - win_length and r >= win_length - 1 and h >= win_length - 1:
                        if all(game_grid[h-i][l+i][c+i][r-i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (hyperlayer-layer-top-to-bottom-column-row)
                    if l <= num_layers - win_length and c >= win_length - 1 and r <= num_rows - win_length and h >= win_length - 1:
                        if all(game_grid[h-i][l+i][c-i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (hyperlayer-layer-bottom-to-top-column-row)
                    if l <= num_layers - win_length and c >= win_length - 1 and r >= win_length - 1 and h >= win_length - 1:
                        if all(game_grid[h-i][l+i][c-i][r-i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (hyperlayer-row-column-layer)
                    if c <= num_columns - win_length and l <= num_layers - win_length and h <= num_hyperlayers - win_length and r <= num_rows - win_length:
                        if all(game_grid[h+i][l+i][c+i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (hyperlayer-row-column-top-to-bottom-layer)
                    if c <= num_columns - win_length and l <= num_layers - win_length and r <= num_rows - win_length and h >= win_length - 1:
                        if all(game_grid[h-i][l+i][c+i][r-i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (hyperlayer-row-layer-column)
                    if c <= num_columns - win_length and h <= num_hyperlayers - win_length and r <= num_rows - win_length and l <= num_layers - win_length:
                        if all(game_grid[h+i][l+i][c+i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (hyperlayer-row-layer-top-to-bottom-column)
                    if c >= win_length - 1 and h <= num_hyperlayers - win_length and r <= num_rows - win_length and l <= num_layers - win_length:
                        if all(game_grid[h+i][l+i][c-i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (hyperlayer-row-layer-bottom-to-top-column)
                    if c >= win_length - 1 and h <= num_hyperlayers - win_length and r >= win_length - 1 and l <= num_layers - win_length:
                        if all(game_grid[h+i][l+i][c-i][r-i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (hyperlayer-column-row-layer)
                    if r <= num_rows - win_length and h <= num_hyperlayers - win_length and l <= num_layers - win_length and c <= num_columns - win_length:
                        if all(game_grid[h+i][l+i][c+i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (hyperlayer-column-row-top-to-bottom-layer)
                    if r <= num_rows - win_length and h >= win_length - 1 and l <= num_layers - win_length and c <= num_columns - win_length:
                        if all(game_grid[h-i][l+i][c+i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (hyperlayer-column-row-bottom-to-top-layer)
                    if r >= win_length - 1 and h >= win_length - 1 and l <= num_layers - win_length and c <= num_columns - win_length:
                        if all(game_grid[h-i][l+i][c+i][r-i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (hyperlayer-row-column-bottom-to-top-layer)
                    if c <= num_columns - win_length and l <= num_layers - win_length and r >= win_length - 1 and h >= win_length - 1:
                        if all(game_grid[h-i][l+i][c-i][r-i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (hyperlayer-layer-top-to-bottom-row)
                    if l <= num_layers - win_length and c >= win_length - 1 and r <= num_rows - win_length and h >= win_length - 1:
                        if all(game_grid[h-i][l+i][c-i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (hyperlayer-layer-bottom-to-top-row)
                    if l <= num_layers - win_length and c >= win_length - 1 and r >= win_length - 1 and h >= win_length - 1:
                        if all(game_grid[h-i][l+i][c-i][r-i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (layer-column-row-hyperlayer)
                    if r <= num_rows - win_length and c <= num_columns - win_length and h <= num_hyperlayers - win_length and l <= num_layers - win_length:
                        if all(game_grid[h+i][l+i][c+i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (layer-column-top-to-bottom-row-hyperlayer)
                    if r <= num_rows - win_length and c <= num_columns - win_length and h >= win_length - 1 and l <= num_layers - win_length:
                        if all(game_grid[h-i][l+i][c+i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (layer-column-bottom-to-top-row-hyperlayer)
                    if r >= win_length - 1 and c <= num_columns - win_length and h >= win_length - 1 and l <= num_layers - win_length:
                        if all(game_grid[h-i][l+i][c+i][r-i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (layer-row-hyperlayer-column)
                    if c <= num_columns - win_length and r <= num_rows - win_length and h <= num_hyperlayers - win_length and l <= num_layers - win_length:
                        if all(game_grid[h+i][l+i][c+i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (layer-row-hyperlayer-column-top-to-bottom)
                    if c <= num_columns - win_length and r <= num_rows - win_length and h >= win_length - 1 and l <= num_layers - win_length:
                        if all(game_grid[h-i][l+i][c+i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (layer-row-hyperlayer-column-bottom-to-top)
                    if c <= num_columns - win_length and r >= win_length - 1 and h >= win_length - 1 and l <= num_layers - win_length:
                        if all(game_grid[h-i][l+i][c+i][r-i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (row-hyperlayer-column-layer)
                    if l <= num_layers - win_length and c <= num_columns - win_length and h <= num_hyperlayers - win_length and r <= num_rows - win_length:
                        if all(game_grid[h+i][l+i][c+i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (row-hyperlayer-column-layer-top-to-bottom)
                    if l <= num_layers - win_length and c <= num_columns - win_length and h >= win_length - 1 and r <= num_rows - win_length:
                        if all(game_grid[h-i][l+i][c+i][r+i] == player for i in range(win_length)):
                            return True
                    # Check for a win in the diagonal direction (row-hyperlayer-column-layer-bottom-to-top)
                    if l <= num_layers - win_length and c <= num_columns - win_length and h >= win_length - 1 and r >= win_length - 1:
                        if all(game_grid[h-i][l+i][c+i][r-i] == player for i in range(win_length)):
                            return True

    return False

# Define the players
player1 = 1
player2 = 2

# Define a variable to keep track of the current player
current_player = player1

# Define a variable to keep track of the number of moves
num_moves = 0

# Define a function to check if a move is valid
def is_valid_move(h, l, c):
    if h < 0 or h >= num_hyperlayers or l < 0 or l >= num_layers or c < 0 or c >= num_columns:
        return False
    return game_grid[h][l][c][num_rows-1] == 0

# Define a function to get valid input from the user
def get_valid_input(prompt, lower_bound, upper_bound):
    while True:
        try:
            value = input(prompt)
            if value.lower() == 'exit':
                quit()
            value = int(value)
            if value < lower_bound or value > upper_bound:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter an integer between", lower_bound, "and", upper_bound, "or 'exit' to quit")

# Loop until there is a winner or the game is a tie
while True:
    # Print the game grid
    print_game_grid()

    # Prompt the current player to enter their move
    print(f"Player {current_player}'s turn.")
    h = get_valid_input("Enter hyperlayer (1 to " + str(num_hyperlayers) + "): ", 1, num_hyperlayers) - 1
    l = get_valid_input("Enter layer (1 to " + str(num_layers) + "): ", 1, num_layers) - 1
    c = get_valid_input("Enter column (1 to " + str(num_columns) + "): ", 1, num_columns) - 1

    # Check if the move is valid
    if is_valid_move(h, l, c):
        # Make the move
        make_move(h, l, c, current_player)
        num_moves += 1

        # Check if the current player has won
        if check_for_win(current_player):
            print_game_grid()
            print(f"Player {current_player} wins!")
            break

        # Check if the game is a tie
        if num_moves == num_hyperlayers * num_layers * num_columns * num_rows:
            print_game_grid()
            print("The game is a tie.")
            break

        # Switch to the other player
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
    else:
        print("Invalid move. Please try again.")
