# filename: future_addonNotes/functions_and_args.py
# -*- coding: utf-8 -*-
# author: Daniel Schubert
# date: 2024-04-20

# for Example 1 and 2:
def coffee_brewer(coffee_type: str) -> None:
    """
    Function to brew coffee.
    Parameters: coffee_type (str): The type of coffee to brew.
    """
    print(f"Brewing: {coffee_type}.")

def run_coffee_tasks() -> None:
    """
    Main function to demonstrate the use of the coffee_brewer function.
    Calls the function with different types of arguments: a value, a variable, and an expression.
    """
    # For Example 1 and 2:
    # The argument is "Americano" and the parameter is coffee_type.
    coffee_brewer("Americano")  # Call the function with a string argument
    # Explanation: In the provided Python code, `Americano` is being used as a string argument when
    # calling the `coffee_brewer` function. Specifically, in the line
    # `coffee_brewer("Americano")`, `"Americano"` is a string literal that represents
    # the type of coffee to be brewed.

    # create vaaribale to pass as argument
    coffee_type_variable = "Latte extra sugar"
    coffee_brewer(coffee_type_variable)  # Call the function with a variable argument
    # create expression to pass as argument
    coffee_brewer("Espresso" + " with milk")  # Call the function with an expression argument

    # Example 3: Construct a function with a local variable.
    # Show what happens when you try to use that variable outside the function.
    def switch_to_espresso(user_wish_exachnaged: str) -> str:
        """
        Function to switch to espresso.
        """
        espresso_type = "Espresso"
        return espresso_type

    # try to use local variable outside the function
    try:
        # This will cause an exception because espresso_type is local
        print(espresso_type) # type: ignore
    except NameError as e:
        print(f"Calling local outside: {e}")

    # Example 4: Construct a function that takes an argument.
    # Show what happens when you try to use that parameter name outside the function.
    def brewing_argument_is(i_cant_be_used_outside: str) -> None:
        """
        Function to demonstrate the use of a parameter name.
        """
        pass
    try:
        print(i_cant_be_used_outside) # type: ignore
    except NameError as e:
        print(f"Using a function argument outside: {e}")

    # Example 5:
    time_for_maintenance = "12:00 PM"
    def coffee_machine(time_for_maintenance: str) -> None:
        """
        Function to demonstrate variable shadowing.
        """
        time_for_maintenance = "12:30 PM"
        print(f"Maintenance scheduled at: {time_for_maintenance}")

    coffee_machine(time_for_maintenance)  # Call the function with a variable argument
    print(f"Global variable time_for_maintenance: {time_for_maintenance}")  # This will print the global variable

if __name__ == "__main__":
    run_coffee_tasks()
