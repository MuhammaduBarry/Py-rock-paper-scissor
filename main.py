# Creating a Tic-Tac-Toe game

# List for our game choices
choices = ["rock", "paper", "scissor", "r", "p", "s"]

# Player's name input
player_name = input("Welcome to Tic-Tac-Toe Player What is your Name: ")


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
    while True and count < 5:
        players_move = input("Choose your weapon: ").lower()
        if players_move in choices:
            print(f"Good job {player_name}! {players_move} is a valid weapon.")
            count += 1
        else:
            print(f'''
                   You fool, {players_move} is not a weapon,
                   you are going to cause humanity to lose,
                   TRY AGAIN!!!!!
               ''')


game()
