from fleet import Fleet
from board import Board


class Player:
    def __init__(self, name = None):
        self.name = name
        self.board = Board()
        self.fleet = Fleet()

    def player_set(self):
        for i in self.board.player_coordinates:
            print(" ".join(i))

        for ship in self.fleet.ships:
            z = 0
            while z < ship.size:
                 y = int(input(f"Input the row coordinates of part {z + 1} of the {ship.name}(1 - 20): "))
                 x = int(input(f"Input the column coordinates of part {z + 1} of the {ship.name}(1 - 20): "))
                 self.board.player_coordinates[y - 1][x - 1] = 'X'
                 z += 1
                 for i in self.board.player_coordinates:
                    print(" ".join(i))
            
            

    def player_attack(self):
        y = int(input(f"Input the row coordinates you wish to attack(1 - 20): "))
        x = int(input(f"Input the column coordinates you wish to attack(1 - 20): "))
        return y, x


    def print_board(self):
        for i in self.board.grid:
            print(" ".join(i))