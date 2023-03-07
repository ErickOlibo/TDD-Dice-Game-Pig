from helpers import *
from player import Player
from event import Event
from winner import Winner
from gui import GUI
from brain import Brain
from dice import Dice
from typing import TypeVar
import random
import time


class Game:
    """ 
        A instance of a game played. It has all the rules, 
        More to add to the docstring
        ** --> is there a possibility to simulate the CPU playing:
            (delay, print choice same line, etc..)
    """

    
    def __init__(self):
        self._time_stamp = round(time.time())  # sorting Games chronologically
        self._gui = GUI()
        self._codename = None # Only for game in a suspended state
        self._mode = None
        self._p1 = None
        self._p2 = None
        self._hand = None
        self._target = 20 #100
        
        self._startup_options = [su.value for su in Start_Up if su.name != 'MENU']
        self._startup_options_dict = {su.value[0]:su for su in Start_Up if su.name != 'MENU'}
        
        self._new_game_options = [m.value for m in Mode if m.name != 'MENU']
        self._new_game_options_dict = {m.value[0]:m for m in Mode if m.name != 'MENU'}
        
        self._settings_options = [s.value for s in Settings if s.name != 'MENU']
        self._settings_options_dict = {s.value[0]:s for s in Settings if s.name != 'MENU'}
    
    
    @property
    def winner(self) -> Winner:
        return self._winner
    
    @winner.setter
    def winner(self, winner: Winner):
        if not isinstance(winner, Winner):
            raise TypeError('name must be a string!')
        self._winner= winner
        
    @property
    def mode(self) -> Mode:
        return self._mode
    
    @mode.setter
    def mode(self, mode: Mode):
        if not isinstance(mode, Mode):
            raise TypeError('Mode must be SOLO or DUEL!')
        self._mode = mode


    def display_rules(self):
        self._gui.clear_terminal()
        self._gui.insert_line_breaks(1)
        self._gui.display_info(Textual.RULES.value, 'RULES', 70)
 

    
    def show_highscore(self, scores, size = 10):
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

    
    def _get_input_from_user(self, title, ask, options, legend) -> str:
        choices = [k[0] for k in options]
        choices = set(choices + [ k[0].lower() for k in options])
        while True:
            try:
                choice = self._gui.get_input_from_shown_menu(
                    title, ask, options, legend)
                if choice not in choices: raise ValueError()
            except ValueError:
                print('\nThis is not a valid option. Please try again!\n')
                time.sleep(2)
                self.menu_transition()
            else:
                return choice
    
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
            if n_two.lower() != n_one.lower(): break
            self._gui.display_message_and_continues(
                f'\n[{n_two}] is already taken by the PLAYER ONE.\nTry again by pressing any keys! ')
            self.menu_transition()

        self._p1 = Player(n_one)
        self._p2 = Player(n_two)
        

    def set_solo_player(self, mode: Mode):
        self.menu_transition()
        self._mode = mode
        ask = 'Enter your name: '
        self._p1 = Player(self._gui.get_simple_answer_from_user(ask, 'PLAYER'))
        self._p2 = Player('CPU', Brain(), Dice(mode))


    def play(self, codename = None):
        if codename is None:
            #play new Game
            print('NO CODENAME - NEW GAME')
            self._play_new_game()
        else:
            print(f'CODE NAME IS {codename}')
        time.sleep(4)
        
    
    def request_codename_from_user(self):
        self.menu_transition()
        ask = "Please Enter the Game's Code Name: "
        codename = self._gui.get_simple_answer_from_user(ask, 'CODE NAME')
        return codename
    
    
    def _play_new_game(self):
        self.menu_transition()
        # DISPLAY GAME INTRO
        self._hand = random.choice([self._p1, self._p2])

        msg = self._intro_message()
        self._gui.display_message_and_continues(msg)
        
        # RUN GAME TILL SOMEONE REACHES TARGET
        while self._p1.score < self._target or self._p2.score < self._target:
            self._playing_round()
            
        # Declare the winner (save to winner list)
        # Send back a Winner object or game codename to Main.py
        # 
    
    
    def _playing_turn(self):
        self.menu_transition()
        state = Turn.ROLL
        while state is Turn.ROLL:
            self._hand.roll_dice()
            rolls = self._hand.rolls
            self._gui.display_scoreboard(self._p1.name, self._p1.score,
                                         self._p2.name, self._p2.score, 
                                         self._hand.name)

            pts = sum(rolls) if rolls[-1] != 1 else 0
            self._gui.display_hand_results_split(self._hand.rolls, pts)
            
            if rolls[-1] == 1: 
                state = self._rolled_one()
            
            else:
                while True:
                    resp = self._gui.get_simple_answer_from_user(
                        self._roll_or_hold_message(), 'ROLL or HOLD').upper()
                    
                    if resp == Turn.HOLD.value:
                        state = self._choose_hold()
                        break
                    
                    elif resp == Turn.ROLL.value:
                        state = Turn.ROLL
                        break
                    
                    elif resp == Turn.SETTINGS.value:
                        pass
                    
                    else:
                        self._gui.print_to_display(f'\n[{resp}] Not a valid option. Try Again!')
        
            #time.sleep(3)
            #self.menu_transition()
            
        
        
        
        pass
    
    # def _message_view_prep(self):
    #     p = self._hand.name
    #     msg = f"{p} choice: [ S ] Settings ░ [ H ] HOLD ░ [ R ] ROLL ? "
    #     pass
    
    # def _rolls_view_prep(self):
        
    #     pass
    
    def _change_hand(self):
        self._hand = self._p1 if self._hand != self._p1 else self._p2
    
    # To get to the playing directly
    def training_game(self):
        self._mode = Mode.DUEL
        self._p1 = Player('Erick')
        self._p2 = Player('Robert')
        self._play_new_game()
        pass
    

    def _playing_round(self):
        self.menu_transition()
        self._hand.roll_dice()
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
                resp = self._gui.get_simple_answer_from_user(
                    self._roll_or_hold_message(), 'ROLL or HOLD').upper()

                if resp == Turn.HOLD.value:
                    self._choose_hold()
                    break
                
                elif resp == Turn.ROLL.value:
                    break
                
                elif resp == Turn.SETTINGS.value:
                    pass
                
                else:
                    self._gui.print_to_display(f'\n[{resp}] Not a valid option. Try Again!')
                    
                
                    
    
    
    
    def _choose_hold(self) -> Turn:
        pts = sum(self._hand.rolls)
        self._hand.add_points_to_score(pts)
        self._hand.reset_rolls()
        msg = self._hold_message(pts)
        self._gui.display_message_and_continues(msg)
        return Turn.ROLL
        
    
    def _choose_settings(self):
        pass
    
    
    def _rolled_one(self) -> Turn:
        self._hand.reset_rolls()
        loss_msg = self._loss_message()
        self._gui.display_message_and_continues(loss_msg)
        return Turn.LOSS
        
        
    
    def _intro_message(self,) -> str:
        msg = Textual.NEW_START.value
        msg += f'\n\nWe have tossed a coin and {self._hand.name} is starting.!'
        msg += f'\n\nPress any key to start rolling! '
        return msg
    
    
    def _loss_message(self) -> str:
        msg = f"\nSorry {self._hand._name}! You rolled a [1]. No points for you."
        self._change_hand()
        msg += f"\n\n{self._hand._name}, it's your turn"
        msg += f"\nPress any key to start Rolling! "
        return msg
    
    def _roll_or_hold_message(self) -> str:
        msg = f"{self._hand.name}:\n\n▐ [ S ] - Settings\n▐"
        msg += " [ H ] - HOLD\n▐ [ R ] - ROLL\n\nYour Choice? "
        return msg
    
    
    def _hold_message(self, pts: int) -> str:
        msg = f'\nCongratulation {self._hand.name}! {pts} points. TOTAL: {self._hand.score}'
        self._change_hand()
        msg += f"\n\n{self._hand.name}, it's your turn"
        msg += f"\nPress any key to start Rolling! "
        return msg

