from modules.libraries import stdout
from modules.libraries import sleep

def simulate_typing(text, delay=0.03):
    """
    This function simulates the effect of typing out a string of text in real-time.
    It prints each character of the text to the console with a small delay between each character.

    Parameters:
    text (str): The text to print.
    delay (float): The delay in seconds between each character. Default is 0.03 seconds.

    Returns:
    None
    """
    # Iterate over each character in the text
    for char in text:
        # Write the character to the console
        stdout.write(char)
        # Flush the output buffer to ensure the character is displayed immediately
        stdout.flush()
        # Pause for a short delay to simulate the time taken to type the character
        sleep(delay)