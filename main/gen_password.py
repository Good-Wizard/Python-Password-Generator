from modules.libraries import choice, ascii_letters, digits, punctuation, Fore, Style, sleep

def generate_password(length):
    try:
        """
        This function generates a random password of a given length.
        The password includes at least one letter, one digit, and one punctuation character.
        The password does not include similar, duplicate, or sequential characters.

        Parameters:
        length (int): The length of the password to generate.

        Returns:
        str: The generated password.
        """
        # Combine all possible characters into one string
        all_characters = ascii_letters + digits + punctuation

        # Ensure the password includes at least one letter, one digit, and one punctuation character
        password = choice(ascii_letters) + choice(digits) + choice(punctuation)

        # Generate the remaining characters randomly
        for _ in range(length - 3):
            password += choice(all_characters)

        # Replace any similar, duplicate, or sequential characters
        while any(char in password for char in 'il1Lo0O'):
            password = password.replace(choice('il1Lo0O'), choice(all_characters), 1)

        # Remove any sequential characters
        for i in range(len(password) - 2):
            if ord(password[i + 1]) - ord(password[i]) == 1 and ord(password[i + 2]) - ord(password[i + 1]) == 1:
                password = password.replace(password[i + 1], choice(all_characters), 1)

        # Return the generated password
        return password
    except ValueError as e:
        print(f"\n{Fore.RED}[ Error ] We Have a Trouble With Generate Password, Check Errors.txt{Style.RESET_ALL}")
        sleep(1)
        