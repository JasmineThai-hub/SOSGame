import unittest
import App
from tkinter import *

class MyTestCase(unittest.TestCase):
    def testSuccessfulBoard(self):
        window = Tk()
        app = App.App(window)
        app.selectedGM.set("Simple Game") #Click Simple Game Radio Button
        n = StringVar()
        n.set("5")
        app.boardSize = n  # Set board size to 5
        check = app.createBoard()
        self.assertEqual(5, check)

    def testDecimalBoard(self):
        window = Tk()
        app = App.App(window)
        app.selectedGM.set("Simple Game") #Click Simple Game Radio Button
        n = StringVar()
        n.set("4.5")
        app.boardSize = n  # Set board size to 4.5
        check = app.createBoard()
        self.assertEqual(0, check) #Check exception handling

    def testLessThanTwoBoard(self):
        window = Tk()
        app = App.App(window)
        app.selectedGM.set("Simple Game") #Click Simple Game Radio Button
        n = StringVar()
        n.set("-1")
        app.boardSize = n  # Set board size to 4.5
        check = app.createBoard()
        self.assertEqual(0, check) #Check exception handling

    def testValidSimpleMenu(self):
        window = Tk()
        app = App.App(window)
        app.selectedGM.set("Simple Game") #Click Simple Game Radio Button
        gm = app.showSimple()
        self.assertEqual("Simple Game", gm) #Make sure it's actually returning a Simple Game

    def testValidGeneralMenu(self):
        window = Tk()
        app = App.App(window)
        app.selectedGM.set("General Game") #Click Simple Game Radio Button
        gm = app.showGeneral()
        self.assertEqual("General Game", gm) #Make sure it's actually returning a Simple Game

    def testInvalidGameMenu(self):
        window = Tk()
        app = App.App(window)
        gm = app.showSimple()
        self.assertEqual('', gm)

    def testInvalidSimpleMove(self):
        window = Tk()
        app = App.App(window)
        app.selectedGM.set("Simple Game")  # Click Simple Game Radio Button
        app.showSimple()
        n = StringVar()
        n.set("5")
        app.boardSize = n  # Set board size to 5
        app.createBoard()
        self.assertEqual(0, app.b.click(0, 0))

    def testValidSimpleMove(self):
        window = Tk()
        app = App.App(window)
        app.selectedGM.set("Simple Game")  # Click Simple Game Radio Button
        app.showSimple()
        n = StringVar()
        n.set("5")
        app.boardSize = n  # Set board size to 5
        app.createBoard()
        app.p1selectedSO.set("S")
        app.p2selectedSO.set("O")
        self.assertEqual(1, app.b.click(0, 0))

    def testInvalidGeneralMove(self):
        window = Tk()
        app = App.App(window)
        app.selectedGM.set("General Game")  # Click Simple Game Radio Button
        app.showGeneral()
        n = StringVar()
        n.set("5")
        app.boardSize = n  # Set board size to 5
        app.createBoard()
        self.assertEqual(0, app.b.click(0, 0))

    def testValidGeneralMove(self):
        window = Tk()
        app = App.App(window)
        app.selectedGM.set("General Game")  # Click Simple Game Radio Button
        app.showGeneral()
        n = StringVar()
        n.set("5")
        app.boardSize = n  # Set board size to 5
        app.createBoard()
        app.p1selectedSO.set("S")
        self.assertEqual('red', app.b.turn) #we changed this from the simple to check if computer made a turn
        #if true, then computer made a turn and it is now p1 turn again

if __name__ == '__main__':
    unittest.main()
