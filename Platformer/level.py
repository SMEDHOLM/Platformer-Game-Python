from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import  QGraphicsItem, QGraphicsPixmapItem

from door import Door
from  enemy import Enemy
from lava import Lava
from player import Player

#Piirtää tason objektit
class Level():
    def __init__(self,scene, level_file,game):
        self.game = game
        self.scene = scene
        self.square_size = 32
        self.enemies = []
        self.lavas = []
        self.door = []
        self.file = level_file
        self.title_map = open(level_file).read().splitlines()
        self.add_item_to_scene()
    #Käy läpi listan, ja luo objektit, kirjaimien mukaan
    def add_item_to_scene(self):
        for y in range(len(self.title_map)):
            for x in range(len(self.title_map[0])):

                if self.title_map[y][x] == "B":
                    sprite = QPixmap("images/brick.png")
                    Rect = QGraphicsPixmapItem()
                    Rect.setPixmap(sprite)
                    Rect.setPos(x*self.square_size, y*self.square_size)
                    self.scene.addItem(Rect)
                if self.title_map[y][x] == "P":
                    self.player_x_location = x*self.square_size
                    self.player_y_location = y * self.square_size
                    player = Player(1024, 544, self, self.scene)
                    player.setFlag(QGraphicsItem.ItemIsFocusable)
                    player.setFocus()
                    self.scene.addItem(player)

                if self.title_map[y][x] == "E":
                    enemy = Enemy(x*32,y*32, self, self.scene)
                    self.enemies.append(enemy)
                    self.scene.addItem(enemy)

                if self.title_map[y][x] == "L":
                    lava = Lava(x*32,y*32, self, self.scene)
                    self.lavas.append(lava)
                    self.scene.addItem(lava)
                if self.title_map[y][x] == "D":
                    door = Door(x*32,y*32, self, self.scene)
                    self.door.append(door)
                    self.scene.addItem(door)






