import random

# Snakes and Ladders
snakes = {22: 6, 45: 30, 96: 64}
ladders = {7: 24, 21: 77, 42: 90, 40: 60}
player_pos = [0, 0]

def roll_dice():
    return random.randint(1, 6)

def move_player(player, position):
    dice = roll_dice()
    print(f" Player {player + 1} rolled a {dice}")
    position += dice
    if position > 100:
        print(" would exceed 100")
        position -= dice
    if position in snakes:
        print(f"  Bitten by a snake at {position} Going down to {snakes[position]}")
        position = snakes[position]
    elif position in ladders:
        print(f" Climbed a ladder at {position} Going up to {ladders[position]}")
        position = ladders[position]
    print(f" Player {player + 1} is now at {position}")
    return position

def play_game():
    turn = 0
    while True:
        input(f"Player {turn + 1} turn Press Enter to roll the dice")
        player_pos[turn] = move_player(turn, player_pos[turn])
        if player_pos[turn] == 100:
            print(f" Player {turn + 1} wins the game")
            
            break
        turn = 1 - turn  
play_game()
