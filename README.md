# DICE GAME PIG

## Bachelor Programme in Software Development - Kristianstad University
- Course: Methods for Sustainable Programming
- Period: Spring 2023 (1st Year)
- Exam: Assignment 2 - Test Driven Development

## Welcome to DICE GAME PIG!
This project is a simple implementation of the dice game pig, created by Erick Olibo and Robert Nesta Nuhu as a assignment exercise.

## Installation
To install this project, you can either download the repository as a ZIP file or clone it using Git.

### Download as ZIP
1. Go to the repository page (https://github.com/ErickOlibo/TDD-Dice-Game-Pig).
2. Click on the "Code" button and select "Download ZIP".
3. Once downloaded, extract the ZIP file to your desired location.

### Clone with Git
1. Open a terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command: git clone https://github.com/ErickOlibo/TDD-Dice-Game-Pig.git' 


## Usage
To run this project, you will need to create a virtual environment and install the required dependencies.

### Creating a Virtual Environment
1. Open a terminal or command prompt.
2. Navigate to the directory where you downloaded/cloned the repository.
3. Run the following command to create a new virtual environment:
```python -m venv venv```


### Activating the Virtual Environment
1. Run the following command to activate the virtual environment:
```source venv/bin/activate```

### Installing Dependencies
1. Run the following command to install the required dependencies:
``` pip install -r requirements.txt```


### Running the Game
1. Navigate to the directory where you downloaded/cloned the repository.
2. Activate the virtual environment using the command shown above.
3. Run the following command to start the game:
```python main.py```

### Use Makefile
You can use this repo and clone it to your desktop, and then use make file
1. Create virtual Environment, Activate it.
2. Use the Makefile to do the rest.
    * check you are running Python 3:  ```make version```
    * Install requirements: ```make install```
    * Check the code coverage: ```make coverage```
    * Check the style: ```make flake8```
    * Check the linter: ```make pylint```
    * Produce the HTML documentation: ```make doc```
    * Create a UML view of the source code: ```make uml```
    * Clean up the created files: ```make clean```
3. Run the Dice Game Pig: ```make run```
