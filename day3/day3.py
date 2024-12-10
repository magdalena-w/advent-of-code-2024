"""
Script to find and compute the sum of all valid mul(X, Y) instructions in a file.
"""

import re

def find_mul(file_path):
    """
    Parses a file to find all valid mul(X, Y) patterns, multiplies the numbers, 
    and returns their total sum.

    Args:
        file_path (str): The path to the input file.

    Returns:
        int: Total sum of the multiplications.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        return 0
    except OSError as e:
        print(f"Error reading file: {e}")
        return 0

    pattern = r'mul\(\d+,\d+\)'
    matches = re.findall(pattern, content)

    total = 0
    for match in matches:
        # Extract numbers and calculate the product
        x, y = map(int, re.findall(r'\d+', match))
        total += x * y

    return total

if __name__ == "__main__":
    INPUT_FILE = 'day3/input.txt'
    result = find_mul(INPUT_FILE)
    print(f"Total sum: {result}")
