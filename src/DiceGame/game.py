"""This module organizes and controls the process of the game."""
from helpers import Mode, Textual, Start_Up, Settings, Turn
from player import Player
from winner import Winner
from gui import GUI
from brain import Brain
from dice import Dice
from typing import TypeVar
import random
import time


class Game:
    """The main engine of the application."""

    def __init__(self, db):
        """Construct the necessary attributes for the game object."""
        self._database = db
        self._time_stamp = round(time.time())
        self._gui = GUI()
        self._codename = None
        self._mode = None
        self._p1 = None
        self._p2 = None
        self._hand = None
        self._target = 100
        self._winner = False
        self._back_from_settings = False
        self._has_quit = False

        self._startup_options = [
            su.value for su in Start_Up if su.name != 'MENU'
        ]
        self._startup_options_dict = {
            su.value[0]: su for su in Start_Up if su.name != 'MENU'
        }
        self._new_game_options = [
            m.value for m in Mode if m.name != 'MENU'
        ]
        self._new_game_options_dict = {
            m.value[0]: m for m in Mode if m.name != 'MENU'
        }
        self._settings_options = [
            s.value for s in Settings if s.name != 'MENU'
        ]
        self._settings_options_dict = {
            s.value[0]: s for s in Settings if s.name != 'MENU'
        }

    @property
    def mode(self) -> Mode:
        """
        Return the current game mode.

        Description:
        This property returns the current game mode, which is stored as an
        instance variable named _mode. The game mode determines the
        behavior of the game, such as the scoring system or the rules of
        play.

        Returns:
        - Mode: the current game mode.
        """
        return self._mode

    @mode.setter
    def mode(self, mode: Mode):
        if not isinstance(mode, Mode):
            raise TypeError('Mode must be SOLO or DUEL!')
        self._mode = mode

    @property
    def codename(self) -> str:
        """
        Return the code name of the game.

        This property returns the code name of the game, which is a unique
        identifier assigned to the game when it is created. The code name
        is stored as an instance variable named _codename.

        Returns:
        - str: the code name of the game.
        """
        return self._codename

    @codename.setter
    def codename(self, code: str):
        """
        Set the code name of the game.

        Description:
        This setter method updates the code name of the game to the
        specified value. The code name is a unique identifier assigned to
        the game when it is created, and is stored as an instance variable
        named _codename.

        Args:
        - code (str): the new code name to assign to the game.
        """
        self._codename = code

    def game_for_test(self, p1: Player, p2: Player, mode: Mode):
        """
        Set up a game instance for testing purposes.

        Descritpion:
        This method creates a new game instance with the specified players
        and mode, and assigns them to the instance variables _p1, _p2, and
        _mode, respectively. This method is intended for testing purposes
        only, and should not be used in production code.

        Args:
        - p1 (Player): the first player of the game.
        - p2 (Player): the second player of the game.
        - mode (Mode): the mode of the game.
        """
        self._p1 = p1
        self._p2 = p2
        self._mode = mode

    def display_rules(self):
        """
        Clear the terminal and displays the game rules.

        Description:
        This method clears the terminal and then displays the game rules
        using the GUI object's `display_info` method. The rules are
        retrieved from the `Textual` enumeration, which contains the text
        for various parts of the game. The maximum line length for the
        displayed text is set to 70 characters.

        """
        self._gui.clear_terminal()
        self._gui.insert_line_breaks(1)
        self._gui.display_info(Textual.RULES.value, 'RULES', 70)

    def show_highscore(self, scores, size=10):
        """
        Clear the terminal and displays the highscores.

        Using the given `scores` list.
                The `size` parameter determines the number of
                highscores to display.
                By default,it is set to 10.

        Args:
            - scores (list): A list of tuples, where each tuple represents
                             a player's name and their score.
            - size (int, optional): The number of highscores to display.
              Defaults to 10.
        """
        self._gui.clear_terminal()
        self._gui.display_highscore(scores, size)

    T = TypeVar("T")

    def show_menu(self, title: str, type: T) -> T:
        """
        Clear the terminal and displays a menu.

                  With the given `title` and `type` of options.
                  The `type` parameter must be an instance of one of
                  the following classes: `Start_Up`,
                  `Mode`, or `Settings`. The function returns the
                  user's selection from the options.

        Args:
            title (str): The title of the menu.
            type (T): An instance of one of the following
            classes: `Start_Up`, `Mode`, or `Settings`.

        Returns:
            T: The user's selection from the options,
               as specified by the `type` parameter.

        Raises:
            TypeError: If the `type` parameter is not an instance of
                      `Start_Up`, `Mode`, or `Settings`.
        """

        [title, q, opt, leg, opt_dict] = self._show_menu_offload(title, type)

        resp = self._get_input_from_user(title, q, opt, leg)
        return opt_dict[resp.upper()]

    def menu_transition(self):
        """Clear the terminal and creates a smooth transition between menus."""
        self._gui.clear_terminal()
        time.sleep(0.2)

    def set_player_one(self):
        """
        Set up the game for the player one.

        Description:
            This method prompts the player one to enter a name.
            The game mode is set to Mode.DUEL.

        """
        self.menu_transition()
        ask1 = 'Enter Player One name: '
        n_one = self._get_simple_answer(ask1, 'PLAYER ONE')
        self._p1 = Player(n_one)
    
    def set_player_two(self):
        """
        Set up the game for the player two.

        Description:
            This method prompts the player two to enter a name.
            In case the player enters the same name as player one,
            he/she will be prompt to choice another one.
            The game mode is set to Mode.DUEL.

        """
        self._mode = Mode.DUEL
        n_one = self._p1.name
        count = 0
        while True:
            self.menu_transition()
            count += 1
            ask2 = 'Enter Player Two name: '
            n_two = self._get_simple_answer(ask2, 'PLAYER TWO')
            n_two = f'{n_one} Jr.' if count >= 2 else n_two
            if n_two.lower() != n_one.lower():
                self._p2 = Player(n_two)
                break
            msg = '\nName is already taken by the PLAYER ONE.'
            msg += '\nTry again by pressing any keys! '
            print(msg)
            
            time.sleep(2)


    def set_solo_player(self, mode: Mode):
        """
        Set up the game for a single player.

        Description:
            This method prompts the user to enter their name,
            creates a Player object to represent them,
            and creates another Player object with the name "CPU".
            The game mode is set to the specified mode.

        Args:
            mode (Mode): The game mode to use.
        """
        ask = self._set_solo_player_offload(mode)
        self._p1 = Player(self._get_simple_answer(ask, 'PLAYER'))
        

    def play(self, codename=None):
        """
        Start playing a game.

        Description:
            This method starts a new game if no codename is provided,
            or resumes a paused game by loading its saved state from
            the database using the provided codename.
            If a new game is started, it determines whether the
            game is solo or dueling based on the name of the second player.
            Then, it starts the game loop by calling the
            _play_new_game() or _play_paused_game() method as appropriate.

        Args:
            codename (str, optional): The codename of the saved game to resume.
            If not provided, a new game is started.
        """
        if codename is None:
            is_solo = self._p2.name == 'CPU'
            self._play_new_game(is_solo)
        else:
            pg = self._database.load_game(codename)
            self._p1 = pg._p1
            self._p2 = pg._p2
            self._hand = pg._hand
            self.mode = pg.mode
            self._play_paused_game()

    def request_codename_from_user(self):
        """
        Display the current game state.

        Description:
            This method displays the current state of the game, including the
            scores of the players, the current hand, and any other relevant
            information. It uses the _gui object to display the information to
            the user.
        """
        self.menu_transition()
        ask = "Please Enter the Game's Code Name: "
        codename = self._get_simple_answer(ask, 'CODE NAME')
        return codename

    # PRIVATE METHODS
    def _play_paused_game(self):
        self.menu_transition()
        self._back_from_settings = True
        while not self._winner:
            if not self._has_quit:
                self._playing_a_turn()
            else:
                break

    def _get_input_from_user(self, title, ask, options, legend) -> str:
        choices = [k[0] for k in options]
        choices = set(choices + [k[0].lower() for k in options])
        count = 0
        while True:
            count += 1
            try:
                menu = self._gui.get_text_to_shown_menu(
                    title, ask, options, legend)
                choice = input(menu)
                if choice not in choices:
                    if count >= 2:
                        choice = '1'
                    else:
                     raise ValueError()
                    
            except ValueError:
                print('\nThis is not a valid option. Please try again!\n')
                time.sleep(1.5)
                self.menu_transition()
            else:
                return choice

    def _play_new_game(self, is_solo=False):
        self.menu_transition()
        if is_solo:
            self._hand = self._p1
        else:
            self._hand = random.choice([self._p1, self._p2])
        msg = self._intro_message()
        input(msg)
        while not self._winner:
            if not self._has_quit:
                self._playing_a_turn()
            else:
                break

    def _play_new_solo_game(self):
        self.menu_transition()
        self._hand = self._p1
        msg = self._intro_message()
        input(msg)

    def _change_hand(self):
        self._hand = self._p1 if self._hand != self._p1 else self._p2

    def _is_cpu_hand(self) -> bool:
        return self._hand.name == 'CPU'

    def _cpu_chosing(self) -> Turn:
        msg = self._roll_or_hold_message()
        msg = self._gui.get_simple_answer_from_cpu(msg, 'ROLL or HOLD')  #_DEF_
        score = self._p2.score
        pts = sum(self._p2.rolls)
        turn = self._p2.brain.action(score, pts)
        self._gui.cpu_question_answer_animation(msg, turn.value)  #_DEF_
        return turn

    # SLITTING Playing a turn
    def _start_of_turn_scoreboard(self):
        self.menu_transition()
        if not self._back_from_settings:
            self._hand.roll_dice()
        self._back_from_settings = False
        rolls = self._hand.rolls
        self._gui.display_scoreboard(
            self._p1.name, self._p1.score, self._p2.name,
            self._p2.score, self._hand.name)  #_DEF_
        pts = sum(rolls) if rolls[-1] != 1 else 0
        self._gui.display_hand_results_split(self._hand.rolls, pts)  #_DEF_

    def _resp_is_turn_hold_value(self):
        self._hand.add_points_to_score(sum(self._hand.rolls))
        if self._hand.score >= self._target:
            self._hold_for_win()
        else:
            self._choose_hold()

    def _resp_is_turn_settings(self, set_value: Settings):
        if set_value == Settings.BACK:
            self._back_from_settings = True

        if set_value == Settings.CHEAT:
            cheat_points = self._target - (self._hand.score + 1)
            self._hand.add_points_to_score(cheat_points)
            self._back_from_settings = True
        
        if set_value == Settings.QUIT:
            self._has_quit = True
            self.menu_transition()
            msg = '\nSad to see you go!.'
            msg += 'Came back again anytime!\n\n'
            self._gui.print_to_display(msg)
        
        if set_value == Settings.PAUSE:
            self._has_quit = True
            self.menu_transition()
            code = self._database.store_game(self)
            self.menu_transition()
            return code

        if set_value == Settings.NAME:
            self.menu_transition()
            old_name = self._hand.name
            question = 'Enter your new name: '
            label = f'CHANGING {old_name.upper()} TO'
            self._back_from_settings = True
            return [question, label]

    def _playing_a_turn(self):
        self._start_of_turn_scoreboard()
        if 1 in self._hand.rolls:
            self._rolled_one()
        else:
            while True:
                resp = self._resolve_hand_response()
                # if self._is_cpu_hand():
                #     resp = self._cpu_chosing().value
                # else:
                #     resp = self._get_simple_answer(
                #         self._roll_or_hold_message(), 'ROLL or HOLD').upper()

                if resp == Turn.HOLD.value:
                    self._resp_is_turn_hold_value()
                    break
                elif resp == Turn.ROLL.value:
                    break
                
                elif resp == Turn.SETTINGS.value:
                    choice = self.show_menu('IN-GAME SETTINGS', Settings.MENU)
                    self._resolve_show_settings_menu(choice)
                    # if choice == Settings.BACK:
                    #     self._resp_is_turn_settings(Settings.BACK)

                    # if choice == Settings.CHEAT:
                    #     self._resp_is_turn_settings(Settings.CHEAT)

                    # if choice == Settings.QUIT:
                    #     self._resp_is_turn_settings(Settings.QUIT)

                    # if choice == Settings.PAUSE:
                    #     code = self._resp_is_turn_settings(Settings.PAUSE)
                    #     msg = self._gui.display_paused_game_message(code)
                    #     input(msg)

                    # if choice == Settings.NAME:
                    #     [question, label] = self._resp_is_turn_settings(
                    #         Settings.NAME)
                    #     new_name = self._get_simple_answer(
                    #         question, label)
                    #     self._hand.name = new_name
                    #     self._database.update_winner_name(
                    #         self._hand.name, new_name)
                        
                    break
                else:
                    msg = f'\n[{resp}] Not a valid option. Try Again!'
                    self._gui.print_to_display(msg)

    def _resolve_show_settings_menu(self, choice: Settings):
        if choice == Settings.BACK:
            self._resp_is_turn_settings(Settings.BACK)

        if choice == Settings.CHEAT:
            self._resp_is_turn_settings(Settings.CHEAT)

        if choice == Settings.QUIT:
            self._resp_is_turn_settings(Settings.QUIT)

        if choice == Settings.PAUSE:
            code = self._resp_is_turn_settings(Settings.PAUSE)
            msg = self._gui.display_paused_game_message(code)
            input(msg)

        if choice == Settings.NAME:
            [question, label] = self._resp_is_turn_settings(
                Settings.NAME)
            new_name = self._get_simple_answer(
                question, label)
            self._hand.name = new_name
            self._database.update_winner_name(
                self._hand.name, new_name)


    def _resolve_hand_response(self) -> str:
        if self._is_cpu_hand():
            resp = self._cpu_chosing().value
        else:
            resp = self._get_simple_answer(
                self._roll_or_hold_message(), 'ROLL or HOLD').upper()
        return resp

        
    def _hold_for_win(self):
        self.menu_transition()
        msg = self._we_have_winner_message()
        self._winner = True
        input(msg)
        victor = Winner(self._hand.name, self._hand.score)
        self._database.add_winner(victor)

    def _choose_hold(self):
        sum_rolls = sum(self._hand.rolls)
        self._hand.reset_rolls()
        msg = self._hold_message(sum_rolls)

        if self._is_cpu_hand():
            self._gui.print_to_display(msg)
            time.sleep(2.5)
        else:
            input(msg)

    def _rolled_one(self) -> Turn:
        self._hand.reset_rolls()
        loss_msg = self._loss_message()

        if self._is_cpu_hand():
            self._gui.print_to_display(loss_msg)
            time.sleep(2.5)
        else:
            input(loss_msg)
        return Turn.LOSS

    def _intro_message(self) -> str:
        msg = Textual.NEW_START.value
        msg += f'\n\nWe have tossed a coin and [ {self._hand.name} ]'
        msg += ' is starting.!\n\nPress any key to start rolling! '
        return msg

    def _loss_message(self) -> str:
        msg = f"\nSorry {self._hand._name}! You rolled a [1]. "
        msg += "No points for you."
        self._change_hand()
        msg += f"\n\n{self._hand._name}, it's your turn"
        msg += "\nPress any key to start Rolling! "
        return msg

    def _roll_or_hold_message(self) -> str:
        msg = f"{self._hand.name}:\n\n▐ [ S ] - Settings\n▐"
        msg += " [ H ] - HOLD\n▐ [ R ] - ROLL\n\nYour Choice? "
        return msg

    def _hold_message(self, pts: int) -> str:
        msg = f'\nCongratulation {self._hand.name}!'
        msg += f' {pts} points. TOTAL: {self._hand.score}'
        self._change_hand()
        msg += f"\n\n{self._hand.name}, it's your turn"
        msg += "\nPress any key to start Rolling! "
        return msg

    def _we_have_winner_message(self) -> str:
        lines = []
        line = "┌───┐"
        line += " THE WINNER IS !! ".center(28, "~")
        line += "┌───┐"
        lines.append(line)
        line = "│ ● │                            │ ● │"
        lines.append(line)
        line = f"│ ● │ {self._hand.name.upper():^26} │ ● │"
        lines.append(line)
        line = "│ ● │                            │ ● │"
        lines.append(line)
        line = "└───┘"
        line += f" [ {self._hand.score} points ] ".center(28, "~")
        line += "└───┘"
        lines.append(line)
        msg = "\n".join(lines)
        msg += '\n\nCongratulations!! '
        msg += '\n\nPress any key to return to Main Menu'
        return msg

    # Deconstructing this large file. NOT THE BEST WAY. (PRIVATE METHODS)
    # But Time is of the essence.
    T = TypeVar("T")
    
    def _show_menu_offload(self, title: str, type: T):
        self._gui.clear_terminal()
        legend = ['Option', 'Actions']
        question = 'Pick an option: '
        title = title.upper().strip()
        if isinstance(type, Start_Up):
            opt = self._startup_options
            opt_dict = self._startup_options_dict
        elif isinstance(type, Mode):
            opt = self._new_game_options
            opt_dict = self._new_game_options_dict
        elif isinstance(type, Settings):
            opt = self._settings_options
            opt_dict = self._settings_options_dict
        return [title, question, opt, legend, opt_dict]

    def _set_solo_player_offload(self, mode: Mode):
        self.menu_transition()
        self._mode = mode
        ask = 'Enter your name: '
        self._p2 = Player('CPU', Brain(), Dice(mode))
        return ask
    
    def _get_simple_answer(self, ask: str, title: str, width=40) -> str:
        header = self._set_header(title, width)
        ask_input = "\n".join([header, ask])
        return input(ask_input)
    
    def _set_header(self, title: str, width: int) -> str:
        header = f" {title} ".center(width, "~")
        return f'\n{header}'

# GAME PROCESS TRAINING METHODS
    # def training_game(self):
    #     """Allow a fast track to the a game session."""
    #     self._mode = Mode.DUEL
    #     self._p1 = Player('Erick')
    #     self._p2 = Player('Robert')
    #     self._play_new_game()
