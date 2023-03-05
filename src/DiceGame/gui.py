from helpers import *

class GUI:
    """ 
        This class is responsible for interacting with the user via a simple
        text graphic. It does not process, but merly gets data and
        display them according to the method selected.
        An input from the user is forwarded as string. The mecanism for checking
        the return string (ValueError, TypeError etc...) must be handled 
        by the caller.
    """
    
    def __init__(self, player_one: str = None, player_two: str = None):
        self._player_one = player_one
        self._player_two = player_two
        pass
    
    @property
    def player_one(self)-> str:
        return self._player_one
    
    @player_one.setter
    def player_one(self, name):
        self._player_one = name
        
    
    @property
    def player_two(self)-> str:
        return self._player_two
    
    @player_two.setter
    def player_two(self, name):
        self._player_two = name
    
    
    def display_hand_results(self, numbers: list, points: int):
        faces = []
        for numb in numbers:
            faces.append(DICE_FACES[numb])
        
        faces_and_points = faces + [self._get_rolls_points(points)]

        faces_rows = []
        for idx in range(DIE_HEIGHT):
            row_cells = []
            for face in faces_and_points:
                row_cells.append(face[idx])
            row_line = DIE_SEP.join(row_cells)
            faces_rows.append(row_line)
            display = "\n".join(faces_rows)
        print(display)
    
    
    def _get_rolls_points(self, points: int):
        line1 = ""
        line2 =  "  ┌─────┐"
        line3 = f'{"= │"} {points:>3} │'
        line4 =  "  └─────┘"
        line5 = ""
        return (line1, line2, line3, line4, line5)
        
    
    def display_scoreboard(self, s_one: int, s_two: int, hand: str):
        if None in [self._player_one, self._player_two]:
            raise Exception("Players' names must be initialized before using this method!")
        one = self._player_one
        two = self._player_two
        if hand not in [one, two]:
            msg = f'"{hand}" does not match any of the players names: [{one}, {two}]'
            raise ValueError(msg)
        
        c = ['🟩', '🟥']
        if hand == two : c.reverse()
        
        one = self._shrink_name(one)
        two = self._shrink_name(two)
        line1 = "┌────┬───────────────┐┌─────┐ ┌────┬───────────────┐┌─────┐"
        line2 = f'│ {c[0]} │ {one:<13}    {s_one:>3} │ │ {c[1]} │ {two:<13}    {s_two:>3}{" │"}'
        line3 = "└────┴───────────────┘└─────┘ └────┴───────────────┘└─────┘"
        scoreboard = "\n".join([line1, line2, line3])
        print(scoreboard)


    def _shrink_name(self, name: str) -> str:
        return name if len(name) <= 13 else name[0:10] + '...'
    

    # METHOD TO BE MOVED. IT VIOLATE THE PURPOSE OF THIS GUI CLASS
    def display_entry_menu(self) -> int:
        while True:
            try:
                entry_choice = input('1 - New Game, 2 - Resume Game, E - Exit: ')
                if entry_choice not in ['1', '2', 'e']: raise ValueError()
            except ValueError:
                print('Must be an intege between 1 and 3. Please try again!')
            except TypeError:
                print('Must be an intege between 1 and 3. Please try again!')
            
            return entry_choice

    

gui = GUI("Erick", "Robert")
myList = {2,6}

print("\n")
gui.display_scoreboard(49, 89, 'Robert')
gui.display_hand_results(myList, 8)
print("\n")

myList = {2,6,4}

print("\n")
gui.display_scoreboard(49, 89, 'Erick')
gui.display_hand_results(myList, 12)
print("\n")