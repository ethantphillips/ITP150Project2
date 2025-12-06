"""
Ethan Phillips
Project 2 - Cereal Nutritional Analysis
ITP 150
Date: 12/6/2025
This program reads a CSV file containing cereal nutritional information
and stores the data in a list of lists. Each inner list represents a cereal.
"""

import csv
import json

def read_cereals_file(filename):
    cereals_list = []
    try:
        with open(filename, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                cereals_list.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
    return cereals_list


def main():
    cereals = []
    filename = "cereals.csv"
    cereals = read_cereals_file(filename)
    print(cereals)


if __name__ == "__main__":
    main()
