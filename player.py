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
# Sprite for moving right
        self.rsprite = QPixmap("images/ghost.png")
        self.trans = QTransform()
# Sprite for moving left
        self.lsprite = self.rsprite.transformed(self.trans.scale(-1, 1))
        self.setPixmap(self.rsprite)

        self.dx =0
        self.dy = 0
# Set the player's starting position
        self.x = self.level.player_x_location
        self.y = self.level.player_y_location
        self.setPos(self.x, self.y)
# Timer for updating position
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Update)
        self.timer.start(50)  # Milliseconds

        self.jump_sound = QMediaPlayer()
        self.jump_sound.setMedia(QMediaContent(QUrl("music/Jump.mp3")))
# Timer for updating elapsed time
        self.g_timer = QtCore.QTimer()
        self.g_timer.timeout.connect(self.Update_TIME)
        self.g_timer.start(1)  # Milliseconds
        self.time = 0

# Player input handling
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

# Updates the player's position
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
# Collision handling in the X direction
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

    # Collision handling in the Y direction
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
# Check whether the player is standing on solid ground
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
# Move the player according to current velocity
    def move(self):
        self.x += self.dx
        self.y+= self.dy
# Checks objects that are colliding with the player
    def Collision_with_objects(self):
        for enemy in self.level.enemies:
            # Enemy defeat when the player lands above it
            if enemy in self.collidingItems() and self.y < enemy.y:
                # Play enemy scream sound
                if enemy.scream.state() == QMediaPlayer.PlayingState:
                    enemy.scream.stop()
                enemy.scream.play()
                # Trigger the jump sound effect
                if self.jump_sound.state() == QMediaPlayer.PlayingState:
                    self.jump_sound.stop()
                self.jump_sound.play()

                self.dy -= 27
                if self.dy < -27:
                    self.dy = - 27
                self.y += self.dy
                self.scene.removeItem(enemy)
                # Remove the player and trigger the death sequence
            elif enemy in self.collidingItems() and self.y >= enemy.y:
                self.scene.removeItem(self)
                self.DIED()
        # Check whether the player is colliding with lava
        for lava in self.level.lavas:
            if lava in self.collidingItems():
                self.scene.removeItem(self)
                self.DIED()
        # Check whether the player is colliding with the door
        for door in self.level.door:
            if door in self.collidingItems():
                self.scene.removeItem(self)
                self.WON()
# Draw the menu shown when the player dies
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

    # Draw the menu shown when the player reaches the door
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





# Render the elapsed time on screen
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
# Check whether the player achieved a new high score
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
# Update the scoreboard with a new record time
    def Change_Score_Board(self, index):
        scoreboard_list = open("SCOREBOARD").read().splitlines()
        scoreboard_list[index] = str(self.time)
        file = open("SCOREBOARD", "w")
        for element in scoreboard_list:
            file.write(element + "\n")
        file.close()







