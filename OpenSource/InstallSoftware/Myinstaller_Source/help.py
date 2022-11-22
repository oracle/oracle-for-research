from termcolor import colored

def help_function():


    """
    Display how to use instructions

    :return: None
    """


    right_arrow = colored("Right Arrow", "blue")
    left_arrow = colored("Left Arrow", "cyan")
    up_arrow = colored("Up Arrow", "yellow")
    down_arrow = colored("Down Arrow", "magenta")
    enter_key = colored("Enter Key", "green")
    how_to_use = colored("HOW TO USE THE INSTALLER", "red")


    help_txt = """
    + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
    +                                                                     +
    +                                                                     +
    +                   {5}                          +
    +                                                                     +
    +                                                                     +
    +           * Keyboard {0} - Select an item                   +
    +           * Keyboard {1}  - Unselect an item                 +
    +           * Keyboard {2}    - Move up the menue                +
    +           * Keyboard {3}  - Move down the menue              +
    +           * Keyboard {4}   - Confirm your selection           +
    +                                                                     +
    +                                                                     +
    + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
    """.format(right_arrow, left_arrow, up_arrow, down_arrow, enter_key, how_to_use)

    print(help_txt)
    input("Press the ENTER KEY to continue ")
    return None
