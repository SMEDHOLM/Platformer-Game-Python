from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem
# Receives coordinates, the current level, and the scene
class Door(QGraphicsPixmapItem):
    def __init__(self, x, y, level, scene):
        super().__init__()
        self.scene = scene
        self.level = level
        # Load the door image
        sprite = QPixmap("images/door.png")
        self.setPixmap(sprite)
        self.x = x
        self.y = y
        self.setPos(self.x, self.y)