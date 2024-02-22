# Creating a Tic-Tac-Toe game
import random

# List for our game choices
choices = ["rock", "paper", "scissor"]

# Player's name input
player_name = input("Welcome to Tic-Tac-Toe Player What is your Name: ")


def computers_move():
    computer_choice = random.choice(choices)
    return computer_choice


def game_score(player, computer):
    score_board = print(f'''
    Current playBoard:
    player: {player}, computer: {computer}
    ''')
    return score_board


def game():
    print(f'''
    The Rules Are simple, you choose either rock,paper, or scissor.
    You are up against The evil machine that wants to take over the world,
    the fate of the world lies in this 5 round game, loose and A.I will
    enslave humanity, win and you bought us another year of survival,
    Good Luck {player_name}
    ''')

    # Creating a while loop to check if player's move is in choices
    count = 0
    # Creating point systems
    players_point = 0
    computers_point = 0
    while True and count < 5:
        players_move = input("Choose your weapon: ").lower()

        computers_turn = computers_move()

        if players_move in choices:
            # Checking for win cases
            if players_move == choices[0] and computers_turn == choices[2]:
                players_point += 1
                print(f"Good Job {player_name} that's a win for humanity")
                game_score(players_point, computers_point)
            elif players_move == choices[1] and computers_turn == choices[0]:
                players_point += 1
                print(f"Good Job {player_name} that's a win for humanity")
                game_score(players_point, computers_point)
            elif players_move == choices[2] and computers_turn == choices[1]:
                players_point += 1
                print(f"Good Job {player_name} that's a win for humanity")
                game_score(players_point, computers_point)
            # Checking for loose cases
            elif computers_turn == choices[0] and players_move == choices[2]:
                computers_point += 1
                print(f"do not allow humanity to loose {player_name}!!!!!")
                game_score(players_point, computers_point)
            elif computers_turn == choices[1] and players_move == choices[0]:
                computers_point += 1
                print(f"do not allow humanity to loose {player_name}!!!!!")
                game_score(players_point, computers_point)
            elif computers_turn == choices[2] and players_move == choices[1]:
                computers_point += 1
                game_score(players_point, computers_point)
                print(f"do not allow humanity to loose {player_name}!!!!!")
            # Checking for draw Cases
            elif players_move == choices[0] and computers_turn == choices[0]:
                print(f"Phew {player_name}, you have bought humanity another life")
                game_score(players_point, computers_point)
            elif players_move == choices[1] and computers_turn == choices[1]:
                print(f"Phew {player_name}, you have bought humanity another life")
                game_score(players_point, computers_point)
            elif players_move == choices[2] and computers_turn == choices[2]:
                print(f"Phew {player_name}, you have bought humanity another life")
                game_score(players_point, computers_point)
            else:
                print("something went wrong")

            count += 1
        else:
            print(f'''
                   You fool, {players_move} is not a weapon,
                   you are going to cause humanity to lose,
                   TRY AGAIN!!!!!
               ''')


game()
