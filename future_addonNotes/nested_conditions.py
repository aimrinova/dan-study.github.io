# filename: future_addonNotes/assignment_unit2.py
# -*- coding: utf-8 -*-
# author: Daniel Schubert
# date: 2025-04-26


# Describe the difference between a chained conditional and a nested conditional. Give your own example of each. Do not copy examples from the textbook.

# Deeply nested conditionals can become difficult to read. Describe a strategy for avoiding nested conditionals. Give your own example of a nested conditional that can be modified to become a single conditional and show the equivalent single conditional. Do not copy the example from the textbook.

# The code and its output must be explained technically whenever asked. The explanation can be provided before or after the code, or in the form of code comments within the code. For any descriptive type of question. Your answer must be at least 150 words.

# End your discussion post with one question related to programming fundamentals learned in this unit from which your colleagues can formulate a response or generate further discussion. Remember to post your initial response as early as possible, preferably by Sunday evening, to allow time for you and your classmates to have a discussion.

if __name__ == "__main__":

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

    # Whenever one of the branches has an additional branch inside, it is called a nested conditional. A nested conditional is a conditional statement that is placed inside another conditional statement. This structure allows for more complex decision-making processes, where the outcome of one condition can lead to further conditions being evaluated. For example, if we want to check the wine type and its acidity level, we can use a nested conditional to check if the wine is red or white and then check its acidity level.
    def check_nested_conditional(wine_type: int, wine_acidity: int) -> str:
        """
        Function to demonstrate a nested conditional. Each first hierarchy is a wine type, and the second
        hierarchy is the acidity level.
        Keyword arguments:
        wine_type -- The type of wine (red or white).
        wine_acidity -- The acidity level of the wine (0-10).
        return -- A string indicating the wine's food pairing or quality.
        """
        if wine_type == "red":
            if wine_acidity > 7:
                return "Try a tomato ragù or spaghetti Bolognese"
            elif wine_acidity < 5:
                return "Try braised short ribs, roasted pork tenderloin, or aged cheddar"
            else:
                return "Matches with roast chicken and mushroom risotto"
        elif wine_type == "white":
            if wine_acidity > 7:
                return "Try oysters on the half shell, goat cheese salad"
            elif wine_acidity < 5:
                return "Try creamy Alfredo pasta or fried chicken"
            else:
                return "Matches with grilled sea bass and sushi rolls"
        else:
            return "Unknown wine type"



    # An example of a nested conditional is a coffee machine state check. This is a simple example of how nested conditionals are hard to read and understand. Addiotnally, it is not easy to maintain and extend the code.
    def coffee_machine_state(state: int) -> str:
        if state == 0:
            return "Coffee machine is off"
        elif state >= 1:
            if state >= 2:
                if state == 3:
                    return "Coffee machine is on"
                elif state == 4:
                    return "Coffee machine is brewing"
                else:
                    return "Coffee machine is in standby mode"
            else:
                return "Coffee machine is in error state"
        else:
            return "Coffee machine does not recognize the state"


    # Adhering to best practices, we can use a single conditional to avoid deeply nested conditionals. This can be achieved by using logical operators to combine conditions or by using a dictionary or a match-case structure. This approach improves code readability and maintainability.
    def coffee_machine_state_mapping(value: int) -> str:
        """
        Function to demonstrate the use of a dictionary to avoid nested conditions.
        """
        return {
            0: "Coffee machine is off",
            1: "Coffee machine is in error state",
            2: "Coffee machine is in standby mode",
            3: "Coffee machine is on",
            4: "Coffee machine is brewing",
        }.get(value, "Coffee machine does not recognize the state")

    # Example usage of the coffee machine state function
    value = 6
    print(coffee_machine_state_mapping(value))  # Output: Coffee machine does not recognize the state
