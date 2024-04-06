import pandas as pd
import os

def menu_options():
    print("|------------Data option------------|")
    print("| 1: Read .CSV Data                 |")
    print("| 2: Check the data overview        |")
    print("| 3: Check for empty values         |")
    print("| 4: Check for duplicate values     |")
    print("|---------Clean data option---------|")
    print("| 5: Delete empty data              |")
    print("| 6: Delete duplicate data          |")
    print("| 7: Delete negative number data    |")
    print("| 8: Delete special characters data |")
    print("|-----------------------------------|\n")


def data_action(option, file_name):
    data = pd.read_csv(file_name)
    if option == 1:
        print(data)
    elif option == 2:
        print(data.info())
    elif option == 3:
        print(data.isnull().sum())
    elif option == 4:
        print(data.duplicated().sum())
    elif option == 5:
        # Delete empty data
        cleaned_data = data.dropna()
        save_path = save_cleaned_data(cleaned_data, file_name)
        print(f"Data after removing empty values saved to: {save_path}")
    elif option == 6:
        # Delete negative number data
        cleaned_data = data.drop_duplicates()
        save_path = save_cleaned_data(cleaned_data, file_name)
        print(f"Data after removing duplicate values saved to: {save_path}")
    elif option == 7:
        column_name = input("Enter the column name containing negative numeric data to be processed (Ex: Age): ")
        # Delete special negative numeric
        cleaned_data = data[data[column_name] >= 0]
        save_path = save_cleaned_data(cleaned_data, file_name)
        print(f"Data after removing negative numeric values data to: {save_path}")
    elif option == 8:
        column_name = input("Enter the column name containing special characters data to be processed (Ex: FirstName): ")
        special_characters_pattern = r'[^a-zA-Z0-9\s]'
        mask = data[column_name].str.contains(special_characters_pattern, na=False)
        # Delete special characters data
        cleaned_data = data[~mask]
        save_path = save_cleaned_data(cleaned_data, file_name)
        print(f"Data after removing special characters data saved to: {save_path}")
    else:
        print("Invalid Option")


def save_cleaned_data(cleaned_data, original_file_name):
    # Get the directory of the original file
    directory = os.path.dirname(original_file_name)
    # Get the base name of the original file
    base_name = os.path.basename(original_file_name)
    # Generate the new file name
    new_file_name = f"cleaned_{base_name}"
    # Construct the full path for the new file
    save_path = os.path.join(directory, new_file_name)
    # Save cleaned data to the new file
    cleaned_data.to_csv(save_path, index=False)
    return save_path


def main():
    menu_options()
    option_input = int(input("Enter option: "))
    csv_file_name = input("Enter csv file name (Ex: Data.csv): ")
    data_action(option_input, csv_file_name)
    
if __name__ == '__main__':
    main()
