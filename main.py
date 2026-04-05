import sys
from PyQt5.QtWidgets import QApplication
from game import Game
import subprocess


# Starts the tests, creates the application window, and launches the game
def main():
    subprocess.Popen([sys.executable, "tester.py"])
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    game.displayMainMenu()
    sys.exit(app.exec_())

main()