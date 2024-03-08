from modules.libraries import sqlite3, Fore, Style, sleep
from modules.save_errors import save_error

def save_passwords(password, title):
    """
    This function saves a password and its associated title into a SQLite database.
    The database file is named 'Passwords.db' and the table is named 'Passwords'.
    If the table doesn't exist, it will be created.
    If an error occurs while saving the password, the error will be logged using the 'save_error' function.

    Parameters:
    password (str): The password to save.
    title (str): The title associated with the password.

    Returns:
    None
    """
    try:
        # Define the database file
        db_file = "Passwords.db"
        # Connect to the SQLite database. If the database doesn't exist, it will be created.
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        # Create the table if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS Passwords (title text, password text)''')
        # Insert the title and password into the table
        c.execute("INSERT INTO Passwords (title, password) VALUES (?, ?)", (title, password))
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        # Print a success message
        print(f"\n{Fore.YELLOW}[ + ] {Fore.LIGHTGREEN_EX}Password Saved!{Style.RESET_ALL}")
    except sqlite3.OperationalError as e:
        # If an OperationalError occurs, print an error message
        print(f"{Fore.RED}\n[ Error ] Table already exists.{Style.RESET_ALL}")
    except ValueError as e:
        print(f"\n{Fore.RED}[ Error ] We Got Error With Save Your Password, Check Errors.txt{Style.RESET_ALL}")
        sleep(1)
        # If a ValueError occurs, save the error
        save_error(e)