"""
computeStatistics.py

This program reads a file containing numbers and calculates:
- Mean
- Median
- Mode
- Variance
- Standard Deviation

The results are printed on the screen and saved in a file.

Usage:
    python3 computeStatistics.py data.txt
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
                    number = float(line.strip())  # Convert to float
                    numbers.append(number)
                except ValueError:
                    print(f"❌ Error found: '{line.strip()}' is not a valid number.")
    except FileNotFoundError:
        print(f"❌ Error found: The file '{file_name}' does not exist.")
        sys.exit(1)

    return numbers

def calculate_mean(numbers):
    """
    Calculates the mean of a list of numbers.
    
    f(x):
        mean = sum(numbers) / len(numbers)
    """
    return sum(numbers) / len(numbers) if numbers else 0

def calculate_median(numbers):
    """
    Calculates the median of a list of numbers.
    
    - If the list has an odd number of elements, returns the middle one.
    - If the list has an even number of elements, returns the average of the two middle ones.
    """
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]

    return (numbers[n // 2 - 1] + numbers[n // 2]) / 2

def calculate_mode(numbers):
    """
    Calculates the mode of a list of numbers.
    
    - The mode is the number that appears most frequently.
    - If multiple numbers have the same highest frequency, returns a list of them.
    """
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_frequency = max(frequency.values(), default=0)
    modes = [num for num, freq in frequency.items() if freq == max_frequency]

    return modes if len(modes) > 1 else modes[0]

def calculate_variance(numbers, mean):
    """
    Calculates the variance of a list of numbers.
    
    f(x):
        variance = sum((X_i - mean) ** 2) / (N - 1)
    """
    n = len(numbers)
    if n < 2:
        return 0
    return sum((x - mean) ** 2 for x in numbers) / (n - 1)

def calculate_standard_deviation(variance):
    """
    Calculates the standard deviation from the variance.
    
    f(x):
        standard deviation = sqrt(variance)
    """
    return variance ** 0.5

def write_results_to_file(results, execution_time):
    """
    Writes the computed statistics to a file named 'statistics_results.txt'.
    """
    with open("statistics_results.txt", "w", encoding="utf-8") as file:
        file.write("Statistics Results:\n")
        file.write(f"Mean: {results['mean']:.2f}\n")
        file.write(f"Median: {results['median']:.2f}\n")
        file.write(f"Mode: {results['mode']}\n")
        file.write(f"Variance: {results['variance']:.2f}\n")
        file.write(f"Standard Deviation: {results['standard_deviation']:.2f}\n")
        file.write(f"Execution Time: {execution_time:.4f} seconds\n")

def main():
    """
    Main function of the program.

    - Reads a file with numerical data.
    - Computes statistics: Mean, Median, Mode, Variance, and Standard Deviation.
    - Saves the results in 'StatisticsResults.txt'.
    - Prints the results on the screen.
    """

    if len(sys.argv) != 2:
        print("Usage eg: python3 computeStatistics.py file.txt")
        sys.exit(1)

    data_file = sys.argv[1]
    numbers = read_numbers(data_file)

    if not numbers:
        print("No valid numbers found in the file.")
        sys.exit(1)

    start_time = time.time() # Start timer

    mean = calculate_mean(numbers)
    print(f"Mean: {mean:.2f}")

    median = calculate_median(numbers)
    print(f"Median: {median:.2f}")

    mode = calculate_mode(numbers)
    print(f"Mode: {mode}")

    variance = calculate_variance(numbers, mean)
    print(f"Variance: {variance:.2f}")

    standard_deviation = calculate_standard_deviation(variance)
    print(f"Standard Deviation: {standard_deviation:.2f}")

    execution_time = time.time() - start_time  # Calc execution time

    #Store results in file
    results = {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": standard_deviation
    }

    write_results_to_file(results, execution_time)
    print(f"Exec time: {execution_time:.4f} seconds")

if __name__ == "__main__":
    main()
