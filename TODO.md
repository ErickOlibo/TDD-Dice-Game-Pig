

# ASSIGNMENT 2 - TEST DRIVEN DEVELOPMENT
This assignment uses the TDD approach to creating softwares. This page will be updated as we go along with the making of the assignment.

## [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) provided by GitHub.com


As we are using TDD we will follow:
- [The Three Rules of TDD](https://www.oreilly.com/library/view/modern-c-programming/9781941222423/f_0055.html). Robert C. Martin ("Uncle Bob") provides a consise set of rules
  1. Write production code only to pass a failing unit test.
  2. Write no more of a unit test than sufficient to fail (compilation failures are failures).
  3. Write no more production code than necessary to pass the one failing unit test.

Rule #1 says to write tests first—understand and specify, in the form of a unit test example, behavior you must build into the system.

Rule #2 says to proceed as incrementally as possible—after each line you write, get feedback (via compilation or test run) if you can before moving on.


# TODO LIST

## Classes Testing & Implementation --> `Erick` [Due: Thu 2, March]
----------------------------------------------------------
Classes to Test and Implement are:
1. GAME.PY
2. BRAIN.PY
3. DATABASE.PY

  - game.py & test_game.py
    1. Class name: 
        - Game
    2. Properties:
        - Rules: constant
        - UID: unique game ID (persistency)
        - Mode: player vs. CPU OR playerOne vs. playerTwo
        - Difficulty: Easy (1 roll), Medium (2 rolls), Hard (3 rolls), Impossible (5 rolls)
        - Game_Type: Class object
        - Turn: keep track of the player turn. This game only have 2 players (not more)
        - etc...
    3. Methods:
        - Init: starts an instance of the game or restart suspended game with code
        - Menu: set the mode, difficulty, style, or restart game with code
        - In_Game_Menu: while the game is on-going
        - Start: starts or restarts game
        - Pause: persistantly (generate unique code)
        - End: destroy current running game and return to menu
        - Cheat: Provide mechanism to win the game rapidly.
        - etc...
  - brain.py & test_brain.py
    1. Class name:
        - Brain
    2. Properties:
        - Frist: Constant for the Hold_20 strategy
        - second: Constant for the Hold_25 strategy
        - third: End race or Keep Pace
        - etc...
    3. Methods:
        - Hold_20: popular strategy [8% disadvantage against Optimal Play]
        - Hold_25: popular strategy [4% disadvantage against Optimal Play]
        - Race_Pace: popular strategy [1% disavantage against Optimal Play]
        - ect...
  - database.py & test_database.py
    1. Class name:
        - Database
    2. Properties:
        - file_name:
        - file_path 
    3. Methods:
        - update_player_name:
        - save_game: game to database
        - save_histogram:
        - save_highscore:
        - retrieve_game:
        - retrieve_histogram:
        - retrieve_highscore:



## Classes Testing & Implementation --> `Robert` [Due: Thu 2, March]
----------------------------------------------------------
Classes to Test and Implement are:
1. DICE.PY
2. HISTOGRAM.PY
3. HIGHSCORE.PY
4. PLAYER.PY

  - dice.py & test_dice.py
    1. Class name:
        - Dice
    2. Properties:
        - random roll vaule
    3. Methods:
        - Init
        - roll dice

  - histogram.py & test_histogram.py
    1. Class name:
        - Histogram
    2. Properties:
        - 
    3. Methods:
        - ect...

  - highscore.py & test_highscore.py (streak length + total point earned)
    1. Class name:
        - Highscore
    2. Properties:
        - streak length
        - total point 
    3. Methods:
        - add streak
        - add point to total

  - player.py & test_player.py
    1. Class name:
        - Player
    2. Properties:
        - name 
    3. Methods:
        - init
        - set name
        - get name

## Classes Testing & Implementation --> `NO ONE` [Due: Sat 4, March]
----------------------------------------------------------
  - main.py & test_main.py
  - inout.py & test_inout.py <-- Separating GUI from other execution
    1. Class name:
        - InOut
    2. Properties:
        - etc...
    3. Methods:
        - ect...


## UPDATING FOLLOWING FILES & TASKS --> `NO ONE` [Due: Mon 6, March]
----------------------------------------------------------
  - LICENSE.md
  - Makefile
  - README.md - Fully document the project and show how a new user can execute the application and know enough to work as a develpoper on the project.
  - RELEASE.md
  - requirements.txt
  - Git & Commits - `50 commits & 10 tags at least`
  - Unit Testing - `make test` & `make coverage`. [add how-to-do-this in README.md]
  - Generate documentation from comments - `make doc` - Must be HTML and inside `doc/api`. [add how-to-do-this in README.md]
  - Generate UML diagrams from code - `make uml` - Documentation included inside `doc/uml` - must generate a least a class diagram and a package diagram [add how-to-do-this in README.md]
  - Code Style - add linters to ensure proper code style - Use at least the tools
    - `pylint`
    - `flake8`
    - `flake8-docstrings`
    - `flake8-polyfill`
    - add `make lint` as a target to execute the linters







