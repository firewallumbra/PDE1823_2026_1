#tictactoe game.

# Find the 4 errors in the code and fix them,
# so the game works as expected.

def draw_line(width, edge, filling):
    print(filling.join([edge] * (width + 1)))


def display_winner(player):
    if player == 0:
        print("Tie")
    else:
        print("Player " + str(player) + " wins!")

def check_row_winner(row):
    """
    Return the player number that wins for that row.
    If there is no winner, return 0.
    """
    if row[0] == row[1] and row[1] == row[2]: # Will come back to this
        return row[0]
    return 0

def get_col(game, col_number):
    return [game[x][col_number] for x in range(3)]

def get_row(game, row_number):
    return game[row_number]

def check_winner(game):
    game_slices = []
    for index in range(3):
        game_slices.append(get_row(game, index))
        game_slices.append(get_col(game, index))

    # check diagonals
    down_diagonal = [game[x][x] for x in range(3)]
    up_diagonal = [game[0][2], game[1][1], game[2][0]]
    game_slices.append(down_diagonal)
    game_slices.append(up_diagonal)

    for game_slice in game_slices:
        winner = check_row_winner(game_slice)
        if winner != 0:
            return winner

    return winner

def start_game():
    return [[0, 0, 0] for x in range(3)]

def display_game(game):
    d = {2: "O", 1: "X", 0: "_"}
    draw_line(3, " ", "_")
    for row_num in range(3):
        new_row = []
        for col_num in range(3):
            new_row.append(d[game[row_num][col_num]])
        print("|" + "|".join(new_row) + "|")


def add_piece(game, player, row, column):
    """
    game: game state
    player: player number
    row: 0-index row
    column: 0-index column
    """
    game[row][column] = player # The function "convert_input_to_coordinate" handles the set logic "start with 1" and the "+1" beside "column" would confuse the players by adding a 1 to what they put in. For instance, if they pick column 1 and insert 1, it will choose the second column. Fixed by removing the "+1" in "[column]".
    return game

def check_space_empty(game, row, column):
    return game[row][column] == 0

def convert_input_to_coordinate(user_input):
    return user_input - 1

def switch_player(player):
    if player == 1: # Single equal sign is only used when assigning data to a variable but in this case, we need a double equal sign for comparison. Fixed by replacing the single equal sign with a double equal sign.
        return 2
    else:
        return 1

def moves_exist(game):
    for row_num in range(3):
        for col_num in range(3):
            if game[row_num][col_num] == 0:
                return True
    return False

if __name__ == '__main__':
    game = start_game()
    display_game(game)
    player = 1
    winner = 0  # the winner is not yet defined

    while winner == 0 and moves_exist(game):
        print("Currently player: " + str(player))
        available = False
        while not available # Issue here
            row = convert_input_to_coordinate(int(input("Which row? (start with 1) ")))
            column = convert_input_to_coordinate(int(input("Which column? (start with 1) ")))
            available = check_space_empty(game, row) # One reuiqred positional argument is missing here, which is "column". Fixed by adding "column" to the argument.
        game = add_piece(game, player, row, column)
        display_game(game)
        player = switch_player(player)
        winner = check_winner(game) # Because this line is stuck in a comment, the program refuses to declare a winner if a player meets all the conditions to win the game. Fixed by removing the hashtag in the beginning that kept the lines in a comment.
    display_winner(winner)

# An error that causes the code to run continuously without confirming the winner. Also one that counts 1, 2, and 3 as 0, 1, and 2.
