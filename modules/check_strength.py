from modules.libraries import Fore, Style

def check_password_strength(password):
    """
    This function checks the strength of a password based on its length.
    The strength is categorized into 'Weak', 'Medium', 'Strong', and 'Invalid'.

    Parameters:
    password (str): The password to check.

    Returns:
    str: A string indicating the strength of the password.
    """
    # Calculate the length of the password
    length = len(password)

    # Check the length and categorize the strength
    if 6 <= length <= 10:
        return f"{Fore.LIGHTRED_EX}Weak{Style.RESET_ALL}"
    elif 11 <= length <= 15:
        return f"{Fore.YELLOW}Medium{Style.RESET_ALL}"
    elif 16 <= length:
        return f"{Fore.LIGHTGREEN_EX}Strong{Style.RESET_ALL}"
    else:
        # If the password is less than 6 characters, it's considered invalid
        return f"{Fore.RED}[ Warning ] The Password Must Be More Than 6 Letters {Style.RESET_ALL}"