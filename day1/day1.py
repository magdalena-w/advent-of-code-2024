import csv

def calculate_distance(input_file):
    left_list, right_list = [], []

    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter=' ')
        for row in reader:
            try:
                left_list.append(int(row[0].strip()))   
                right_list.append(int(row[3].strip()))
            except (IndexError, ValueError):
                print(f"Skipping invalid row: {row}")

    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    return sum(abs(l - r) for l, r in zip(sorted_left, sorted_right))

if __name__ == "__main__":
    input_file = 'input.csv'
    distance = calculate_distance(input_file)
    print(distance)
