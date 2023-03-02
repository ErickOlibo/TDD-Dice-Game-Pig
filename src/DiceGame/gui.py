from helpers import *

class GUI:
    """ This class is responsible for interacting with the user
        Meaning, any output (text to user), and input (response from user)
        is handled here
    """
    
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
        
    
    def display_scoreboard(self, name_one: str, name_two: str, s_one: int, s_two: int):
        one = self._shrink_name(name_one)
        two = self._shrink_name(name_two)
        line1 = "┌──────────────┐┌─────┐ ┌──────────────┐┌─────┐"
        line2 = f'{"│ "}{one:<13}   {s_one:>3}{" │ │ "}{two:<13}   {s_two:>3}{" │"}'
        line3 = "└──────────────┘└─────┘ └──────────────┘└─────┘"
        scoreboard = "\n".join([line1, line2, line3])
        print(scoreboard)

    def _shrink_name(self, name: str) -> str:
        return name if len(name) <= 13 else name[0:10] + '...'
    
    
    def display_hand_turn(self):
        pass

    

gui = GUI()
myList = {2,4,6,5,3}
gui.display_hand_results(myList, 20)
print("\n")
scoreboard = gui.display_scoreboard("ErickTerrasson", "Robert", 49, 89)

#print(f'\n{gui._shrink_name("ErickTerrasson")}')