class PawnClass:
    def __init__(self, x_loc, y_loc, colour, captured=False):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.colour = colour
        self.captured = captured

class KnightClass:
    def __init__(self, x_loc, y_loc, colour, captured=False):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.colour = colour
        self.captured = captured

class BishopClass:
    def __init__(self, x_loc, y_loc, colour, captured=False):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.colour = colour
        self.captured = captured

class RookClass:
    def __init__(self, x_loc, y_loc, colour, captured=False):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.colour = colour
        self.captured = captured

class QueenClass:
    def __init__(self, x_loc, y_loc, colour, captured=False):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.colour = colour
        self.captured = captured

class KingClass:
    def __init__(self, x_loc, y_loc, colour, can_castle=True):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.colour = colour
        self.can_castle = can_castle