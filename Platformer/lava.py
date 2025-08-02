from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem
#Lava, joka ei tee mitään
class Lava(QGraphicsPixmapItem):
    def __init__(self, x, y, level, scene):
        super().__init__()
        self.scene = scene
        self.level = level
        sprite = QPixmap("images/lava.png")
        self.setPixmap(sprite)
        self.x = x
        self.y = y + 16
        self.setPos(self.x, self.y)