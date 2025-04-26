# filename: future_addonNotes/assignment_unit2.py
# -*- coding: utf-8 -*-
# author: Daniel Schubert
# date: 2025-04-26


# Describe the difference between a chained conditional and a nested conditional. Give your own example of each. Do not copy examples from the textbook.

# Deeply nested conditionals can become difficult to read. Describe a strategy for avoiding nested conditionals. Give your own example of a nested conditional that can be modified to become a single conditional and show the equivalent single conditional. Do not copy the example from the textbook.

# The code and its output must be explained technically whenever asked. The explanation can be provided before or after the code, or in the form of code comments within the code. For any descriptive type of question. Your answer must be at least 150 words.

# End your discussion post with one question related to programming fundamentals learned in this unit from which your colleagues can formulate a response or generate further discussion. Remember to post your initial response as early as possible, preferably by Sunday evening, to allow time for you and your classmates to have a discussion.

if __name__ == "__main__":

    def check_nested_conditions() -> None:
        print("Check nested conditions")

    assign_void = check_nested_conditions()

    print(f"Function with nested conditions: {assign_void}")

    # example to avoid nested conditions
    # switch case to avoid nested conditions
    def check_switch_case(value: int) -> str:
        """
        Function to demonstrate the use of a switch case to avoid nested conditions.
        """
        match value:
            case 1:
                return "Value is 1"
            case 2:
                return "Value is 2"
            case _:
                return "Value is not 1 or 2"

    # example to avoid nested conditions
    # a dictionary to avoid nested conditions
    def check_dict(value: int) -> str:
        """
        Function to demonstrate the use of a dictionary to avoid nested conditions.
        """
        return {
            1: "Value is 1",
            2: "Value is 2"
        }.get(value, "Value is not 1 or 2")

    # or create a dict with a lambda function to avoid nested conditions
    def check_lambda(value: int) -> str:
        """
        Function to demonstrate the use of a lambda function to avoid nested conditions.
        """
        return (lambda x: "Value is 1" if x == 1 else "Value is 2" if x == 2 else "Value is not 1 or 2")(value)


    # example to avoid nested conditions
    numbers_list = {
        1: "Value is 1",
        2: "Value is 2",
        3: "Value is 3",
        4: "Value is 4",
        5: "Value is 5",
    }

    number = numbers_list.get(int(1), "Value is not 1 or 2")



    # Explanation of the difference between a chained conditional and a nested conditional.

    # A chained conditional is a series of if-elif-else statements that are evaluated in sequence. Each condition is checked one after the other, and the first true condition's block of code is executed. This structure allows for multiple conditions to be checked in a linear fashion, making it easier to read and understand. For example, if we want to check how a wine scores similar to the Wine-Searcher Aggregate Score, we can use a chained conditional to check if the score is greater than or equal to 95, 90, 85, etc.

    def check_chained_conditional(wine_score: int) -> str:
        """
        Function to demonstrate a chained conditional.
        """
        if wine_score >= 95:        # Check if the wine score is greater than or equal to 95.
            return "Classic"        # Return "Classic" if the condition is true.
        elif wine_score >= 90:      # This is an elif statement that checks if the wine score is greater than or equal to 90.
            return "Outstanding"
        elif wine_score >= 85:      # Another simple elif statement, checking if the wine score is greater than or equal to 85.
            return "Very good"
        elif wine_score >= 80:      # This block of code can only be reached if the previous conditions are false.
            return "Good"
        else:                       # Else can be skipped if not needed, but it is good practice to include it.
            return "Not recommended"


    def check_nested_conditional(wine_type: int, wine_acidity: int) -> str:
        """
        Function to demonstrate a nested conditional. Each first hierarchy is a wine type, and the second hierarchy is the acidity level.
        @param wine_type: The type of wine (red or white).
        @param wine_acidity: The acidity level of the wine (0-10).
        @return: A string indicating the wine's food pairing or quality.
        """
        if wine_type == "red":
            if wine_acidity > 7:
                return "Can be used for alla rague"
            elif wine_acidity < 5:
                return "Trink it with food"
            else:
                return "Balanced red wine"
        elif wine_type == "white":
            if wine_acidity > 7:
                return "Mozarella cheese is a good match"
            elif wine_acidity < 5:
                return "Trink it with food"
            else:
                return "Balanced white wine"
        else:
            return "Unknown wine type"


    def check_single_conditional(wine_type: int, wine_acidity: int) -> str:
        """
        Function to demonstrate a single conditional.
        @param wine_type: The type of wine (red or white).
        @param wine_acidity: The acidity level of the wine (0-10).
        @return: A string indicating the wine's food pairing or quality.
        """
        if wine_type == "red" and wine_acidity > 7:
            return "Can be used for alla rague"
        elif wine_type == "red" and wine_acidity < 5:
            return "Trink it with food"
        elif wine_type == "white" and wine_acidity > 7:
            return "Mozarella cheese is a good match"
        elif wine_type == "white" and wine_acidity < 5:
            return "Trink it with food"
        else:
            return "Unknown wine type"
