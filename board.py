class Board:
    def __init__(self):
        self.grid = []

        for i in range(20):
            self.grid.append(['?'] * 20)

        self.player_coordinates = self.grid
            