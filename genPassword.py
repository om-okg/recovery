"""
Problem Statement: Generate a password for specified length of characters.
Input: Length of a password to be generated.
Process: Use the random library to generate a password from a pool of characters.
Output: A randomly generated password.
"""

import random  # Library for random generation
import string  # Library to work with string functions


def genPass(length=12, useUpper=True, useDigits=True, useSymbols=True):
    """
    Generates a random password of a given length using specified character sets.
    
    Parameters:
        length (int): The length of the password (default: 12).
        useUpper (bool): Include uppercase letters in the character pool.
        useDigits (bool): Include numeric digits in the character pool.
        useSymbols (bool): Include punctuation symbols in the character pool.
        
    Returns:
        str: The randomly generated password.
    """
    # Start with lowercase letters as the base character pool
    characters = string.ascii_lowercase
      
    if useUpper: 
        characters += string.ascii_uppercase

    if useDigits:
        characters += string.digits

    if useSymbols:
        characters += string.punctuation

    # Randomly select characters from the pool and join them together
    return "".join(random.choice(characters) for _ in range(length))
  
  
def main():
    print("Let's Generate your Password!\n")
    
    # Input the password length with a try-except block to handle invalid input
    try:
        inputLnt = input("Enter the length of your password (default 12): ").strip()
        lnt = int(inputLnt) if inputLnt else 12
    except ValueError:
        print("Invalid Input! Setting default length to 12.")
        lnt = 12

    # Generate and print the password
    secPass = genPass(lnt)
    print(f"\nYour generated password (length {lnt}): {secPass}")


if __name__ == "__main__":
    main() 
