from ship import Ship


class Fleet:
    def __init__(self):
        self.ships = []
        
        ship1 = Ship("Destroyer", 2)
        ship2 = Ship("Submarine", 3)
        ship3 = Ship("Battleship", 4)
        ship4 = Ship("Aircraft Carrier", 5)

        self.ships.append(ship1)
        self.ships.append(ship2)
        self.ships.append(ship3)
        self.ships.append(ship4)