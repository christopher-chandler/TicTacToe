# Standard
None

# Pip
from colorama import init
from termcolor import colored

# Custom
None


class GameMessageKeys:
    welcome = colored("Welcome to Tic-Tac-Toe", "green")
    player_one_name = "Player 1, what is your name?"
    player_two_name = "Player 2, what is your name?"
    who_starts_game = "Who plays first?"
    chose_player = "Enter the respective number to choose the player"
    not_valid_option = colored("Not a valid option. Please try again.", "red")
    make_move = "make a move"
    not_valid_move = colored("Not a valid move", "red")
    has_won_game = colored(" has won!", "blue")