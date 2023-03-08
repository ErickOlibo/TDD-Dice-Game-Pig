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

    def __init__(self, db):
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
        return self._mode

    @mode.setter
    def mode(self, mode: Mode):
        if not isinstance(mode, Mode):
            raise TypeError('Mode must be SOLO or DUEL!')
        self._mode = mode

    @property
    def codename(self) -> str:
        return self._codename

    @codename.setter
    def codename(self, code: str):
        self._codename = code

    def game_for_test(self, p1: Player, p2: Player, mode: Mode):
        self._p1 = p1
        self._p2 = p2
        self._mode = mode

    def display_rules(self):
        self._gui.clear_terminal()
        self._gui.insert_line_breaks(1)
        self._gui.display_info(Textual.RULES.value, 'RULES', 70)

    def show_highscore(self, scores, size=10):
        self._gui.clear_terminal()
        self._gui.display_highscore(scores, size)

    T = TypeVar("T")

    def show_menu(self, title: str, type: T) -> T:
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

        resp = self._get_input_from_user(title, question, opt, legend)
        return opt_dict[resp.upper()]

    def menu_transition(self):
        self._gui.clear_terminal()
        time.sleep(0.2)

    def press_any_keys_to_continue(self):
        self._gui.display_any_key_continues()
        self.menu_transition()

    def set_duel_players(self):
        self.menu_transition()
        self._mode = Mode.DUEL
        ask1 = 'Enter Player One name: '
        ask2 = 'Enter Player Two name: '
        n_one = self._gui.get_simple_answer_from_user(ask1, 'PLAYER ONE')
        self.menu_transition()
        while True:
            n_two = self._gui.get_simple_answer_from_user(ask2, 'PLAYER TWO')
            if n_two.lower() != n_one.lower():
                break
            msg = f'\n[{n_two}] is already taken by the PLAYER ONE.'
            msg += '\nTry again by pressing any keys! '
            self._gui.display_message_and_continues(msg)
            self.menu_transition()
        self._p1 = Player(n_one)
        self._p2 = Player(n_two)

    def set_solo_player(self, mode: Mode):
        self.menu_transition()
        self._mode = mode
        ask = 'Enter your name: '
        self._p1 = Player(self._gui.get_simple_answer_from_user(ask, 'PLAYER'))
        self._p2 = Player('CPU', Brain(), Dice(mode))

    def play(self, codename=None):
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
        self.menu_transition()
        ask = "Please Enter the Game's Code Name: "
        codename = self._gui.get_simple_answer_from_user(ask, 'CODE NAME')
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
        while True:
            try:
                choice = self._gui.get_input_from_shown_menu(
                    title, ask, options, legend)
                if choice not in choices:
                    raise ValueError()
            except ValueError:
                print('\nThis is not a valid option. Please try again!\n')
                time.sleep(2)
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
        self._gui.display_message_and_continues(msg)
        while not self._winner:
            if not self._has_quit:
                self._playing_a_turn()
            else:
                break

    def _play_new_solo_game(self):
        self.menu_transition()
        self._hand = self._p1
        msg = self._intro_message()
        self._gui.display_message_and_continues(msg)

    def _change_hand(self):
        self._hand = self._p1 if self._hand != self._p1 else self._p2

    def _is_cpu_hand(self) -> bool:
        return self._hand.name == 'CPU'

    def _cpu_chosing(self) -> Turn:
        msg = self._roll_or_hold_message()
        msg = self._gui.get_simple_answer_from_cpu(msg, 'ROLL or HOLD')
        score = self._p2.score
        pts = sum(self._p2.rolls)
        turn = self._p2.brain.action(score, pts)
        self._gui.cpu_question_answer_animation(msg, turn.value)
        return turn

    def _playing_a_turn(self):
        self.menu_transition()
        if not self._back_from_settings:
            self._hand.roll_dice()
        self._back_from_settings = False
        rolls = self._hand.rolls
        self._gui.display_scoreboard(
            self._p1.name, self._p1.score, self._p2.name,
            self._p2.score, self._hand.name)
        pts = sum(rolls) if rolls[-1] != 1 else 0
        self._gui.display_hand_results_split(self._hand.rolls, pts)
        if rolls[-1] == 1:
            self._rolled_one()
        else:
            while True:
                if self._is_cpu_hand():
                    resp = self._cpu_chosing().value
                else:
                    resp = self._gui.get_simple_answer_from_user(
                        self._roll_or_hold_message(), 'ROLL or HOLD').upper()

                if resp == Turn.HOLD.value:
                    self._hand.add_points_to_score(sum(self._hand.rolls))
                    if self._hand.score >= self._target:
                        self._hold_for_win()
                        break
                    else:
                        self._choose_hold()
                        break
                elif resp == Turn.ROLL.value:
                    break
                elif resp == Turn.SETTINGS.value:
                    choice = self.show_menu('IN-GAME SETTINGS', Settings.MENU)
                    if choice == Settings.BACK:
                        self._back_from_settings = True
                        break

                    if choice == Settings.CHEAT:
                        cheat_points = self._target - (self._hand.score + 1)
                        self._hand.add_points_to_score(cheat_points)
                        self._back_from_settings = True
                        break

                    if choice == Settings.QUIT:
                        self._has_quit = True
                        self.menu_transition()
                        msg = '\nSad to see you go!.'
                        msg += 'Came back again anytime!\n\n'
                        self._gui.print_to_display(msg)
                        break

                    if choice == Settings.PAUSE:
                        self._has_quit = True
                        self.menu_transition()
                        code = self._database.store_game(self)
                        self.menu_transition()
                        self._gui.display_paused_game_message(code)
                        break

                    if choice == Settings.NAME:
                        self.menu_transition()
                        old_name = self._hand.name
                        question = 'Enter your new name: '
                        label = f'CHANGING {old_name.upper()} TO'
                        new_name = self._gui.get_simple_answer_from_user(
                            question, label)
                        self._hand.name = new_name
                        self._database.update_winner_name(old_name, new_name)
                        self._back_from_settings = True
                        break
                else:
                    msg = f'\n[{resp}] Not a valid option. Try Again!'
                    self._gui.print_to_display(msg)

    def _hold_for_win(self):
        self.menu_transition()
        msg = self._we_have_winner_message()
        self._winner = True
        self._gui.display_message_and_continues(msg)
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
            self._gui.display_message_and_continues(msg)

    def _rolled_one(self) -> Turn:
        self._hand.reset_rolls()
        loss_msg = self._loss_message()
        self._gui.display_message_and_continues(loss_msg)
        return Turn.LOSS

    def _intro_message(self,) -> str:
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

# GAME PROCESS TRAINING METHODS
    def training_game(self):
        self._mode = Mode.DUEL
        self._p1 = Player('Erick')
        self._p2 = Player('Robert')
        self._play_new_game()
