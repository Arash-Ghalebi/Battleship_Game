from player import Player


class Battlefield:
    def __init__(self):
        self.player_1 = Player()
        self.player_2 = Player()

    def run_game(self):
        z = True
        player1_counter = 0
        player2_counter = 0
        self.welcome()
        self.get_name()
        self.display_rules()
        
        self.player_1.player_set()
        self.player_2.player_set()

        while z is True:
            print(f"{self.player_1.name} - It is your turn.")
            y, x = self.player_1.player_attack()
            if self.player_2.board.player_coordinates[y - 1][x - 1] == 'X':
                self.player_1.board.grid[y - 1][x - 1] = 'X'
                player1_counter += 1
                for i in self.player_1.board.grid:
                    print(" ".join(i))
                print("Hit!\n")
            else:
                self.player_1.board.grid[y - 1][x - 1] = 'O'
                for i in self.player_1.board.grid:
                    print(" ".join(i))
                print("Miss.\n")
            
            if player1_counter == 14:
                print(f"The winner is {self.player_1.name}!")
                break

            print(f"{self.player_2.name} - It is your turn.")
            y, x = self.player_2.player_attack()
            if self.player_1.board.player_coordinates[y - 1][x - 1] == 'X':
                self.player_2.board.grid[y - 1][x - 1] = 'X'
                player2_counter += 1
                for i in self.player_2.board.grid:
                    print(" ".join(i))
                print("Hit!\n")
            else:
                self.player_2.board.grid[y - 1][x - 1] = 'O'
                for i in self.player_2.board.grid:
                    print(" ".join(i))
                print("Miss.\n")

            if player2_counter == 14:
                break

        



    def welcome(self):
        print("--- Welcome to Battleship! ---\n")

        print("Place your units on your board. Players take turns attacking each other's ships. First to sink the other's fleet wins!\n")

    def get_name(self):
        self.player_1.name = input("Player 1 - Please input your name: ")
        self.player_2.name = input("Player 2 - Please input your name: ")

    def display_rules(self):
        print("\nEach player has the following ships:\n1. Destroyer - Size: 2\n2. Submarine  - Size: 3\n3. Battleship - Size: 4\n4. Aircraft Carrier - Size: 5\n")
        print("To begin placing ships on your board, input the coordinates of the row and column you want the front of the ship to be placed.\n")
        print("For example, to place the front of the ship on row 13 - column 5, simply input '13' and '5' when prompted. Then do the same for the rest of the ship size until your entire fleet is placed.\n")
