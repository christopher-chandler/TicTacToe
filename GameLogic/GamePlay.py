# Standard
import random

# Pip
from colorama import init
from termcolor import colored

# Custom
from BoardLogic.BoardLogic import Board, Player
from GameLogic.GameMessageKeys import GameMessageKeys as GMK


class GamePlay:

    def __init__(self, player_one=False,
                 player_two=False):

        self.player_one = player_one
        self.player_two = player_two

    def getplayerinfo(self):
        # game starts with False for won
        won = False

        # Game Intro
        print(GMK.welcome)
        print(GMK.player_one_name)

        # Player intro
        name1 = input()
        player1 = Player(name1, id=1)
        print(GMK.player_two_name)

        name2 = input()
        player2 = Player(name2, id=-1)
        print(GMK.who_starts_game)

        # List of players
        choice = name1, name2, "Random"
        print(GMK.chose_player)

        for number, player in enumerate(choice, start=1):
            print(f"\t {number} : {player}")

        # Checking player selection
        while True:
            first = input()
            # Only choice between 1 - 3 is allowed
            if first in [str(i) for i in range(len(choice))]:
                break
            else:
                print(GMK.not_valid_option)

        if first == "1":
            first_player = player1
            second_player = player2
        elif first == "2":
            first_player = player2
            second_player = player1
        else:
            # Random player chosen
            randint = random.randint(1, 2)
            if randint == 1:
                first_player = player1
                second_player = player2
            else:
                first_player = player2
                second_player = player1

        self.player_one = first_player
        self.player_two = second_player

    def multiplayer(self):
        first_player = self.player_one
        second_player = self.player_two
        board = Board()

        while True:
            board.display()

            # Player one turn
            print(f"{GMK.make_move}, {first_player.name}:")

            while True:
                row, col, id = first_player.make_move()
                if board.board[row][col].value is None:
                    board.set_field(row, col, id)
                    won = board.has_won(row, col)
                    break
                else:
                    print(GMK.not_valid_move)
            if won:
                board.display()
                print(f"{first_player.name}, {GMK.has_won_game}")
                break

            # Player two turn
            board.display()
            print(f"{GMK.make_move}, {second_player.name}:")

            while True:
                row, col, id = second_player.make_move()
                if board.board[row][col].value is None:
                    board.set_field(row, col, id)
                    won = board.has_won(row, col)
                    break
                else:
                    print(GMK.not_valid_move)
            if won:
                board.display()
                print(f"{second_player.name},{GMK.has_won_game}")


