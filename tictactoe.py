import random
import time


class Board:

    def __init__(self):
        self.placeholder = [" " for _ in range(9)]
        self.players = 0
        self.winner = False

    def print(self):
        print(f" {self.placeholder[0]} | {self.placeholder[1]} | {self.placeholder[2]}")
        print("-----------")
        print(f" {self.placeholder[3]} | {self.placeholder[4]} | {self.placeholder[5]}")
        print("-----------")
        print(f" {self.placeholder[6]} | {self.placeholder[7]} | {self.placeholder[8]}")
        print("\n")

    def setup(self):
        print("Are you gonna play versus PC (1) or versus second player (2) or you will watch (0): ")
        self.players = int(input())
        print("Positions:")
        print(" 1 | 2 | 3")
        print("-----------")
        print(" 4 | 5 | 6")
        print("-----------")
        print(" 7 | 8 | 9")
        print("\n")

    def pick_place_player_1(self):
        print("Pick a number between 1 and 9: ")
        picked_place = int(input()) - 1
        if not self.check_picked_pos(picked_place):
            print("Not valid position!")
        else:
            self.placeholder[picked_place] = "1"

    def pick_place_player_2(self):
        print("Pick a number between 1 and 9: ")
        picked_place = int(input()) - 1
        if not self.check_picked_pos(picked_place):
            print("Not valid position!")
        else:
            self.placeholder[picked_place] = "0"

    def winner_check(self):
        for i in range(3):  # Looks the horizontal
            if self.placeholder[i] == "1" and self.placeholder[i + 1] == "1" and self.placeholder[i + 2] == "1":
                self.winner = True
                print("Player 1 wins")
                return self.winner
            if self.placeholder[i] == "0" and self.placeholder[i + 1] == "0" and self.placeholder[i + 2] == "0":
                self.winner = True
                print("Player 2 wins")
                return self.winner

        for i in range(3):  # Vertical check
            if self.placeholder[i] == "1" and self.placeholder[i + 3] == "1" and self.placeholder[i + 6] == "1":
                self.winner = True
                print("Player 1 wins")
                return self.winner
            if self.placeholder[i] == "0" and self.placeholder[i + 3] == "0" and self.placeholder[i + 6] == "0":
                self.winner = True
                print("Player 2 wins")
                return self.winner

        if self.placeholder[0] == "1" and self.placeholder[4] == "1" and self.placeholder[8] == "1":
            self.winner = True
            print("Player 1 wins")
            return self.winner

        if self.placeholder[2] == "1" and self.placeholder[4] == "1" and self.placeholder[6] == "1":
            self.winner = True
            print("Player 1 wins")
            return self.winner

        if self.placeholder[0] == "0" and self.placeholder[4] == "0" and self.placeholder[8] == "0":
            self.winner = True
            print("Player 2 wins")
            return self.winner

        if self.placeholder[2] == "0" and self.placeholder[4] == "0" and self.placeholder[6] == "0":
            self.winner = True
            print("Player 2 wins")
            return self.winner

        return self.winner

    def pc_pick(self):
        placed = False
        if self.players == 1:  # Vertical
            for i in range(3, 6):
                down = self.placeholder[i + 3]
                up = self.placeholder[i - 3]
                center = self.placeholder[i]

                if (up == "1" and down == "1") or (up == "0" and down == "0"):
                    if self.check_picked_pos(i):
                        self.placeholder[i] = "0"
                        placed = True
                        break

                if (center == "1" and down == "1") or (center == "0" and down == "0"):
                    if self.check_picked_pos(i + 3):
                        self.placeholder[i + 3] = "0"
                        placed = True
                        break
                if (up == "1" and center == "1") or (up == "0" and center == "0"):
                    if self.check_picked_pos(i - 3):
                        self.placeholder[i - 3] = "0"
                        placed = True
                        break
            else:
                for i in range(1, 8, 3):  # Horizontal
                    left = self.placeholder[i - 1]
                    right = self.placeholder[i + 1]
                    center = self.placeholder[i]

                    if (right == "1" and left == "1") or (right == "0" and left == "0"):
                        if self.check_picked_pos(i):
                            self.placeholder[i] = "0"
                            placed = True
                            break
                    if (center == "1" and left == "1") or (center == "0" and left == "0"):
                        if self.check_picked_pos(i + 1):
                            self.placeholder[i + 1] = "0"
                            placed = True
                            break
                    if (right == "1" and center == "1") or (right == "0" and center == "0"):
                        if self.check_picked_pos(i - 1):
                            self.placeholder[i - 1] = "0"
                            placed = True
                            break
                else:  # Diagonals
                    if self.placeholder[4] == "1" and self.placeholder[0] == "1":
                        if self.check_picked_pos(8):
                            self.placeholder[8] = "0"
                            placed = True
                    if self.placeholder[4] == "0" and self.placeholder[0] == "0":
                        if self.check_picked_pos(8):
                            self.placeholder[8] = "0"
                            placed = True
                    if self.placeholder[4] == "1" and self.placeholder[6] == "1":
                        if self.check_picked_pos(2):
                            self.placeholder[2] = "0"
                            placed = True
                    if self.placeholder[4] == "0" and self.placeholder[6] == "0":
                        if self.check_picked_pos(2):
                            self.placeholder[2] = "0"
                            placed = True
                    if self.placeholder[4] == "1" and self.placeholder[8] == "1":
                        if self.check_picked_pos(0):
                            self.placeholder[0] = "0"
                            placed = True
                    if self.placeholder[4] == "0" and self.placeholder[8] == "0":
                        if self.check_picked_pos(0):
                            self.placeholder[0] = "0"
                            placed = True
                    if self.placeholder[4] == "1" and self.placeholder[2] == "1":
                        if self.check_picked_pos(6):
                            self.placeholder[6] = "0"
                            placed = True
                    if self.placeholder[4] == "0" and self.placeholder[2] == "0":
                        if self.check_picked_pos(6):
                            self.placeholder[6] = "0"
                            placed = True

                    if self.placeholder[0] == "1" and self.placeholder[8] == "1":
                        if self.check_picked_pos(4):
                            self.placeholder[4] = "0"
                            placed = True
                    if self.placeholder[0] == "0" and self.placeholder[8] == "0":
                        if self.check_picked_pos(4):
                            self.placeholder[4] = "0"
                            placed = True
                    if self.placeholder[6] == "1" and self.placeholder[2] == "10":
                        if self.check_picked_pos(4):
                            self.placeholder[4] = "0"
                            placed = True
                    if self.placeholder[6] == "0" and self.placeholder[2] == "0":
                        if self.check_picked_pos(4):
                            self.placeholder[4] = "0"
                            placed = True
            if not placed:
                index_list = self.rand_choice()
                pick = random.choice(index_list)
                self.placeholder[pick] = "0"

    def pc_pick_2(self):
        placed = False
        for i in range(3, 6):  # Vertical check
            down = self.placeholder[i + 3]
            up = self.placeholder[i - 3]
            center = self.placeholder[i]

            if (up == "1" and down == "1") or (up == "0" and down == "0"):
                if self.check_picked_pos(i):
                    self.placeholder[i] = "0"
                    placed = True
                    break

            if (center == "1" and down == "1") or (center == "0" and down == "0"):
                if self.check_picked_pos(i + 3):
                    self.placeholder[i + 3] = "0"
                    placed = True
                    break
            if (up == "1" and center == "1") or (up == "0" and center == "0"):
                if self.check_picked_pos(i - 3):
                    self.placeholder[i - 3] = "0"
                    placed = True
                    break
        else:
            for i in range(1, 8, 3):  # Horizontal check
                left = self.placeholder[i - 1]
                right = self.placeholder[i + 1]
                center = self.placeholder[i]

                if (right == "1" and left == "1") or (right == "0" and left == "0"):
                    if self.check_picked_pos(i):
                        self.placeholder[i] = "0"
                        placed = True
                        break
                if (center == "1" and left == "1") or (center == "0" and left == "0"):
                    if self.check_picked_pos(i + 1):
                        self.placeholder[i + 1] = "0"
                        placed = True
                        break
                if (right == "1" and center == "1") or (right == "0" and center == "0"):
                    if self.check_picked_pos(i - 1):
                        self.placeholder[i - 1] = "0"
                        placed = True
                        break
            else:  # Diagonals

                if self.placeholder[4] == "1" and self.placeholder[0] == "1":
                    if self.check_picked_pos(8):
                        self.placeholder[8] = "0"
                        placed = True
                if self.placeholder[4] == "0" and self.placeholder[0] == "0":
                    if self.check_picked_pos(8):
                        self.placeholder[8] = "0"
                        placed = True
                if self.placeholder[4] == "1" and self.placeholder[6] == "1":
                    if self.check_picked_pos(2):
                        self.placeholder[2] = "0"
                        placed = True
                if self.placeholder[4] == "0" and self.placeholder[6] == "0":
                    if self.check_picked_pos(2):
                        self.placeholder[2] = "0"
                        placed = True
                if self.placeholder[4] == "1" and self.placeholder[8] == "1":
                    if self.check_picked_pos(0):
                        self.placeholder[0] = "0"
                        placed = True
                if self.placeholder[4] == "0" and self.placeholder[8] == "0":
                    if self.check_picked_pos(0):
                        self.placeholder[0] = "0"
                        placed = True
                if self.placeholder[4] == "1" and self.placeholder[2] == "1":
                    if self.check_picked_pos(6):
                        self.placeholder[6] = "0"
                        placed = True
                if self.placeholder[4] == "0" and self.placeholder[2] == "0":
                    if self.check_picked_pos(6):
                        self.placeholder[6] = "0"
                        placed = True

                if self.placeholder[0] == "1" and self.placeholder[8] == "1":
                    if self.check_picked_pos(4):
                        self.placeholder[4] = "0"
                        placed = True
                if self.placeholder[0] == "0" and self.placeholder[8] == "0":
                    if self.check_picked_pos(4):
                        self.placeholder[4] = "0"
                        placed = True
                if self.placeholder[6] == "1" and self.placeholder[2] == "10":
                    if self.check_picked_pos(4):
                        self.placeholder[4] = "0"
                        placed = True
                if self.placeholder[6] == "0" and self.placeholder[2] == "0":
                    if self.check_picked_pos(4):
                        self.placeholder[4] = "0"
                        placed = True
        if not placed:
            index_list = self.rand_choice()
            pick = random.choice(index_list)
            self.placeholder[pick] = "0"

    def pc_pick_1(self):
        placed = False
        for i in range(3, 6):
            down = self.placeholder[i + 3]
            up = self.placeholder[i - 3]
            center = self.placeholder[i]

            if (up == "1" and down == "1") or (up == "0" and down == "0"):
                if self.check_picked_pos(i):
                    self.placeholder[i] = "1"
                    placed = True
                    break

            if (center == "1" and down == "1") or (center == "0" and down == "0"):
                if self.check_picked_pos(i + 3):
                    self.placeholder[i + 3] = "1"
                    placed = True
                    break
            if (up == "1" and center == "1") or (up == "0" and center == "0"):
                if self.check_picked_pos(i - 3):
                    self.placeholder[i - 3] = "1"
                    placed = True
                    break
        else:
            for i in range(1, 8, 3):
                left = self.placeholder[i - 1]
                right = self.placeholder[i + 1]
                center = self.placeholder[i]

                if (right == "1" and left == "1") or (right == "0" and left == "0"):
                    if self.check_picked_pos(i):
                        self.placeholder[i] = "1"
                        placed = True
                        break
                if (center == "1" and left == "1") or (center == "0" and left == "0"):
                    if self.check_picked_pos(i + 1):
                        self.placeholder[i + 1] = "1"
                        placed = True
                        break
                if (right == "1" and center == "1") or (right == "0" and center == "0"):
                    if self.check_picked_pos(i - 1):
                        self.placeholder[i - 1] = "1"
                        placed = True
                        break
            else:
                if self.placeholder[4] == "1":
                    if self.placeholder[0] == "1":
                        if self.check_picked_pos(8):
                            self.placeholder[8] = "1"
                            placed = True
                    if self.placeholder[6] == "1":
                        if self.check_picked_pos(8):
                            self.placeholder[8] = "1"
                            placed = True
                    if self.placeholder[8] == "1":
                        if self.check_picked_pos(8):
                            self.placeholder[8] = "1"
                            placed = True
                    if self.placeholder[2] == "1":
                        if self.check_picked_pos(8):
                            self.placeholder[8] = "1"
                            placed = True

                if self.placeholder[4] == "0":
                    if self.placeholder[0] == "0":
                        if self.check_picked_pos(8):
                            self.placeholder[8] = "1"
                            placed = True
                    if self.placeholder[6] == "0":
                        if self.check_picked_pos(8):
                            self.placeholder[8] = "1"
                            placed = True
                    if self.placeholder[8] == "0":
                        if self.check_picked_pos(8):
                            self.placeholder[8] = "1"
                            placed = True
                    if self.placeholder[2] == "0":
                        if self.check_picked_pos(8):
                            self.placeholder[8] = "1"
                            placed = True

                if self.placeholder[0] == "1" and self.placeholder[8] == "1":
                    if self.check_picked_pos(4):
                        self.placeholder[4] = "1"
                        placed = True
                if self.placeholder[0] == "0" and self.placeholder[8] == "0":
                    if self.check_picked_pos(4):
                        self.placeholder[4] = "1"
                        placed = True
                if self.placeholder[6] == "1" and self.placeholder[2] == "10":
                    if self.check_picked_pos(4):
                        self.placeholder[4] = "1"
                        placed = True
                if self.placeholder[6] == "0" and self.placeholder[2] == "0":
                    if self.check_picked_pos(4):
                        self.placeholder[4] = "1"
                        placed = True
        if not placed:
            index_list = self.rand_choice()
            pick = random.choice(index_list)
            self.placeholder[pick] = "1"

    def rand_choice(self):
        index_list = []
        for i in range(9):
            if self.placeholder[i] == " ":
                index_list.append(i)

        return index_list

    def check_picked_pos(self, pick):
        if not 9 > pick >= 0:
            return False

        if self.placeholder[pick] == "1" or self.placeholder[pick] == "0":
            return False
        else:
            return True

    def get_player(self):
        return self.players


print("Welcome to TicTacToe game!\n")
game = Board()
game.setup()

if game.get_player() == 0:
    while 1:
        game.print()
        time.sleep(3)
        if game.winner_check():
            break
        game.pc_pick_1()
        game.print()
        time.sleep(3)
        if game.winner_check():
            break
        game.pc_pick_2()

if game.get_player() == 1:
    while 1:
        game.print()
        if game.winner_check():
            break
        game.pick_place_player_1()
        game.print()
        if game.winner_check():
            break
        print("PC picks")
        game.pc_pick()

if game.get_player() == 2:
    while not game.winner_check():
        game.print()
        game.pick_place_player_1()
        game.print()
        if game.winner_check():
            break
        game.pick_place_player_2()
