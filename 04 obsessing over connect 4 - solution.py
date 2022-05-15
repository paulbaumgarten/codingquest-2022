# Sample solution for Coding Quest 2022 day 4
# Paul Baumgarten 2022
# codingquest.io

import requests
response = requests.get("https://codingquest.io/api/puzzledata?puzzle=4")
data = response.text.splitlines()
games = [[int(n) for n in line] for line in data]

# Draw a gameboard on screen
def draw(b):
    print("  1   2   3   4   5   6   7")
    for r in range(0, len(b)):
        for i in range(7):
            if b[r][i] == 0: b[r][i] = ' '
        print(f"| {b[r][0]} | {b[r][1]} | {b[r][2]} | {b[r][3]} | {b[r][4]} | {b[r][5]} | {b[r][6]} |")
        for i in range(7):
            if b[r][i] == ' ': b[r][i] = 0
    print(" --- --- --- --- --- --- ---")

# Play 1 game
def play(game):
    board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    player = 1
    move = 0
    while  move < len(game):
        # Place a piece
        row = 6                             # Start at the bottom of the board
        column = game[move]-1               # What column are we dropping a token into?
        while board[row][column] != 0:
            row -= 1                        # Move up the board until we find an empty slot
        board[row][column] = player

        # Check if player has won - vertical
        for column in range(0, 7):
            for row in range(0, 4):
                if board[row][column] == player and board[row+1][column] == player and board[row+2][column] == player and board[row+3][column] == player:
                    draw(board)
                    return player, "vertical"

        # Check if player has won - horizontal
        for row in range(0, 7):
            for column in range(0, 4):
                if board[row][column] == player and board[row][column+1] == player and board[row][column+2] == player and board[row][column+3] == player:
                    draw(board)
                    return player, "horizontal"

        # Check if player has won - diagonal \
        for row in range(0, 4):
            for column in range(0, 4):
                if board[row][column] == player and board[row+1][column+1] == player and board[row+2][column+2] == player and board[row+3][column+3] == player:
                    draw(board)
                    return player, "diagonal \\"

        # Check if player has won - diagonal /
        for row in range(0, 4):
            for column in range(0, 4):
                if board[row+3][column] == player and board[row+2][column+1] == player and board[row+1][column+2] == player and board[row][column+3] == player:
                    draw(board)
                    return player, "diagonal /"

        # Increment to next player and move
        player += 1
        if player > 3: player = 1
        move +=1

    # Game over, no player won, therefore a draw
    draw(board)
    return 0, "draw" # Draw

# Play all the games
winners = [0,0,0,0] # To log number of games won by each player
for g in range(0,len(games)):
    winner,method = play(games[g])
    print("Game",g,"winner",winner,method)
    winners[winner] += 1
print(winners)
print(winners[1]*winners[2]*winners[3])
