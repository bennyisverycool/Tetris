class Piece (object):
    row = 20
    col = 10
    def __init__(self, col,row, shape):
        self.x = col
        self.y = row
        self.shape = shape
        self.color = shapes_colors[
            shapes.index(shape)
        ]
        self.rotation = 0
