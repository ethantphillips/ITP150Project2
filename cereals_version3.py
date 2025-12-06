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


def convert_cereal_data(cereals_list):
    try:
        for row_index in range(1, len(cereals_list)):
            row = cereals_list[row_index]
            row[1] = int(row[1])
            row[2] = int(row[2])
            row[3] = int(row[3])
            row[4] = float(row[4])
            row[5] = float(row[5])
    except IndexError:
        print("IndexError: Problem accessing one of the cereal rows.")
    except Exception as e:
        print(f"Unexpected error while converting data: {e}")
    return cereals_list


def get_menu_choice(menu_text, valid_choices):
    while True:
        print(menu_text)
        try:
            choice_str = input()
            choice = int(choice_str)
            if choice in valid_choices:
                return choice
            else:
                raise ValueError
        except ValueError:
            print("Invalid. Please enter 1, 2, 3, 4, 5, 6, or 99 as an integer.")


def main():
    MENU_PRINT_LIST = 1
    MENU_HIGHEST_PROTEIN = 2
    MENU_LOWEST_SUGAR = 3
    MENU_AVG_CALORIES = 4
    MENU_DISPLAY_CEREAL = 5
    MENU_SAVE_STATS = 6
    MENU_QUIT = 99

    cereals = []
    cereal_stats = {}
    menu_choice = 0

    filename = "cereals.csv"
    cereals = read_cereals_file(filename)
    cereals = convert_cereal_data(cereals)

    while True:
        menu_text = (
            "Cereal Nutritional Analysis\n"
            "--------------------------------------------------------------------------------\n"
            "Please choose from the following menu:\t\t\n"
            "Enter 1 to print the cereals list.\t\t\n"
            "Enter 2 to find cereal with the highest protein.\t\t\n"
            "Enter 3 to find cereal with the lowest sugar.\t\t\n"
            "Enter 4 to display average calories.\t\t\n"
            "Enter 5 to display the nutritional information for a cereal.\t\t\n"
            "Enter 6 to save the statistics.\t\t\n"
            "Enter 99 to Quit.\n"
            "--------------------------------------------------------------------------------"
        )

        valid_choices = [
            MENU_PRINT_LIST,
            MENU_HIGHEST_PROTEIN,
            MENU_LOWEST_SUGAR,
            MENU_AVG_CALORIES,
            MENU_DISPLAY_CEREAL,
            MENU_SAVE_STATS,
            MENU_QUIT,
        ]

        menu_choice = get_menu_choice(menu_text, valid_choices)

        if menu_choice == MENU_QUIT:
            break


if __name__ == "__main__":
    main()
