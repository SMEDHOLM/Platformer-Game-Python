from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsSceneHoverEvent, QPushButton
from PyQt5.QtWidgets import QGraphicsTextItem

#Näppäin, joka palauttaa päävalikkoon

class Back(QGraphicsRectItem, QGraphicsTextItem, QPushButton):
    def __init__(self, text,scene, game):
        super().__init__()
        self.scene = scene
        self.setRect(400,200,200,50)
        self.setBrush(QBrush(QColor(200,0,0)))
        self.game = game

        self.text = QGraphicsTextItem(text)
        self.text.setScale(2)
        self.text.setPos(420, 200)
        self.scene.addItem(self)
        self.scene.addItem(self.text)
        self.setAcceptHoverEvents(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.scene.clear()
            self.game.displayMainMenu()



    def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent'):
        self.setBrush(QBrush(QColor(250, 0, 0)))

    def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent'):
        self.setBrush(QBrush(QColor(200, 0, 0)))


