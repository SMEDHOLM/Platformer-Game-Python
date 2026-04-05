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
        # Create the rendering scene
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 1024, 544)
        self.setScene(self.scene)
        # Set the background color
        self.scene.setBackgroundBrush(QBrush(QColor(100, 0, 0)))

        # Create a timer that calls the update function every 50 ms
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Update)
        self.timer.start(50)  # Milliseconds

        # Configure background music playback
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl("music/Background_music.mp3")))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        self.music = QMediaPlayer()
        self.music.setPlaylist(self.playlist)
        self.music.play()

    # Receives a level file, sets the background, and creates the Level object
    def start_level(self, level):
        self.scene.setBackgroundBrush(QBrush(QImage("images/Hell.gif")))
        Level(self.scene, level,self)

        # Draws the main menu and creates buttons

    def displayMainMenu(self):
        Title = QGraphicsTextItem("PLATFORMER")
        Title.setScale(3)
        Title.setPos(400, 0)
        self.scene.addItem(Title)
        self.start_button = Button("Start", self.scene, 400,100,470, 100, 2)
        self.scoreboard_button = Button("SCOREBOARD", self.scene, 400,150,430, 150, 2)
        self.exit_button = Button("Exit", self.scene, 400,200,470, 200, 2)

        # Checks whether any of the buttons have been clicked
    def Update(self):
        if self.start_button._clicked:
            self.Button_clicked(self.start_button, self.displayLevelMenu)
        if self.exit_button._clicked:
            self.Button_clicked(self.exit_button, exit)
        if self.scoreboard_button._clicked:
            self.Button_clicked(self.scoreboard_button, self.displayScoreBoard)
        # Prevent errors when the following buttons are not present on the current menu
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

# Receives a button and a callback function, then clears the scene and executes the callback.
# Resets the button state so the action does not repeat continuously.
    def Button_clicked(self, button, function):
        self.scene.clear()
        function()
        button._clicked= False
# Same pattern, but it receives a level file to start.

    def LevelButton_clicked(self, button, level):
        self.scene.clear()
        self.start_level(level)
        button._clicked= False
# Draws the level selection menu and a button to return to the main menu
    def displayLevelMenu(self):
        Title = QGraphicsTextItem("Choose Level")
        Title.setScale(3)
        Title.setPos(400, 0)
        self.scene.addItem(Title)
        self.back_button = Button("BACK", self.scene, 0, 0, 0, 0, 2)
        self.level1_button = Button("LEVEL1", self.scene, 400, 100, 470, 100, 2)
        self.level2_button = Button("LEVEL2", self.scene, 400, 150, 470, 150, 2)
        self.level3_button = Button("LEVEL3", self.scene, 400, 200, 470, 200, 2)

# Draws the scoreboard and a button to return to the main menu

    def displayScoreBoard(self):
        self.back_button = Button("BACK", self.scene, 0, 0, 0, 0, 2)
        scoreboard = open("SCOREBOARD").read().splitlines()
        x= 400
        y = 50
        for line in scoreboard:
            self.AddText(line, x,y,3)
            y+=30

# Receives text, coordinates, scale, and draws it on the scene.
    def AddText(self, text, x,y, scale):
        Title = QGraphicsTextItem(text)
        Title.setScale(scale)
        Title.setPos(x, y)
        self.scene.addItem(Title)








