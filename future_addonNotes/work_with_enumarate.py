# filename: future_addonNotes/assignment_unit2.py
# -*- coding: utf-8 -*-
# author: Daniel Schubert
# date: 2025-04-21

if __name__ == "__main__":
    # Part 2: Online Store Catalog
    try:
            table_header = ["Product(S)", "Price"]  # Header for the table
            # List of product names
            product_list = ["Item 1", "Item 2", "Item 3", "Combo 1 (Item 1 + 2)",
                            "Combo 2 (Item 2 + 3)",
                            "Combo 3 (Item 1 + 3)", "Combo 4 (Item 1 + 2 + 3)"]
            # List of product prices
            price_list = [200.0, 400.0, 600.0, 540.0, 900.0, 720.0, 900.0]
            def print_multiplied_chars(char: str, count_value: int) -> None:
                """
                Print a character multiplied by a given count value.
                @param char: The character to be printed.
                @param count_value: The number of times to print the character.
                @return: None
                """
                # The f-string is used to format the output string
                print(f"{char * count_value}")

            # Define the width of the catalog table. It dynamically adjusts based on the longest product name.
            def calc_len_of_table_values(
                      product_list: list) -> int:
                """
                Calculate the length of the table values based on the product list.
                @param product_list: List of product names.
                @return: The fixed length based on the maximum product name length.
                @note: It is added 4 spaces if the maximum product name length is greater than 30.
                """
                # Calculate the maximum length of the product names and prices
                max_product_length = max(len(product) for product in product_list)
                if max_product_length > 30:
                     max_product_length += 4  # Add 4 spaces if the length exceeds 30
                else:
                     max_product_length = 30  # Set to 30 if less than 30
                return max_product_length

            def create_store_table(product_list: list, price_list: list, calc_len_of_table_values) -> None:
                """
                Create and display a store table with product names and prices.
                @param product_list: List of product names.
                @param price_list: List of product prices.
                @param calc_len_of_table_values: Function to calculate the length of the table values.
                @return: None
                """
                # Get hold of the maximum length of the product names
                maxlen_of_table_values = calc_len_of_table_values(product_list)
                # Print the header of the table
                print(f"{table_header[0]:<{maxlen_of_table_values}}{table_header[1]}")
                # Print the table row by row. The underscore is used to ignore the index value.
                for _ , product in enumerate(product_list):     # In python it is not necessary to use the index value in the loop.
                    # Print the product names and prices in a formatted table
                    print(f"{product:<{maxlen_of_table_values}}{price_list[_]}")
                # Print the product names and prices in a formatted table

            def online_store_catalog() -> None:
                """Display an online store catalog with prices and discounts."""
                print("\n")
                print("Online Store")
                print_multiplied_chars("-", 26)  # Print a line of dashes
                create_store_table(product_list, price_list, calc_len_of_table_values)  # Create the store table
                print_multiplied_chars("_", 26)  # Print a line of underscores
                print("For delivery Contact: 98764678899")
                print("\n")
            # The function illustrates the use of print statements to display a formatted catalog.
            # It also demonstrates the use of string formatting to align the output.
            online_store_catalog()

    except SyntaxError as e:
        print(f"SyntaxError: {e}")
