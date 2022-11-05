from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from SOSAlgos import *
import random

class SimpleBoard:
    def __init__(self, b, n, p1Sel, p2Sel, p1Score, p2Score, t, window):
        self.board = b
        self.p1Score = p1Score
        self.p2Score = p2Score
        self.t = t
        self.window = window
        self.n = n
        self.text = " "
        self.turn = 'red'
        self.players = {
            'red':p1Sel,
            'blue':p2Sel,
        }
        self.playerScore = {
            'red': 0,
            'blue': 0
        }
        self.arr = [[Button(self.board, text=self.text, bd=5, height=4, width=8,bg='Linen') for x in range(self.n)] for y in range(self.n)]
        self.count = 0

    def checkTie(self):
        if self.count == (self.n * self.n):
            if self.playerScore["red"] == self.playerScore["blue"]:
                messagebox.showinfo("Tie", "It was a tie")
            elif self.playerScore["red"] > self.playerScore["blue"]:
                messagebox.showinfo("Winner", "Red Won")
            elif self.playerScore["red"] < self.playerScore["blue"]:
                messagebox.showinfo("Winner", "Blue Won")
            self.clear_board()

    def change_turn(self):  # Function to change the operand for the next player
        for i in ['red', 'blue']:
            if not (i == self.turn):
                self.turn = i
                break

    def click(self, row, col):
        if self.players[self.turn].get() != "S" and self.players[self.turn].get() != "O":
            messagebox.showinfo("NOPE", "Invalid Move")
            return 0
        else:
            self.count += 1
            self.arr[row][col].config(text=self.players[self.turn].get(),state=DISABLED, disabledforeground="black")
            checkWin = Score(self.arr, self.turn, self.n)
            if checkWin != 0:
                self.playerScore[self.turn] += checkWin
                self.p1Score.set("Red's Score:{}".format(str(self.playerScore["red"])))
                self.p2Score.set("Blue's Score: {}".format(str(self.playerScore["blue"])))
            else:
                self.change_turn()
            self.checkTie()
            self.t.set("It is {}'s turn".format(self.turn))
            return 1

    def show_board(self):
        clearBoardButton = Button(
            self.window,
            text="Clear Board",
            command=self.clear_board
        )
        clearBoardButton.place(x=1100, y=3)
        for i in range(self.n):
            for j in range(self.n):
                self.arr[i][j].config(command=lambda row=i, col=j: self.click(row,
                                                                              col))
                self.arr[i][j].grid(row=i, column=j)
        self.board.place(x=600, y=50)

    def clear_board(self):
        self.board.destroy()

class GeneralGame(SimpleBoard):
    def __init__(self, b, n, p1Sel, p2Sel, p1Score, p2Score, t, window):
        super().__init__(b, n, p1Sel, p2Sel, p1Score, p2Score, t, window)
        self.AISel = StringVar()
        self.players["blue"] = self.AISel

    def playAI(self):
        if self.turn == 'blue':
            for i in range(self.n):
                for j in range(self.n):
                    if not(self.arr[i][j].cget('text') in ("S", "O")):
                        ranSO = random.randint(0,1)
                        if ranSO == 0:
                            self.AISel.set("S")
                        else:
                            self.AISel.set("O")
                        self.click(i,j)
                        return 1
        else:
            return 0

    def click(self, row, col):
        if self.count == (self.n * self.n):
            return 0
        if self.players[self.turn].get() != "S" and self.players[self.turn].get() != "O":
            messagebox.showinfo("NOPE", "Invalid Move")
            return 0
        else:
            self.count += 1
            self.arr[row][col].config(text=self.players[self.turn].get(),state=DISABLED, disabledforeground="black")
            checkWin = Score(self.arr, self.turn, self.n)
            if checkWin != 0:
                self.playerScore[self.turn] += checkWin
                self.p1Score.set("Red's Score:{}".format(str(self.playerScore["red"])))
                self.p2Score.set("Blue's Score: {}".format(str(self.playerScore["blue"])))
            else:
                self.change_turn()
            self.checkTie()
            self.playAI()
            self.t.set("It is {}'s turn".format(self.turn))
            return 1

class App:
    def __init__(self, window):
        self.window = window
        self.window.state('zoomed')
        self.window.configure(bg='green')
        self.t = StringVar()
        self.p1Score = StringVar()
        self.p2Score = StringVar()
        self.t.set("It is red's turn")
        label = Label(self.window, textvariable=self.t, bg="green")
        label.place(x=600, y=5)
        self.p1Score.set("Red's Score:")
        redLabel = Label(self.window, textvariable=self.p1Score, bg="green")
        redLabel.place(x=750, y=5)
        self.p2Score.set("Blue's Score:")
        redLabel = Label(self.window, textvariable=self.p2Score, bg="green")
        redLabel.place(x=900, y=5)
        self.board = Canvas(self.window, width=800, height=700, bg='Linen')
        self.board.place(x=600, y=25)
        # MENU GUI
        self.menuCanvas = Canvas(self.window, width=530, height=1280, bg='sky blue')
        self.menuCanvas.pack(side=LEFT)
        # label
        label = Label(text="Welcome to SOS!")
        label.place(x=0, y=0, width=530)
        self.menuCanvas.create_text(75, 35, text="Choose your game mode:", fill="black")
        self.menuCanvas.create_text(300, 60, text="Board Size:", fill="black")
        self.boardSize = Entry(self.menuCanvas)
        self.boardSize.place(x=335, y=50)
        # Simple/General Radio Buttons
        self.selectedGM = StringVar()
        self.p1selectedSO = StringVar()
        self.p2selectedSO = StringVar()
        self.simpleRadio = Radiobutton(
            self.menuCanvas,
            text="Simple Game",
            value="Simple Game",
            variable=self.selectedGM,
            bg='sky blue',
            command=self.showSimple
        )
        self.simpleRadio.place(x=10, y=50)
        self.generalRadio = Radiobutton(
            self.menuCanvas,
            text="General Game",
            value="General Game",
            variable=self.selectedGM,
            bg='sky blue',
            command=self.showGeneral
        )
        self.generalRadio.place(x=135, y=50)

    def showSimple(self):
        chosenCanvas = Canvas(self.menuCanvas, width=530, height=1000, bg='sky blue')
        chosenCanvas.create_text(40, 110, text="Player 1: RED", fill="red")
        # S/O radio buttons
        ry = 100
        t = "S"
        for i in range(2):
            ry += 30
            r = Radiobutton(
                chosenCanvas,
                text=t,
                value=t,
                variable=self.p1selectedSO,
                bg='sky blue',
            )
            r.place(x=10, y=ry)
            if t == "S":
                t = "O"
            else:
                t = "S"
        ry += 50
        chosenCanvas.create_text(80, 50, text="SIMPLE GAME", fill="black")
        chosenCanvas.create_text(80, 70, text="Player vs Player", fill="black")
        chosenCanvas.create_text(40, 220, text="Player 2: BLUE", fill="blue")
        # S/O radio buttons
        ry = 100
        t = "S"
        for i in range(2):
            ry += 30
            r = Radiobutton(
                chosenCanvas,
                text=t,
                value=t,
                variable=self.p1selectedSO,
                bg='sky blue',
            )
            r.place(x=10, y=ry)
            if t == "S":
                t = "O"
            else:
                t = "S"
        ry += 50
        for i in range(2):
            if i == 2:
                val = "S"
            else:
                val = "O"
            ry += 30
            p2 = Radiobutton(
                chosenCanvas,
                text=t,
                value=t,
                variable=self.p2selectedSO,
                bg='sky blue'
            )
            p2.place(x=10, y=ry)
            if t == "S":
                t = "O"
            else:
                t = "S"
        # button
        button = Button(
            chosenCanvas,
            text="New Game",
            command=self.createBoard
        )
        button.place(x=10, y=300)
        chosenCanvas.place(x=0, y=100)
        return self.selectedGM.get()

    def showGeneral(self):
        chosenCanvas = Canvas(self.menuCanvas, width=530, height=1000, bg='sky blue')
        chosenCanvas.create_text(80, 50, text="GENERAL GAME", fill="black")
        chosenCanvas.create_text(80, 70, text="Player vs Computer", fill="black")
        chosenCanvas.create_text(40, 110, text="Player 1: RED", fill="red")
        # S/O radio buttons
        ry = 100
        t = "S"
        for i in range(2):
            ry += 30
            r = Radiobutton(
                chosenCanvas,
                text=t,
                value=t,
                variable=self.p1selectedSO,
                bg='sky blue',
            )
            r.place(x=10, y=ry)
            if t == "S":
                t = "O"
            else:
                t = "S"
        ry += 50

        # button
        button = Button(
            chosenCanvas,
            text="New Game",
            command=self.createBoard
        )
        button.place(x=10, y=300)
        chosenCanvas.place(x=0, y=100)
        return self.selectedGM.get()

    def createBoard(self):
        board = Canvas(self.window, width=800, height=700, bg='Linen')
        board.place(x=600, y=25)
        self.p1Score.set("Red's Score:")
        self.p2Score.set("Blue's Score:")
        self.t.set("It is red's turn")
        try:
            self.n = int(self.boardSize.get())
        except(ValueError):
            messagebox.showinfo("Error 101", "Invalid Board Size")
            return 0
        if self.n == '' or self.n < 2:
            messagebox.showinfo("Error 101", "Invalid Board Size")
            return 0
        else:
            if self.selectedGM.get() == "Simple Game":
                self.b = SimpleBoard(board, self.n, self.p1selectedSO, self.p2selectedSO, self.p1Score, self.p2Score, self.t, self.window)
                self.b.show_board()
                return self.n
            elif self.selectedGM.get() == "General Game":
                self.b = GeneralGame(board, self.n, self.p1selectedSO, self.p2selectedSO, self.p1Score, self.p2Score,
                                     self.t, self.window)
                self.b.show_board()
                return self.n