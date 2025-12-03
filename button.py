from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsSceneHoverEvent, QPushButton
from PyQt5.QtWidgets import QGraphicsTextItem

#Saa parametriksi tekstin, aluen, nappäin ja tekstin koordinatit ja tekstin kokon
class Button(QGraphicsRectItem, QGraphicsTextItem, QPushButton):
    def __init__(self, text, scene, x, y, tx,ty, scale):
        super().__init__()
        self._clicked = False

        self.scene = scene
        self.setRect(x, y, 200, 50)
        self.setBrush(QBrush(QColor(200, 0, 0)))

        self.text = QGraphicsTextItem(text)
        self.text.setScale(scale)
        self.text.setPos(tx, ty)
        self.scene.addItem(self)
        self.scene.addItem(self.text)

        self.setAcceptHoverEvents(True)
#Kun nappäintä painataan vasemalla hiirennäppäimella, vaihtaa muuttujan arvoa
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._clicked = True


#Kun kohdistin saapuu näppäimeen, vaihtaa sen väriä
    def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent'):
        self.setBrush(QBrush(QColor(250,0,0)))

 # Kun kohdistin poistuu näppäimesta, vaihtaa sen väriä alkuperäiseen
    def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent'):
        self.setBrush(QBrush(QColor(200,0,0)))

