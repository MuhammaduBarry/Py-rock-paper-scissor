# Creating a Tic-Tac-Toe game
import random

# List for our game choices
choices = ["rock", "paper", "scissor"]

# Player's name input
player_name = input("Welcome to Tic-Tac-Toe Player What is your Name: ")


def computers_move():
    computer_choice = random.choice(choices)
    return computer_choice


def game():
    # Creating a while loop to check if player's move is in choices
    count = 0
    # Creating point systems
    players_point = 0
    computers_point = 0

    def game_score(player, computer):
        print(f'''
        Current playBoard:
        player: {player}, computer: {computer}
        ''')

    def player_win():
        print(f"Good Job {player_name} that's a win for humanity")

    def computers_win():
        print(f"do not allow humanity to loose {player_name}!!!!!")

    def game_draw():
        print(f"Phew {player_name}, you have bought humanity another life")

    print(f'''
    The Rules Are simple, you choose either rock,paper, or scissor.
    You are up against The evil machine that wants to take over the world,
    the fate of the world lies in this 5 round game, loose and A.I will
    enslave humanity, win and you bought us another year of survival,
    Good Luck {player_name}
    ''')

    while True and count < 5:
        players_move = input("Choose your weapon: ").lower()

        computers_turn = computers_move()

        if players_move in choices:
            # Checking for win cases
            if players_move == choices[0] and computers_turn == choices[2]:
                players_point += 1
                player_win()
                game_score(players_point, computers_point)
            elif players_move == choices[1] and computers_turn == choices[0]:
                players_point += 1
                player_win()
                game_score(players_point, computers_point)
            elif players_move == choices[2] and computers_turn == choices[1]:
                players_point += 1
                player_win()
                game_score(players_point, computers_point)
            # Checking for loose cases
            elif computers_turn == choices[0] and players_move == choices[2]:
                computers_point += 1
                computers_win()
                game_score(players_point, computers_point)
            elif computers_turn == choices[1] and players_move == choices[0]:
                computers_point += 1
                computers_win()
                game_score(players_point, computers_point)
            elif computers_turn == choices[2] and players_move == choices[1]:
                computers_point += 1
                computers_win()
                game_score(players_point, computers_point)
            # Checking for draw Cases
            elif players_move == choices[0] and computers_turn == choices[0]:
                game_draw()
                game_score(players_point, computers_point)
            elif players_move == choices[1] and computers_turn == choices[1]:
                game_draw()
                game_score(players_point, computers_point)
            elif players_move == choices[2] and computers_turn == choices[2]:
                game_draw()
                game_score(players_point, computers_point)
            else:
                print("something went wrong")
            count += 1
        elif players_move not in choices:
            print(f'''
                   You fool, {players_move} is not a weapon,
                   you are going to cause humanity to lose,
                   TRY AGAIN!!!!!
               ''')
    if count == 5 and players_point > computers_point:
        print(f'''
            Good job {player_name}, you have saved humanity this time,
            you are a true warrior, now train even harder for next time
            ''')
    elif count == 5 and players_point < computers_point:
        print(f'''
            It was a long shot but i guess, we never stood a chance,
            do not blame yourself {player_name}, you were humanities best bet.
            ''')
    elif count == 5 and players_point == computers_point:
        print(f'''
            Good job on surviving, but we need to play a rematch for humanities sake...
            ''')


game()
