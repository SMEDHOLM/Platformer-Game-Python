from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem
#Saa parametriksi koordinatit, tason ja aluen
class Door(QGraphicsPixmapItem):
    def __init__(self, x, y, level, scene):
        super().__init__()
        self.scene = scene
        self.level = level
        #Asentaa kuvan
        sprite = QPixmap("images/door.png")
        self.setPixmap(sprite)
        self.x = x
        self.y = y
        self.setPos(self.x, self.y)