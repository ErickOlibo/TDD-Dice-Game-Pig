import os
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
    
    
    def clear_terminal(self):
        os.system('clear')
    
    
    def display_info(self, text: str, title: str, width = 40):
        header = self._set_menu_header(title, width)
        info = "".join([header, text])
        print(info)


    def get_simple_answer_from_user(self, ask: str, title: str, width = 40) -> str:
        header = self._set_menu_header(title, width)
        ask_input = "\n".join([header, ask])
        return input(ask_input)
    
    def display_hand_results(self, numbers: list, points: int):
        """Display the results of a dice roll to the user, including the
        individual dice faces and the total points for the roll.
        
        Args:
            numbers (list): A list of integers representing the dice rolls.
            points (int): An integer representing the total points for the roll.
        """
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
        """Return a string representation of the points for a dice roll.
        
        Args:
            points (int): An integer representing the total points for the roll.
        
        Returns:
            tuple of str: A tuple of strings representing the points for the roll.
        """
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
        
        one = self._shrink_name(one, 13)
        two = self._shrink_name(two, 13)
        line1 = "┌────┬───────────────┐┌─────┐ ┌────┬───────────────┐┌─────┐"
        line2 = f'│ {c[0]} │ {one:<13}    {s_one:>3} │ │ {c[1]} │ {two:<13}    {s_two:>3}{" │"}'
        line3 = "└────┴───────────────┘└─────┘ └────┴───────────────┘└─────┘"

    def _shrink_name(self, name: str) -> str:
        return name if len(name) <= 13 else name[0:10] + '...'
    
    def display_hand_turn(self):
        """Displays the entry menu for the game and prompts the user for a choice.

        Returns:
            An integer representing the user's choice: 1 for New Game, 2 for Resume Game, or E for Exit.
        """
        pass

    def get_input_from_shown_menu(self, title: str, question: str, options: list, 
                                  legend = ['Option', 'Actions']
                                  ) -> str:
        menu = self._get_menu_layout(title,options, legend)
        menu += f"\n{question}"
        return input(menu)
        
    
    def _get_menu_layout(self, title: str, opt: list, legend) -> str:
        leg1 = legend[0]
        leg2 = legend[1]
        line1 = "┌────────┬──────────────────────┐"
        line2 = f'│ {leg1:^6} │ {leg2:^20}{" │"}'
        line3 = "├────────┼──────────────────────┤"
        end = "└────────┴──────────────────────┘"
        center = []
        for i in range(len(opt)):
            row = f'│ {opt[i][0]:^6} │ {opt[i][1]:<20}{" │"}'
            if i != len(opt) - 1:
                row += f'\n│ {"":^6} │ {"":^20}{" │"}'
            center.append(row)

        start = [line1, line2, line3]
        header = self._set_menu_header(title, len(line1))
        menu = "\n".join([header] + start + center + [end])
        return menu
    
    
    def _set_menu_header(self, title: str, width = 40) -> str:
        return f" {title} ".center(width, "~")
    
    
    def display_highscore(self, scores: list, size: int):
        scores.sort(key=lambda row: (-row[1], -row[2]))
        line1 = "┌──────┬──────────────────────┬────────┬────────┐"
        line2 = f'│ {"Rank":^4} │ {"Names":^20} │ {"Streak":^6} │ {"Points":^6} │' 
        line3 = "├──────┼──────────────────────┼────────┼────────┤"
        end = "└──────┴──────────────────────┴────────┴────────┘"
        header = self._set_menu_header(f'HIGH-SCORE TOP[{size}]', len(line1))
        center = []
        top = scores[0:size]
        for i in range(len(top)):
            name = scores[i][0]
            streak = scores[i][1]
            points = scores[i][2]
            row = f'│ {i+1:^4} │ {name:^20} │ {streak:^6} │ {points:>6} │'
            if i != len(top) - 1:
                row += f'\n│ {"":^4} │ {"":^20} │ {"":^6} │ {"":>6} │'
            center.append(row)
        highscore = "\n".join([header, line1, line2, line3] + center + [end])
        print(highscore)
        pass
        
    def display_any_key_continues(self):
        input('Press any keys to contiue: ')

    def insert_line_breaks(self, numb: int):
        [print() for _ in range(numb)]


# TO DELETE WHAT'S UNDER TESTING

# gui = GUI("ErickTerrasson", "Robert")
# gui.display_info(Textual.RULES.value, 'RULES')
# print()
# title = 'START UP'
# options = [['N', 'New game'], ['R', 'Resume game'], ['E', 'Exit']]
# legend = ['Option', 'Actions']
# question = 'What would you like to do? Pick an option: '

# gui.get_input_from_shown_menu(title, question, options, legend)

# gui.display_scoreboard(34,20, 'Robert')
# rolls = [2,3,4]
# gui.display_hand_results(rolls, 9)

#scores = [["Erick", 2005, 222512], ["Robert", 2, 203], ["Steve", 5, 514]]

#gui.display_highscore(scores)