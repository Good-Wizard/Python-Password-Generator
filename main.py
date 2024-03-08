# Import necessary libraries
from modules.libraries import *
from modules.check_strength import check_password_strength
from modules.simulate_typing import simulate_typing
from modules.save_errors import save_error
from modules.clear_screen import clear_screen
from main.save_password import save_passwords
from main.show_passwords import print_saved_passwords
from main.gen_password import generate_password

# Initialize colorama
init()

def Menu():
# Main loop
    while True:
        try:
            # Clear the console screen
            clear_screen()

            # Print a welcome message and system information
            username = getuser()
            current_date = datetime.now().strftime("%Y-%m-%d")
            system_info = system()
            print(f"{Fore.YELLOW}\n{f"=" * 50}{Fore.YELLOW}\n\nUser: {Fore.MAGENTA}{username}  {Fore.YELLOW}Date: {Fore.MAGENTA}{current_date}  {Fore.YELLOW}System: {Fore.MAGENTA}{system_info}\n\n{Fore.GREEN}* Options *\n\n{Fore.BLUE}[ {Fore.RED}1{Fore.BLUE} ] Generate Password\n\n{Fore.BLUE}[ {Fore.RED}2{Fore.BLUE} ] Show My Saved Passwords\n\n{Fore.BLUE}[ {Fore.RED}3{Fore.BLUE} ] Exit\n{Style.RESET_ALL}{Fore.YELLOW}\n{f"=" * 50}")

            # Prompt the user to choose an option
            simulate_typing((f"{Fore.LIGHTBLACK_EX}\n\n--> Which One? "))
            user_choice = int(input())

            # If the user chooses to generate a password
            if user_choice == 1:
                main()

            # If the user chooses to view saved passwords
            elif user_choice == 2:
                while True:
                    # Prompt the user to enter the master password
                    verify_user = input(f"{Fore.YELLOW}\n[ ? ] Please Enter Master Password ( 0 For Back Menu ):{Fore.LIGHTBLACK_EX} ")

                    # If the entered password is correct
                    if verify_user == master_password:
                        print_saved_passwords()
                        input(f"\n{Fore.CYAN}[ + ] Press Enter For Back Menu...{Style.RESET_ALL}")
                        break
                    # If the user chooses to return to the main menu
                    elif verify_user == '0':
                        break

                    # If the entered password is incorrect
                    elif verify_user != master_password:
                        print(f"{Fore.RED}\n[ Error ] Invalid Master Password!{Style.RESET_ALL}")
                        sleep(1)

            # If the user chooses to exit the program
            elif user_choice == 3:
                clear_screen()
                exit()

            # If the user input is invalid
            else:
                print(f"\n{Fore.RED}[ Error ] Invalid input. Please enter a valid integer value.{Style.RESET_ALL}")
                sleep(2)

        # If a ValueError occurs, save the error
        except ValueError as e:
            print(f"\n{Fore.RED}[ Error ] Invalid input. Please enter a valid integer value.{Style.RESET_ALL}")
            sleep(1)
            save_error(e)
            continue

def main():
    """
    This function is the main driver of the password manager program.
    It provides an interactive console interface for the user to generate, save, and view passwords.
    If an error occurs during the execution of the program, the error will be logged using the 'save_error' function.

    Parameters:
    None

    Returns:
    None
    """
    try:
        # Initialize user choice
        user_choice3 = 1

        # Main loop
        while True:
            # Clear the console screen
            clear_screen()

            # Print password strength guidelines
            print(f"{Fore.BLUE}\n[ < 9 ]{Style.RESET_ALL} : {Fore.RED}Weak{Style.RESET_ALL}\n{Fore.BLUE}[ < 15 ]{Style.RESET_ALL} : {Fore.YELLOW}Medium{Style.RESET_ALL}\n{Fore.BLUE}[ 18 < ] {Style.RESET_ALL}:{Fore.LIGHTGREEN_EX} Strong{Style.RESET_ALL}")

            # Prompt the user to enter the password length
            password_length = int(input(f"\n{Style.RESET_ALL}{Fore.YELLOW}[ ? ] Enter the password length ( Maximum 50 ):{Fore.LIGHTBLACK_EX} "))

            # Validate the password length
            if password_length > 50:
                print(f"{Fore.RED}[ Error ] Maximum Length Is 50")
                sleep(1)
                continue
            elif password_length < 1:
                print(f"\n{Fore.RED}[ Error ] Invalid input. Please enter a valid integer value.{Style.RESET_ALL}")
                sleep(1)
                continue

            # Password generation loop
            while user_choice3 != 0:
                # Clear the console screen
                clear_screen()

                # Generate a password
                password = generate_password(password_length)

                # Copy the password to the clipboard
                copy(password)

                # Check the strength of the password
                strength = check_password_strength(password)

                # Print the generated password and its strength
                print(f"\n{Style.RESET_ALL}{Fore.BLUE}[ # ] Generated password --> {Style.RESET_ALL}{Fore.LIGHTWHITE_EX}{password}\n\n{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}[ Strength: {Style.RESET_ALL}{strength} ]{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}\n\n[ Successfully Copied! ]")

                # Prompt the user to save the password
                while True:
                    simulate_typing(f"{Style.RESET_ALL}{Fore.YELLOW}\n[ ? ] Wanna Save It? (y/n): {Fore.LIGHTBLACK_EX}")
                    save_choice = input()

                    # If the user chooses to save the password
                    if save_choice.lower() == 'y':
                        simulate_typing(f"\n{Style.RESET_ALL}{Fore.YELLOW}[ ? ] Please Enter Title For This Password : {Fore.LIGHTBLACK_EX}")
                        title = input()

                        # If a title is provided, save the password
                        if title:
                            save_passwords(password, title)

                    # If the user chooses not to save the password
                    elif save_choice.lower() == "n":
                        pass

                    # If the user input is invalid
                    else:
                        print(f"\n{Fore.RED}[ Error ] Invalid input. Please enter 'y' or 'n'.{Style.RESET_ALL}")
                        sleep(1)
                        continue

                    # Prompt the user to generate another password or return to the menu
                    while True:
                        print(f"\n{Style.RESET_ALL}{Fore.LIGHTCYAN_EX}[ {Fore.LIGHTGREEN_EX}1{Fore.LIGHTCYAN_EX} ] Generate Again {Fore.RED}OR{Fore.LIGHTCYAN_EX} [ {Fore.LIGHTGREEN_EX}2{Fore.LIGHTCYAN_EX} ] Back To Menu{Style.RESET_ALL}{Fore.YELLOW}")
                        simulate_typing(f"{Fore.YELLOW}\n--> {Fore.LIGHTBLACK_EX}Which One? ")
                        user_choice3 = input()
                        # If the user chooses to generate another password
                        if user_choice3 == '1':
                            break

                        # If the user chooses to return to the menu
                        elif user_choice3 == '2':
                            return

                        # If the user input is invalid
                        else:
                            print(f"\n{Fore.RED}[ Error ] Invalid input. Please enter '1' or '2'.{Style.RESET_ALL}")
                            sleep(1)
                            clear_screen()
                            continue
                    break
    except ValueError as e:
        print(f"\n{Fore.RED}[ Error ] Invalid input. Please enter a valid value.{Style.RESET_ALL}")
        sleep(1)
        # If a ValueError occurs, save the error
        save_error(e)

if __name__ == "__main__":
    try:
        # Define the master password
        master_password = "test"
        """
        This is the main execution block that runs when the script is run directly.
        It provides an interactive console interface for the user to generate, save, and view passwords.
        If an error occurs during the execution of the program, the error will be logged using the 'save_error' function.
        """
        Menu()
    except ValueError as e:
        # If a ValueError occurs, save the error
        print(f"\n{Fore.RED}[ Error ] Invalid input. Please enter a valid integer value.{Style.RESET_ALL}")
        sleep(1)
        save_error(e)
