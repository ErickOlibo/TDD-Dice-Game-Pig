import uuid
from helpers import *
from player import Player
from event import Event
from winner import Winner
from gui import GUI
from brain import Brain
from dice import Dice
from typing import TypeVar
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
        self._participants = list[Player]
        self._hand = None # (name of the player)
        
        self._startup_options = [su.value for su in Start_Up if su.name != 'MENU']
        self._startup_options_dict = {su.value[0]:su for su in Start_Up if su.name != 'MENU'}
        #print(self._startup_options_dict)
        
        self._new_game_options = [m.value for m in Mode if m.name != 'MENU']
        self._new_game_options_dict = {m.value[0]:m for m in Mode if m.name != 'MENU'}
        #print(self._new_game_options_dict)
        
        self._settings_options = [s.value for s in Settings if s.name != 'MENU']
        self._settings_options_dict = {s.value[0]:s for s in Settings if s.name != 'MENU'}
        #print(self._settings_options_dict)
    
    
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

# POSSIBILITY TO CHANGE ALL BELOW INTO ONE METHOD
# TO DELETE LATER---
    # def show_startup_menu(self) -> Start_Up:
    #     self._gui.clear_terminal()
    #     title = 'START UP'
    #     legend = ['Option', 'Actions']
    #     question = 'Pick an option: '
    #     options = self._startup_options
    #     response = self._get_input_from_user(title, question, options, legend)
    #     return self._startup_options_dict[response.upper()]
    
    
    # def show_new_game_menu(self) -> Mode:
    #     self._gui.clear_terminal()
    #     title = 'NEW GAME'
    #     legend = ['Option', 'Actions']
    #     question = 'Pick an option: '
    #     options = self._new_game_options
    #     response = self._get_input_from_user(title, question, options, legend)
    #     return self._new_game_options_dict[response.upper()]
    
    
    # def show_in_game_settings(self) -> Settings:
    #     self._gui.clear_terminal()
    #     title = 'SETTINGS'
    #     legend = ['Option', 'Actions']
    #     question = 'Pick an option: '
    #     options = self._settings_options
    #     response = self._get_input_from_user(title, question, options, legend)
    #     return self._settings_options_dict[response.upper()]


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
        time.sleep(0.3)
    
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

        one = Player(n_one)
        two = Player(n_two)
        self._participants = list([one, two])
        

    def set_solo_player(self, mode: Mode):
        self.menu_transition()
        self._mode = mode
        ask = 'Enter your name: '
        one = Player(self._gui.get_simple_answer_from_user(ask, 'PLAYER'))
        cpu = Player('CPU', Brain(), Dice(mode))
        

    def play(self, codename = None):
        if codename is None:
            #play new Game
            print('NO CODENAME - NEW GAME')
        else:
            print(f'CODE NAME IS {codename}')
        time.sleep(4)
        
    
    def request_codename_from_user(self):
        self.menu_transition()
        ask = "Please Enter the Game's Code Name: "
        codename = self._gui.get_simple_answer_from_user(ask, 'CODE NAME')
        return codename
    