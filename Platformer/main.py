import sys
from PyQt5.QtWidgets import QApplication
from game import Game
import subprocess


#Käynnistää testit, luo ikkunan ja pelin
def main():
    subprocess.Popen(['python3', 'tester.py'])
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    game.displayMainMenu()
    sys.exit(app.exec_())

main()