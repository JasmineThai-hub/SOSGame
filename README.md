# SOS Game

# Individual Project for UMKC Course: Foundation of Software Engineering

This project was completed over six sprints throughout the semester.

## Skills Learned Through the Project

- **Object-oriented programming**: Familiarity with object-oriented programming concepts, including classes, objects, inheritance, and polymorphism.
- **Version control**: Proficiency in using version control systems like Git to manage source code and collaborate with other developers.
- **Debugging and problem-solving**: Ability to troubleshoot and resolve software issues using debugging tools and techniques.
- **Software design principles**: Understanding of software design principles, such as modularity, abstraction, encapsulation, and separation of concerns.
- **Code quality**: Knowledge of best practices for writing clean, maintainable, and efficient code, including addressing code smells and adhering to coding standards.
- **Testing**: Familiarity with software testing techniques and methodologies, such as unit testing, integration testing, and test-driven development (TDD).
- **Development methodologies**: Exposure to various software development methodologies, such as Agile.
- **Basic project management**: Understanding of project planning, requirements gathering, and time estimation techniques.

## Implementation Details

The Python code provided implements a tkinter-based SOS game with two game modes: "Simple Game" (Player vs Player) and "General Game" (Player vs Computer). Below are the implementation details:

### Classes and Modules

- **Imports**: The program imports the necessary libraries and modules, such as `tkinter`, `messagebox`, `random`, and a custom module called `SOSAlgos`.

#### SimpleBoard Class

- Represents the simple game mode, where two players take turns placing "S" or "O" on the game board.
- Initializes the game board, keeps track of scores, and implements the game logic.

#### GeneralGame Class

- Inherits from `SimpleBoard` and represents the general game mode, where a player competes against the computer.
- Overrides the `click` method to include the AI's move after each player move.

#### App Class

- Represents the main application window and menu.
- Includes the game board, selection of game modes, and displays scores and turn information.
- Has methods to show the menu for each game mode and create a new game board based on the selected game mode.

### Methods

#### createBoard Method (in App Class)

- Responsible for initializing a new game board of the selected game mode and board size.
- Creates an instance of either `SimpleBoard` or `GeneralGame` based on the user's selection.

#### showSimple and showGeneral Methods (in App Class)

- Display the menu options for each game mode.
- These options include the choice of "S" or "O" for each player in the simple game mode and the choice of "S" or "O" for the player in the general game mode.

### Execution

- The program creates a tkinter window and initializes the `App` class with the window as a parameter.
- The main tkinter event loop is then started.

### Summary

In summary, the program creates a tkinter-based SOS game with both player vs player and player vs computer game modes. The user can choose the game mode and board size, and the game tracks scores and turns throughout the gameplay.
