from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QBrush, QImage, QColor
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QGraphicsView, QGraphicsTextItem
from PyQt5 import QtWidgets


from button import Button
from level import Level
from  PyQt5 import QtCore


class Game(QGraphicsView):
    def __init__(self):
        super().__init__()
        #Luo piirtoaluen
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 1024, 544)
        self.setScene(self.scene)
        #Värittää taustaa
        self.scene.setBackgroundBrush(QBrush(QColor(100, 0, 0)))

        #Luo ajastinta, joka käynistää Update-function 50ms välein
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Update)
        self.timer.start(50)  # Milliseconds

        #Asentaa taustamusikkia
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl("music/Background_music.mp3")))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        self.music = QMediaPlayer()
        self.music.setPlaylist(self.playlist)
        self.music.play()

        #Saa parametriksi tason tiedoston. Asentaa taustakuvaa ja luo Level-olion
    def start_level(self, level):
        self.scene.setBackgroundBrush(QBrush(QImage("images/Hell.gif")))
        Level(self.scene, level,self)

        #Piirtää päävalikkoa ja luo näppäimet

    def displayMainMenu(self):
        Title = QGraphicsTextItem("PLATFORMER")
        Title.setScale(3)
        Title.setPos(400, 0)
        self.scene.addItem(Title)
        self.start_button = Button("Start", self.scene, 400,100,470, 100, 2)
        self.scoreboard_button = Button("SCOREBOARD", self.scene, 400,150,430, 150, 2)
        self.exit_button = Button("Exit", self.scene, 400,200,470, 200, 2)

        #Tarkistaa, jos joku nappeista on painettu
    def Update(self):
        if self.start_button._clicked:
            self.Button_clicked(self.start_button, self.displayLevelMenu)
        if self.exit_button._clicked:
            self.Button_clicked(self.exit_button, exit)
        if self.scoreboard_button._clicked:
            self.Button_clicked(self.scoreboard_button, self.displayScoreBoard)
        # Estää virhen syntymisen, kun seuravat napit, eivät ole päävalikkossa
        try:
            if self.back_button._clicked:
                self.Button_clicked(self.back_button, self.displayMainMenu)
            if self.level1_button._clicked:
                self.LevelButton_clicked(self.level1_button, "LEVELS/LEVEL1")
            if self.level2_button._clicked:
                self.LevelButton_clicked(self.level2_button, "LEVELS/LEVEL2")
            if self.level3_button._clicked:
                self.LevelButton_clicked(self.level3_button, "LEVELS/LEVEL3")
        except:
            pass

# Saa paramtriksi napin ja function, joka suoritetaan, kun nappi painetaan. Vaihtaa nappi ei painettuksi, ettei funktio suoritetaan loputtomasti
    def Button_clicked(self, button, function):
        self.scene.clear()
        function()
        button._clicked= False
# Sama funktio, mutta saa parametriksi tason tiedoston, joka piirtetään.

    def LevelButton_clicked(self, button, level):
        self.scene.clear()
        self.start_level(level)
        button._clicked= False
# Piirtää Tasovalikkon ja nappia, joka palauttaa päävalikkoon
    def displayLevelMenu(self):
        Title = QGraphicsTextItem("Choose Level")
        Title.setScale(3)
        Title.setPos(400, 0)
        self.scene.addItem(Title)
        self.back_button = Button("BACK", self.scene, 0, 0, 0, 0, 2)
        self.level1_button = Button("LEVEL1", self.scene, 400, 100, 470, 100, 2)
        self.level2_button = Button("LEVEL2", self.scene, 400, 150, 470, 150, 2)
        self.level3_button = Button("LEVEL3", self.scene, 400, 200, 470, 200, 2)

#Piirtää tulostaulua ja nappia, joka palauttaa päävalikkoon

    def displayScoreBoard(self):
        self.back_button = Button("BACK", self.scene, 0, 0, 0, 0, 2)
        scoreboard = open("SCOREBOARD").read().splitlines()
        x= 400
        y = 50
        for line in scoreboard:
            self.AddText(line, x,y,3)
            y+=30

#Saa parametriksi tekstin, koordinatit, tekstin kokon ja piirtää ne.
    def AddText(self, text, x,y, scale):
        Title = QGraphicsTextItem(text)
        Title.setScale(scale)
        Title.setPos(x, y)
        self.scene.addItem(Title)








