from PyQt5.QtCore import  QUrl
from PyQt5.QtGui import QBrush, QColor, QPixmap
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import  QGraphicsTextItem
from PyQt5.Qt import Qt

from PyQt5.QtWidgets import QGraphicsPixmapItem
from  PyQt5 import QtCore

from PyQt5.QtGui import QTransform

from exit import EXIT
from back import Back

from restart import RESTART


class Player(QGraphicsPixmapItem):
    def __init__(self, scene_width, scene_height, level, scene):
        super().__init__()
        self.scene = scene
        self.scene_height = scene_height
        self.level = level
#Oikealle liikkuva kuva
        self.rsprite = QPixmap("images/ghost.png")
        self.trans = QTransform()
#Vasemmallle liikkuva kuva
        self.lsprite = self.rsprite.transformed(self.trans.scale(-1, 1))
        self.setPixmap(self.rsprite)

        self.dx =0
        self.dy = 0
#Asentaa pelajan paikalle
        self.x = self.level.player_x_location
        self.y = self.level.player_y_location
        self.setPos(self.x, self.y)
#Ajastin sijainnin päivittämiseen
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Update)
        self.timer.start(50)  # Milliseconds

        self.jump_sound = QMediaPlayer()
        self.jump_sound.setMedia(QMediaContent(QUrl("music/Jump.mp3")))
# Ajastin ajan päivittämiseen päivittämiseen
        self.g_timer = QtCore.QTimer()
        self.g_timer.timeout.connect(self.Update_TIME)
        self.g_timer.start(1)  # Milliseconds
        self.time = 0

# Pelajan ohjaminen
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.dx += 6
            self.setPixmap(self.rsprite)
            if self.dx > 12:
                self.dx = 12
        elif event.key() == Qt.Key_A:
            self.dx -= 6
            self.setPixmap(self.lsprite)
            if self.dx < -12:
                self.dx = -12
        elif event.key() == Qt.Key_W and self.OnGround():
            if self.jump_sound.state() == QMediaPlayer.PlayingState:
                self.jump_sound.stop()
            self.jump_sound.play()
            self.dy -= 16
            if self.dy < -16:
                self.dy = - 16

#Päivittää pelajan sijantia
    def Update(self):
        self.setFocus()
        if not self.OnGround():
            self.dy += 2
        self.CollisionY(), self.CollisionX()
        self.Collision_with_objects()

        if self.OnGround() and self.dy > 0:
            self.dy = 0

        if self.y + self.dy > self.scene_height - 32:
            self.dy = 0
            self.y = self.scene_height - 32
        self.move()
        self.setPos(self.x, self.y)
#Törmykset X suunnassa
    def CollisionX(self):
        i = int(self.y / 32)
        j = int(self.x / 32)
        while i < (self.y + 32) / 32:
            while j < (self.x + 32) / 32:
                if self.level.title_map[i][j] == "B":
                    if self.dx < 0:
                        self.dx =0
                        self.x = (j + 1)*32
                    if self.dx > 0:
                        self.dx = 0
                        self.x = (j -1)*32

                j += 1
            i += 1

    # Törmykset Y suunnassa
    def CollisionY(self):
        i = int(self.y / 32)
        j = int(self.x / 32)
        z = int((self.x + 20) / 32)
        while i < (self.y + 32) / 32:
            while j < (self.x + 32) / 32:
                if self.level.title_map[i][j] == "B":
                    if self.dy < 0:
                        self.y = i * 32 + 32
                        self.dy = 0
                if self.level.title_map[i][z] == "B":
                    if self.dy < 0:
                        self.y = i * 32 + 32
                        self.dy = 0

                j += 1
            i += 1
#Tarkista, ono pelaja pinnalla
    def OnGround(self):
        i = int(self.y / 32)
        j = int(self.x / 32)
        z = int((self.x + 20)/32)
        if self.level.title_map[i+1][j] == "B":
            self.y = i * 32
            return True
        if self.level.title_map[i+1][z] == "B":
            self.y = i * 32
            return True
        else:
            return False
#Liikutta pelajaa
    def move(self):
        self.x += self.dx
        self.y+= self.dy
#Tarkistaa objektit, jotka ovat kosketuksessa pelajaan
    def Collision_with_objects(self):
        for enemy in self.level.enemies:
            #Hirviö tappaminen, kun pelaja on ylempi
            if enemy in self.collidingItems() and self.y < enemy.y:
                #Hirviö huutaa
                if enemy.scream.state() == QMediaPlayer.PlayingState:
                    enemy.scream.stop()
                enemy.scream.play()
                # Käynistää hypyn ääniä
                if self.jump_sound.state() == QMediaPlayer.PlayingState:
                    self.jump_sound.stop()
                self.jump_sound.play()

                self.dy -= 27
                if self.dy < -27:
                    self.dy = - 27
                self.y += self.dy
                self.scene.removeItem(enemy)
                #Poistaa pelajan ja käynistä kuoleman funktion
            elif enemy in self.collidingItems() and self.y >= enemy.y:
                self.scene.removeItem(self)
                self.DIED()
        #Tarksitaa, onko pelaja kosketuksessa lavan kanssa
        for lava in self.level.lavas:
            if lava in self.collidingItems():
                self.scene.removeItem(self)
                self.DIED()
        # Tarksitaa, onko pelaja kosketuksessa oven kanssa
        for door in self.level.door:
            if door in self.collidingItems():
                self.scene.removeItem(self)
                self.WON()
#Piirrtää valikkon, jos pelaja kuollut
    def DIED(self):
        self.scene.clear()
        LOSE = QGraphicsTextItem("YOU ARE DEAD")
        LOSE.setScale(5)
        LOSE.setPos(350, 50)
        self.scene.addItem(LOSE)
        self.scene.setBackgroundBrush(QBrush(QColor(100, 0, 0)))
        self.restart_button = RESTART("RESTART", self.scene, self.level.file, self.level.game)
        self.back_button = Back("BACK", self.scene, self.level.game)

        self.exit_button = EXIT("EXIT", self.scene)

    # Piirrtää valikkon, jos pelaja kosketuksessa oveen
    def WON(self):
        self.scene.clear()
        text = QGraphicsTextItem("YOU WON")
        self.g_timer.stop()
        result = self.Check_ScoreBoard()
        if result != None:
            self.Change_Score_Board(result)
            text = QGraphicsTextItem("NEW RECORD:"+ str(self.time) + "ms")
        text.setScale(5)
        text.setPos(350, 50)
        self.scene.addItem(text)
        self.scene.setBackgroundBrush(QBrush(QColor(100, 0, 0)))
        self.restart_button = RESTART("RESTART", self.scene, self.level.file, self.level.game)
        self.back_button = Back("BACK", self.scene, self.level.game)
        self.exit_button = EXIT("EXIT", self.scene)





#Piirtää aikaa
    def Update_TIME(self):
        try:
            self.scene.removeItem(self.stime)
        except:
            pass
        self.time += 1
        self.stime = QGraphicsTextItem(str(self.time))
        self.stime.setScale(3)
        self.stime.setPos(0, 0)
        self.scene.addItem(self.stime)
# Tarkistaa, oliko tehtty uusi ennätys
    def Check_ScoreBoard(self):

        scoreboard_list = open("SCOREBOARD").read().splitlines()
        i = scoreboard_list.index(self.level.file)
        if int(scoreboard_list[i+3]) > self.time:
            if int(scoreboard_list[i+2]) > self.time:
                if int(scoreboard_list[i+1]) > self.time:
                    return i+1
                else:
                    return i+2
            else:
                return i+3
        else:
            return None
# Vaihtaa, ennätyksen tideostossa
    def Change_Score_Board(self, index):
        scoreboard_list = open("SCOREBOARD").read().splitlines()
        scoreboard_list[index] = str(self.time)
        file = open("SCOREBOARD", "w")
        for element in scoreboard_list:
            file.write(element + "\n")
        file.close()







