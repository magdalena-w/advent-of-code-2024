import csv
from collections import Counter

def calculate_distance(file_path):
    """
    Calculates the distance between two lists of integers extracted from a file.
    """
    left_numbers, right_numbers = extract_numbers(file_path)

    # Sort lists for distance calculation
    left_sorted = sorted(left_numbers)
    right_sorted = sorted(right_numbers)

    # Calculate and return the distance
    distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    print(f"Distance: {distance}")
    return distance

def calculate_similarity_score(file_path):
    """
    Calculates the similarity score based on frequency of matching elements.
    """
    left_numbers, right_numbers = extract_numbers(file_path)
    right_counts = Counter(right_numbers)
    similarity_score = sum(num * right_counts[num] for num in left_numbers)
    print(f"Similarity Score: {similarity_score}")
    return similarity_score

def extract_numbers(file_path):
    """
    Extracts and returns two lists of integers from the input file.
    """
    left_list, right_list = [], []

    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            try:
                left_list.append(int(row[0].strip()))
                right_list.append(int(row[3].strip()))
            except ValueError:
                print(f"Skipping invalid row (non-integer values): {row}")

    return left_list, right_list

if __name__ == "__main__":
    input_file = 'day1/input.csv'

    calculate_similarity_score(input_file)
    calculate_distance(input_file)