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


def display_cereals_list(cereals_list):
    if not cereals_list:
        print("The cereals list is empty.")
        return

    headings = cereals_list[0]
    print("--------------------------------------------------------------------------------")
    print(f"{headings[0]:<35}{headings[1]:>10}{headings[2]:>9}{headings[3]:>8}{headings[4]:>6}{headings[5]:>8}")

    for row_index in range(1, len(cereals_list)):
        row = cereals_list[row_index]
        print(
            f"{row[0]:<35}{row[1]:>10}{row[2]:>9}{row[3]:>8}{row[4]:>6.1f}{row[5]:>8.1f}"
        )


def calc_highest_protein(cereals_list, stats_dict):
    try:
        if len(cereals_list) <= 1:
            print("The cereals list is empty.")
            return stats_dict

        highest_protein = cereals_list[1][2]
        highest_protein_cereal = cereals_list[1][0]

        for row_index in range(2, len(cereals_list)):
            protein = cereals_list[row_index][2]
            if protein > highest_protein:
                highest_protein = protein
                highest_protein_cereal = cereals_list[row_index][0]

        print("\nHighest Protein                                       Cereal")
        print(f"{highest_protein:<51}{highest_protein_cereal}")

        stats_dict["Highest Protein"] = highest_protein
        stats_dict["Highest Cereal"] = highest_protein_cereal

    except IndexError:
        print("IndexError: Problem accessing one of the cereal rows.")
    except ValueError:
        print("ValueError: Problem with the cereal data values.")
    except Exception as e:
        print(f"Unexpected error while calculating highest protein: {e}")

    return stats_dict


def calc_lowest_sugar(cereals_list, stats_dict):
    try:
        if len(cereals_list) <= 1:
            print("The cereals list is empty.")
            return stats_dict

        lowest_sugar = cereals_list[1][3]
        lowest_sugar_cereal = cereals_list[1][0]

        for row_index in range(2, len(cereals_list)):
            sugar = cereals_list[row_index][3]
            if sugar < lowest_sugar:
                lowest_sugar = sugar
                lowest_sugar_cereal = cereals_list[row_index][0]

        print("\nLowest Sugar                                          Cereal")
        print(f"{lowest_sugar:<51}{lowest_sugar_cereal}")

        stats_dict["Lowest Sugar"] = lowest_sugar
        stats_dict["Lowest Sugar Cereal"] = lowest_sugar_cereal

    except IndexError:
        print("IndexError: Problem accessing one of the cereal rows.")
    except ValueError:
        print("ValueError: Problem with the cereal data values.")
    except Exception as e:
        print(f"Unexpected error while calculating lowest sugar: {e}")

    return stats_dict


def calc_average_calories(cereals_list, stats_dict):
    try:
        if len(cereals_list) <= 1:
            print("The cereals list is empty.")
            return stats_dict

        total_calories = 0
        count = 0

        for row_index in range(1, len(cereals_list)):
            calories = cereals_list[row_index][1]
            total_calories += calories
            count += 1

        average_calories = total_calories / count

        print("\nAverage Calories")
        print(f"{average_calories:>10.1f}")

        stats_dict["Average Calories"] = average_calories

    except IndexError:
        print("IndexError: Problem accessing one of the cereal rows.")
    except ZeroDivisionError:
        print("ZeroDivisionError: There were no cereals to average.")
    except ValueError:
        print("ValueError: Problem with the cereal data values.")
    except Exception as e:
        print(f"Unexpected error while calculating average calories: {e}")

    return stats_dict


def search_cereal(cereals_list):
    try:
        if len(cereals_list) <= 1:
            print("The cereals list is empty.")
            return

        found = False
        cereal_name = input("Please enter the name of the cereal:\n").strip()

        for row_index in range(1, len(cereals_list)):
            row = cereals_list[row_index]
            if row[0].lower() == cereal_name.lower():
                print(f"{row[0]:<35}{row[1]:>10}{row[2]:>9}{row[3]:>8}{row[4]:>6.1f}{row[5]:>8.1f}")
                found = True
                break

        if not found:
            print(f"We can't find {cereal_name} in the cereals list.")

    except IndexError:
        print("IndexError: Problem accessing one of the cereal rows.")
    except ValueError:
        print("ValueError: Problem with the cereal data values.")
    except Exception as e:
        print(f"Unexpected error while searching for the cereal: {e}")


def save_stats_to_json(stats_dict):
    try:
        if not stats_dict:
            print("There are no statistics to save yet.")
            return

        filename = "cereal_stats.json"
        print(stats_dict)

        with open(filename, "w", newline="") as json_file:
            json.dump(stats_dict, json_file, indent=4)

        print("The cereal_stats.json file has been updated.")

    except PermissionError:
        print("PermissionError: You do not have permission to write to this file.")
    except OSError as e:
        print(f"OSError while writing to the file: {e}")
    except Exception as e:
        print(f"Unexpected error while saving stats: {e}")


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

        if menu_choice == MENU_PRINT_LIST:
            display_cereals_list(cereals)
        elif menu_choice == MENU_HIGHEST_PROTEIN:
            cereal_stats = calc_highest_protein(cereals, cereal_stats)
        elif menu_choice == MENU_LOWEST_SUGAR:
            cereal_stats = calc_lowest_sugar(cereals, cereal_stats)
        elif menu_choice == MENU_AVG_CALORIES:
            cereal_stats = calc_average_calories(cereals, cereal_stats)
        elif menu_choice == MENU_DISPLAY_CEREAL:
            search_cereal(cereals)
        elif menu_choice == MENU_SAVE_STATS:
            save_stats_to_json(cereal_stats)
        else:
            # This will happen when the user enters 99 to exit
            print("Cereal, it's like having dessert for breakfast!")
            break

        elif menu_choice == MENU_SAVE_STATS:
            save_stats_to_json(cereal_stats)
        else:
            print("Cereal, it's like having dessert for breakfast!")
            break