"""
Problem Statement: Use a hashing algorithm on a file and hash it.
Input: 1) Path to the file and 2) Hashing algorithm (e.g., SHA256, MD5)
Process: 
    1. Dynamically fetch the algorithm function using the hashlib library.
    2. Read the file in binary chunks to handle large files efficiently.
    3. Update the hash object and compute the hexadecimal digest.
Output: Hashed value of the file.
"""

import hashlib
import os
import sys

def hash(path, algorithm="sha256"):
    """
    Computes the cryptographic hash of a file using the specified algorithm.
    
    Parameters:
        path (str): The file system path to the target file.
        algorithm (str): The name of the hashing algorithm (default: 'sha256').
        
    Returns:
        str: The hexadecimal hash digest of the file, or None if an error occurs.
    """
    # Fetch the hashing function dynamically from hashlib
    hashfun = getattr(hashlib, algorithm.lower(), None)
    if not hashfun:
        raise ValueError(f"Invalid algorithm: {algorithm.upper()}")
        
    # Initialize the hasher instance
    hasher = hashfun()
    
    try:
        # Open the file in binary read mode and read in 8KB chunks for memory efficiency
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
        
    except FileNotFoundError:
        print(f"Error: File not found at '{path}'")
        return None
        
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'")
        return None                


def main():
    print("Let us hash a file!!\n")
    
    # Prompt user for file path and validate it
    path = input("Enter the file path: ").strip()
    if not os.path.isfile(path):
        print(f"Invalid path entered: {path}")
        return
        
    print("\nSelect the Algorithm:\n1. SHA256 (Default)\n2. MD5")
    choice = input("Select between 1/2: ").strip() or "1"
    
    # Map user choice to algorithm name
    algo = "md5" if choice == "2" else "sha256"
    
    # Compute and display the hash
    file_hash = hash(path, algo)
    if file_hash:
        print(f"\nComputing {algo.upper()} hash...")
        print(f"Result: {file_hash}")    


if __name__ == "__main__":
    main()
