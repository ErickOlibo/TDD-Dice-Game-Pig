# DICE GAME PIG v2.00
This version follow the same requirement as the original one. 

The differences are:
- The classes that will be implemented
- The design
- Better understanding of TDD and good code
- Using code coverage, pylint and flake8 regularly during implementation
- Interfaces, Abstract classes, Enum methods, etc...
- Proper separation from Model and Views
- No use of private/protected properties in unittesting methods

For example:
- game.py (abstract class)
    * duel.py (inherit from class Game)
    * solo.py (inherit from class Game)
- participant.py (abstract class)
    * user.py (inherit from class Participant)
    * cpu.py (inherit from class Participant)
- utilities.py [old helpers.py] (for enums and constant)
- gui.py (user interface)
- brain.py (cpu simulated intellect)
- database.py (saves instances of class object Game)
- dice.py
- winner.py
- main.py (entry point)

Extra files:
- Makefile
- Docs
- UML
- LICENSE.md


## Document the evolution...