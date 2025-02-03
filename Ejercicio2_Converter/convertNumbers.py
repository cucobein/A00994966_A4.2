"""
convertNumbers.py

This program reads a file containing numbers and converts them to:
- Binary (Base 2)
- Hexadecimal (Base 16)

The results are printed on the screen and saved in a file.

Usage:
    python3 convertNumbers.py data.txt
"""

import sys
import time

def read_numbers(file_name):
    """
    Reads a file and returns a list of valid numbers.
    
    - If the file contains invalid data (text), it shows an error message.
    - If the file does not exist, it stops the program.
    """
    numbers = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    number = int(line.strip())  # Convert to integer
                    numbers.append(number)
                except ValueError:
                    print(f"❌ Error: '{line.strip()}' is not a valid number.")
    except FileNotFoundError:
        print(f"❌ Error: The file '{file_name}' does not exist.")
        sys.exit(1)

    return numbers

def convert_to_binary(number):
    """
    Converts a decimal number to binary (Base 2).
    Returns a string representation of the binary number.
    """
    binary = ""
    if number == 0:
        return "0"
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary

def convert_to_hexadecimal(number):
    """
    Converts a decimal number to hexadecimal (Base 16).
    Returns a string representation of the hexadecimal number.
    """
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    if number == 0:
        return "0"
    while number > 0:
        remainder = number % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        number //= 16
    return hexadecimal

def write_results_to_file(numbers, binary_numbers, hexadecimal_numbers, execution_time):
    """
    Writes the conversion results to a file named 'ConvertionResults.txt'.
    """
    with open("ConvertionResults.txt", "w", encoding="utf-8") as file:
        file.write("Conversion Results:\n")
        file.write("Decimal | Binary | Hexadecimal\n")
        file.write("---------------------------------\n")
        for num, binary, hex_value in zip(numbers, binary_numbers, hexadecimal_numbers):
            file.write(f"{num:<8} | {binary:<16} | {hex_value:<8}\n")

        file.write("\n---------------------------------\n")
        file.write(f"Execution Time: {execution_time:.4f} seconds\n")

def main():
    """Main function of the program."""
    if len(sys.argv) != 2:
        print("Usage: python3 convertNumbers.py file.txt")
        sys.exit(1)

    data_file = sys.argv[1]
    numbers = read_numbers(data_file)

    if not numbers:
        print("No valid numbers found in the file.")
        sys.exit(1)

    start_time = time.time()  # Start timer

    binary_numbers = [convert_to_binary(num) for num in numbers]
    print("Binary conversion:", binary_numbers)

    hexadecimal_numbers = [convert_to_hexadecimal(num) for num in numbers]
    print("Hexadecimal conversion:", hexadecimal_numbers)

    # Write results to file
    execution_time = time.time() - start_time
    write_results_to_file(numbers, binary_numbers, hexadecimal_numbers, execution_time)
    print(f"Execution Time: {execution_time:.4f} seconds")

if __name__ == "__main__":
    main()
    