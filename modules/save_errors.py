from modules.libraries import Fore, Style

def save_error(e):
    """
    This function saves the details of an exception into a file named 'Errors.txt'.
    It appends the error message at the end of the file and then prints an error message on the console.

    Parameters:
    e (Exception): The exception to log.

    Returns:
    None
    """
    # Define the error file
    error_file = "Errors.txt"
    # Open the file in append mode. If the file doesn't exist, it will be created.
    with open(error_file, "a") as f:
        # Write the string representation of the exception into the file
        f.write(str(e))
        # Add a newline for better readability of the file
        f.write("\n")
        # Flush the write buffer to ensure that the error is written immediately
        f.flush()
    # Print an error message on the console
    print(f"{Fore.RED}\n[ Error ] An error occurred. Check {error_file} for more information.{Style.RESET_ALL}")