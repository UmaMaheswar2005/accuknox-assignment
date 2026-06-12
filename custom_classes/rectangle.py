class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Yields the required dictionary formats in order
        yield {'length': self.length}
        yield {'width': self.width}