from color import Color
class Light:
    """ Point light source of a color"""

    def __init__(self, position, color = Color.from_hex("#FFFFFF")):
        self.position = position
        self.color = color
