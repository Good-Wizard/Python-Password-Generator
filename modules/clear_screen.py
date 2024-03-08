from modules.save_errors import save_error
from modules.libraries import os, system

def clear_screen():
    """
    This function clears the console screen.
    It checks the operating system name and uses the appropriate command to clear the screen.
    If an error occurs while clearing the screen, the error will be logged using the 'save_error' function.

    Parameters:
    None

    Returns:
    None
    """
    try:
        # Get the name of the operating system
        os_name = system()

        # Clear the console screen
        os.system("cls" if os_name == "Windows" else "clear")
    except ValueError as e:
        # If a ValueError occurs, save the error
        save_error(e)