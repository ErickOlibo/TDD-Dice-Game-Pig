"""This file is the entry point of the program."""
from game import Game
from gui import GUI
from helpers import Start_Up, Mode
from database import Database


def main():
    """
    Control the flow of the application.

    Description:
    This function controls the flow of the application,
    by starting an instance of Game, getting the user's option
    from the Start Up menu, handling the chosen option, and
    repeating the process until the user chooses to exit.

    Args:
    - None

    """
    while True:
        # 1 - Start an instance of Game
        db = Database()
        game = Game(db)
        gui = GUI()

        # 2 - Get the option from the user for the Start Up menu
        start_choice = game.show_menu('START UP', Start_Up.MENU)

        # 3 - Handle Chosen Option
        game.menu_transition()
        if start_choice == Start_Up.EXIT:
            break

        if start_choice == Start_Up.NEW_GAME:
            new_game_choice = game.show_menu('NEW GAME MODE', Mode.MENU)
            if new_game_choice == Mode.BACK:
                game.menu_transition()
                continue

            if new_game_choice == Mode.DUEL:
                game.set_player_one()
                game.set_player_two()
                game.play()

            solo_mode = [
                mode for mode in Mode if mode not in [Mode.DUEL, Mode.BACK]
                ]
            if new_game_choice in solo_mode:
                game.set_solo_player(new_game_choice)
                game.play()

        msg = 'Press any key to contiue: '
        if start_choice == Start_Up.RESUME_GAME:
            codename = game.request_codename_from_user()
            game.play(codename)

        if start_choice == Start_Up.HIGH_SCORE:
            game.show_highscore(db.highscore)
            input(msg)

        if start_choice == Start_Up.RULES:
            game.display_rules()
            input(msg)


if __name__ == "__main__":
    main()
