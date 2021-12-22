class Piece:
    def __init__(self, x_loc, y_loc, colour, piece_type, captured=False):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.colour = colour
        self.piece_type = piece_type
        self.captured = captured