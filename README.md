# SOSGame

This was an individual project for the UMKC course Foundation of Software Engineering. The project was completed over 6 sprints throughout the semester.

I learned these skills through doing this project:

Object-oriented programming: Familiarity with object-oriented programming concepts, including classes, objects, inheritance, and polymorphism.
Version control: Proficiency in using version control systems like Git to manage source code and collaborate with other developers.
Debugging and problem-solving: Ability to troubleshoot and resolve software issues using debugging tools and techniques.
Software design principles: Understanding of software design principles, such as modularity, abstraction, encapsulation, and separation of concerns.
Code quality: Knowledge of best practices for writing clean, maintainable, and efficient code, including addressing code smells and adhering to coding standards.
Testing: Familiarity with software testing techniques and methodologies, such as unit testing, integration testing, and test-driven development (TDD).
Development methodologies: Exposure to various software development methodologies, such as Agile
Basic project management: Understanding of project planning, requirements gathering, and time estimation techniques.
Implementation Details
The given Python code implements a tkinter-based SOS game with two game modes: "Simple Game" (Player vs Player) and "General Game" (Player vs Computer). The implementation details are as follows:

The program imports the necessary libraries and modules, such as tkinter, messagebox, random, and a custom module called SOSAlgos.
The SimpleBoard class represents the simple game mode, where two players take turns placing "S" or "O" on the game board. It initializes the game board, keeps track of scores, and implements the game logic.
The GeneralGame class inherits from SimpleBoard and represents the general game mode, where a player competes against the computer. It overrides the click method to include the AI's move after each player move.
The App class represents the main application window and menu. It includes the game board, selection of game modes, and displays scores and turn information. It also has methods to show the menu for each game mode and create a new game board based on the selected game mode.
The createBoard method in the App class is responsible for initializing a new game board of the selected game mode and board size. It creates an instance of either SimpleBoard or GeneralGame based on the user's selection.
The showSimple and showGeneral methods in the App class display the menu options for each game mode. These options include the choice of "S" or "O" for each player in the simple game mode and the choice of "S" or "O" for the player in the general game mode.
The program creates a tkinter window and initializes the App class with the window as a parameter. The main tkinter event loop is then started.
In summary, the program creates a tkinter-based SOS game with both player vs player and player vs computer game modes. The user can choose the game mode and board size, and the game tracks scores and turns throughout the gameplay.
