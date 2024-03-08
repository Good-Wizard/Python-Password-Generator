from modules.libraries import sqlite3, Fore, Style, sleep, PrettyTable
from modules.clear_screen import clear_screen
from modules.save_errors import save_error

def print_saved_passwords():
    """
    This function retrieves and prints all saved passwords from a SQLite database.
    The database file is named 'Passwords.db' and the table is named 'Passwords'.
    The passwords are printed in a table with the columns 'Index', 'Title', and 'Password'.
    If an error occurs while retrieving the passwords, an error message is printed.

    Parameters:
    None

    Returns:
    None
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("Passwords.db")
        c = conn.cursor()

        # Retrieve all records from the table
        c.execute("SELECT * FROM Passwords")
        data = c.fetchall()

        # Clear the console screen
        clear_screen()

        # Create a table with headers
        table = PrettyTable([f"{Fore.MAGENTA}Index{Style.RESET_ALL}", f"{Fore.YELLOW}Title{Style.RESET_ALL}", f"{Fore.LIGHTGREEN_EX}Password{Style.RESET_ALL}"])

        # Add each password to the table
        for i, (title, password) in enumerate(data):
            table.add_row([i+1, title, password])

        # Print the table
        print(Style.RESET_ALL, table)

        # Close the connection
        conn.close()

    except sqlite3.OperationalError as e:
        # If an OperationalError occurs, print an error message
        print(f"\n{Fore.RED}[ Error ] Could not retrieve data from the database or no passwords have been saved yet!{Style.RESET_ALL}")
        sleep(1)
    except ValueError as e:
        print(f"\n{Fore.RED}[ Error ] We Got Error With Show Your Passwords, Check Errors.txt{Style.RESET_ALL}")
        sleep(1)
        save_error(e)