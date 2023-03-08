"""This module display info and interacts with the user."""
import os
from helpers import DIE_HEIGHT, DICE_FACES, DIE_SEP
import time


class GUI:

    def clear_terminal(self):
        """
        Function: Clear the terminal window.

        Description:
            This method clears the contents of the terminal using the 'clear'
            command from the os module. It is used to provide a clean slate for
            displaying new information to the user.

        """
        os.system('clear')

    def display_info(self, text: str, title: str, width=40):
        """
        Function: Display information to the user.

        Description:
            This method displays the provided text and title to the user,
            formatted with a header created by the _set_menu_header() method.
            The width of the header can be customized using the width argument.
            The text is printed to the console using the print() function.

        Args:
            text (str): The text to display to the user.
            title (str): The title of the information being displayed.
            width (int, optional): The width of the header. Default is 40.
        """
        header = self._set_menu_header(title, width)
        info = "".join([header, text])
        print(info)

    def get_simple_answer_from_user(self, ask: str,
                                    title: str, width=40) -> str:
        """
        Function: Get a simple user input.

        Description:
            This method displays a question to the user, along with a
            formatted title header created by the _set_menu_header() method.
            The user's response is read from the console using the input()
            function and returned as a string.

        Args:
            ask (str): The question to ask the user.
            title (str): The title of the input being requested.
            width (int, optional): The width of the header. Default is 40.

        Returns:
            str: The user's input as a string.
        """
        header = self._set_menu_header(title, width)
        ask_input = "\n".join([header, ask])
        return input(ask_input)

    def get_simple_answer_from_cpu(self, ask: str,
                                   title: str, width=40) -> str:
        """
        Function: Get a simple response from the CPU.

        Description:
            This method displays a question to the CPU player, along with a
            formatted title header created by the _set_menu_header() method.
            The CPU's response is returned as a string.

        Args:
            ask (str): The question to ask the CPU.
            title (str): The title of the response being requested.
            width (int, optional): The width of the header. Default is 40.

        Returns:
            str: The CPU's response as a string.
        """

        header = self._set_menu_header(title, width)
        ask_input = "\n".join([header, ask])
        return ask_input

    def display_hand_results(self, numbers: list, points: int):
        """
        Function: Display the results of a dice roll.

        Description:
            This method takes a list of roll results and their point value,
            and formats them for display in a graphical representation of the
            dice faces. The resulting display is printed to the terminal.

        Args:
            numbers (list): A list of integers representing the face values
                            of the dice rolled.
            points (int): The total point value of the roll.

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
        """
        Function: Display the results of a hand of dice, split into chunks.

        Description:
        This method takes a list of integers representing the dice rolls,
        a total number of points, and an optional split parameter which
        determines how many dice should be displayed on each line.
        The method splits the dice rolls into chunks of size `split`,
        then displays the results of each chunk separately.
        The results of each chunk are displayed using the `DICE_FACES`
        constant, with a row of points displayed underneath the dice faces.

        Args:
        - numbers (list): A list of integers representing the dice rolls.
        - points (int): The total number of points for the hand.
        - split (int): An optional parameter which determines how many dice
          should be displayed on each line. Defaults to 4.
        """

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
        """
        Function: Display a scoreboard with two players' names, scores,
                  and current hand.

        Description:
        This method takes in the names and scores of two players,
        as well as the name of the player whose turn it is.
        It then generates a graphical scoreboard displaying the two players'
        names and scores, along with an indication of whose turn it is.
        The scoreboard is printed to the console.

        Args:
            n1 (str): The name of player 1.
            s1 (int): The score of player 1.
            n2 (str): The name of player 2.
            s2 (int): The score of player 2.
            hand (str): The name of the player whose turn it is.

        """
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
        """
        Function: Get user input from a shown menu

        Description:
        This method displays a menu with the given title and options,
        and prompts the user with the given question to select an option.
        The method returns the user's input as a string.

        Args:
        - title (str): The title to display at the top of the menu.
        - question (str): The prompt to display to the user.
        - options (list): A list of strings representing the menu options.
        - legend (list): An optional list of strings that specify the column
          headings of the menu. Defaults to ['Option', 'Actions'].

        Returns:
        - input (str): The user's input as a string.
        """
        menu = self._get_menu_layout(title, options, legend)
        menu += f"\n{question}"
        return input(menu)

    def display_highscore(self, scores: list, size: int):
        """
        Function: Display high scores in a tabular format.

        Description:
        This method takes a list of high scores,
        displays them in a tabular format,
        with columns for rank, name, streak, and points.
        The table is sorted by the streak,
        and points columns in descending order.
        The number of scores displayedis determined by the `size` parameter.

        Args:
        - scores (list): A list of tuples containing the player name,
                         streak, and points.
        - size (int): The number of high scores to display.

        """
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
        """

        Display a message that prompts the user to press any key to continue.

         """
        input('Press any key to contiue: ')

    def display_message_and_continues(self, msg: str):
        """
        Displays a message to the user and waits for any key press to continue.

        Args:
            msg (str): The message to display to the user.

        """
        input(f'{msg}')

    def insert_line_breaks(self, numb=1):
        """
        Function: Inserts one or more line breaks into the console output.

        Description:
        This method inserts a specified number of line breaks
        into the console output.

        Args:
        - numb (int): An optional parameter which determines the number
                      of line breaks to insert into the console output.
                      Defaults to 1.
        """
        [print() for _ in range(numb)]

    def print_to_display(self, msg: str):
        """

        Function: Print a message to the console.

        Description:
        This method takes a message string as input and prints it to the
        console.

        Args:
         - msg (str): The message to be printed.

        """
        print(msg)

    def display_paused_game_message(self, code: str):
        """
        Function: Display a message to the console and prompt for input.

        Description:
        This method displays a message to the console along with a code,
        and prompts the user to input any key to continue.

        Args:
        - code (str): The code for the paused game session.

        """
        msg = '\nYour game session has been saved under the CodeName:\n\n'
        msg += '       ┌──────┐\n'
        msg += f'       │ {code} │\n'
        msg += '       └──────┘'
        msg += '\n\nUse this code (case sensitive) to resume your game.'
        msg += '\n\nSee you soon for another game of PIG!!\n'
        msg += '\nPress any key to go back to Start Up menu! '
        input(msg)

    def cpu_question_answer_animation(self, msg1: str, msg2: str):
        """
        Function: Print animation to console.

        Description:
        This method takes two message strings as input and prints the first,
        message with a delay of 1.5 seconds,
        and then prints the second message with a delay of 0.5 seconds.

        Args:
        - msg1 (str): The first message to be printed.
        - msg2 (str): The second message to be printed.
        """
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
