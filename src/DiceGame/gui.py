"""This module display info and interacts with the user."""
import os
from helpers import DIE_HEIGHT, DICE_FACES, DIE_SEP
import time


class GUI:

    def clear_terminal(self):
        os.system('clear')

    def display_info(self, text: str, title: str, width=40):
        header = self._set_menu_header(title, width)
        info = "".join([header, text])
        print(info)

    def get_simple_answer_from_user(self, ask: str,
                                    title: str, width=40) -> str:
        header = self._set_menu_header(title, width)
        ask_input = "\n".join([header, ask])
        return input(ask_input)

    def get_simple_answer_from_cpu(self, ask: str,
                                   title: str, width=40) -> str:
        header = self._set_menu_header(title, width)
        ask_input = "\n".join([header, ask])
        return ask_input

    def display_hand_results(self, numbers: list, points: int):
        """Display the dice rolled for the current user.

        Args:
            numbers (list): List of integers representing the dice rolls.
            points (int): Integer representing the total points for the roll.
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

    def display_hand_results_split(self, numbers: list,
                                   points: int, split=4):
        chunk = [numbers[i:split+i] for i in range(0, len(numbers), split)]
        rows = []
        for int_list in chunk:
            faces = []
            for numb in int_list:
                faces.append(DICE_FACES[numb])
            if int_list == chunk[-1]:
                fap = faces + [self._get_rolls_points(points)]
            else:
                fap = faces + []
            faces_rows = []
            for idx in range(DIE_HEIGHT):
                row_cells = []
                for face in fap:
                    row_cells.append(face[idx])
                row_line = DIE_SEP.join(row_cells)
                faces_rows.append(row_line)
            display = "\n".join(faces_rows)
            rows.append(display)
        lines = "\n".join(rows)
        print(lines)

    def display_scoreboard(self, n1: str, s1: int,
                           n2: str, s2: int, hand: str):
        c = ['🟩', '🟥']
        if hand == n2:
            c.reverse()
        n1 = self._shrink_name(n1, 13)
        n2 = self._shrink_name(n2, 13)
        line1 = "┌────┬───────────────┐┌─────┐ ┌────┬───────────────┐┌─────┐"
        line2 = f'│ {c[0]} │ {n1:<13}    {s1:>3} │ │ '
        line2 += f'{c[1]} │ {n2:<13}    {s2:>3}{" │"}'
        line3 = "└────┴───────────────┘└─────┘ └────┴───────────────┘└─────┘"
        scoreboard = "\n".join([line1, line2, line3])
        print(scoreboard)

    def get_input_from_shown_menu(self, title: str,
                                  question: str, options: list,
                                  legend=['Option', 'Actions']) -> str:
        menu = self._get_menu_layout(title, options, legend)
        menu += f"\n{question}"
        return input(menu)

    def display_highscore(self, scores: list, size: int):
        scores.sort(key=lambda row: (-row[1], -row[2]))
        line1 = "┌──────┬──────────────────────┬────────┬────────┐"
        line2 = f'│ {"Rank":^4} │ {"Names":^20} │ '
        line2 += f'{"Streak":^6} │ {"Points":^6} │'
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

    def display_any_key_continues(self):
        input('Press any key to contiue: ')

    def display_message_and_continues(self, msg: str):
        input(f'{msg}')

    def insert_line_breaks(self, numb=1):
        [print() for _ in range(numb)]

    def print_to_display(self, msg: str):
        print(msg)

    def display_paused_game_message(self, code: str):
        msg = '\nYour game session has been saved under the CodeName:\n\n'
        msg += '       ┌──────┐\n'
        msg += f'       │ {code} │\n'
        msg += '       └──────┘'
        msg += '\n\nUse this code (case sensitive) to resume your game.'
        msg += '\n\nSee you soon for another game of PIG!!\n'
        msg += '\nPress any key to go back to Start Up menu! '
        input(msg)

    def cpu_question_answer_animation(self, msg1: str, msg2: str):
        print(msg1, end=' ')
        time.sleep(1.5)
        print(msg2)
        time.sleep(0.5)

    def _shrink_name(self, name: str, max_len: int) -> str:
        return name if len(name) <= max_len else name[0:max_len - 3] + '...'

    def _get_rolls_points(self, points: int):
        line1 = ""
        line2 = "  ┌─────┐"
        line3 = f'{"= │"} {points:>3} │'
        line4 = "  └─────┘"
        line5 = ""
        return (line1, line2, line3, line4, line5)

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

    def _set_menu_header(self, title: str, width=40) -> str:
        header = f" {title} ".center(width, "~")
        return f'\n{header}'
