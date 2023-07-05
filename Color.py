class Colors:
    Cells = (0, 91, 150)
    green = (89, 209, 2)
    red = (249,65,68)
    orange = (255, 140, 0)
    yellow = (175, 252, 175)
    purple = (188, 0, 221)
    lime = (255, 237, 0)
    blue = (0, 255, 208)
    white = (255, 255, 255)
    black = (0, 0, 0)
    backGround = (1, 31, 75)
    boxes = (3, 57, 108)

    @classmethod
    def getCellColors(cls):
        return [cls.Cells, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.lime, cls.blue]