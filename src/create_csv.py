import csv
import os

def create_csv(data, file_path):
    try:
        with open(file_path, mode="w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    data = [
        ['UserID'], [1], [2], [3], [4], [5]
    ]

    directory_path = os.path.join(os.getcwd(), '..', 'doc')

    file_name = 'SDW2023.csv'
    file_path = os.path.join(directory_path, file_name)

    os.makedirs(directory_path, exist_ok=True)
    
    create_csv(data, file_path)
