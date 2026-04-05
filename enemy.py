from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem
from  PyQt5 import QtCore
from  PyQt5.QtCore import QElapsedTimer
from PyQt5.QtGui import QTransform
from PyQt5.QtCore import QUrl

# Creates an enemy
class Enemy(QGraphicsPixmapItem):
    def __init__(self, x, y, level, scene):
        super().__init__()
        self.scene = scene
        self.level = level
        self.scream = QMediaPlayer()
        # Attach a scream sound to the enemy
        self.scream.setMedia(QMediaContent(QUrl("music/Monster Scream.mp3")))

        self.sprite = QPixmap("images/monster.png")
        # Coordinate velocity changes
        self.dx = 2
        self.dy = 0
        self.on_ground = True
        # Set the enemy image
        self.setPixmap(self.sprite)
        self.x = x
        self.y = y

        # Timer that triggers the update function
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updatePosition)
        self.timer.start(50)  # Milliseconds



# Updates the enemy position on the scene
    def updatePosition(self):
        self.x += self.dx
        self.Collision()
        self.setPixmap(self.sprite)
        self.setPos(self.x, self.y)
# Checks collisions. On contact, mirror the sprite and reverse direction
    def Collision(self):
        i = int(self.y / 32)
        j = int(self.x /32)
        while i < (self.y + 64) // 32:
            while j < (self.x + 64) // 32:
                if self.level.title_map[i][j] == "B":
                    if self.dx > 0:
                        self.x = (j - 1) * 32
                        self.dx *= -1
                        trans = QTransform()
                        self.sprite = self.sprite.transformed(trans.scale(-1, 1))
                    elif self.dx < 0:
                        self.x = j * 32 + 32
                        self.dx *= -1
                        trans = QTransform()
                        self.sprite = self.sprite.transformed(trans.scale(-1, 1))
                j += 1
            i += 1

