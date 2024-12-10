import csv

def check_if_safe(report):
    is_increasing = all(report[i] < report[i+1] for i in range(len(report)-1))
    is_decreasing = all(report[i] > report[i+1] for i in range(len(report)-1))

    if not (is_increasing or is_decreasing):
        return False
    
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff < 1 or diff > 3:
            return False

    # If all checks are passed, report is safe
    return True

def count_safe_reports(reports):
    counter = 0
    for report in reports:
        if check_if_safe(report):
            counter += 1

    return counter

def read_data(file_path):
    reports = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            reports.append([int(value) for value in row])
        return reports

if __name__ == "__main__":
    input_file = 'day2/input.csv'
    reports = read_data(input_file)
    safe_reports = count_safe_reports(reports)
    print(f"Safe reports count: {safe_reports}")