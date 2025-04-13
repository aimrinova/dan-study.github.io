# filename:
# -*- coding: utf-8 -*-

import ast

def run_this_file():
    """ test ast duumb and what it is doing"""
    f_var = 78
    tree_todumb = ast.parse("print(f'this is text. {f_var} and here')")
    print(ast.dump(tree_todumb, indent=True))


# TODO: add more tests for the ast module and how it works with the pip module
# use assert statements to check the output of the ast module and how it works with the pip module
# and use mocking
def test_ast_module():
    """ test ast module"""
    # test ast module
    pass


if __name__ == "__main__":
    run_this_file()
    # print 'Hello, World!'



# #
# # Type the statements below into your Python interpreter. For each statement, copy the output into your Discussion # # Assignment and explain the output. Compare it with any similar examples in the textbook, and describe what it means # about your version of Python.


# # Beforehand, the idle mode uses prompts and each single line was typed in the prompt. No import statements were used. # # The output was copied from the idle mode and pasted into the discussion assignment. The output was not modified in any # way. The code was not run in a script, but rather in the idle mode.

# # all in idle mode Python 3.13.1
# # 1. input output
# print 'Hello, World!'  # idle output: SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# # explaination: In Python 3, print is a function and requires parentheses. In Python 2, print was a statement and did not require parentheses.
# # The error message suggests that the user may have meant to use the print function with parentheses, which is the correct syntax in Python 3.
# # Lexer and parser are two important components of the Python interpreter. The lexer is responsible for breaking the input code into tokens, while the parser is responsible for analyzing the structure of the code and determining its meaning. In this case, the lexer was able to identify the print statement, but the parser was unable to understand it due to the missing parentheses.
# # The error message indicates that the parser was expecting a function call, but instead found a statement. This is a common issue when transitioning from Python 2 to Python 3, as many syntax changes were introduced in the new version.


# # 2. input output
# 1/2 #  idle output: 0.5
# # explaination: In Python 3, the division operator (/) performs true division, which means it returns a float result even if both operands are integers. In Python 2, the division operator performed integer division if both operands were integers, which would return an integer result. The lexer and parser in Python 3 correctly identify the division operation and evaluate it to 0.5. This change in behavior is part of the effort to make Python 3 more consistent and predictable in its handling of numeric types and operations.
# # The lexer identifies the division operator and the operands, while the parser evaluates the expression and returns the result. This is a common example of how Python 3 has improved the handling of numeric operations compared to Python 2.
# # In idle mode, it is not possible to see the lexer and parser in action, but they are working behind the scenes to interpret the code and produce the output. The lexer breaks the input into tokens, while the parser analyzes the structure of the code and evaluates the expression. This is a fundamental part of how Python works, and it is important to understand how these components interact to produce the final result.
# # Additionally the idle mode does not require import statements, as the lexer and parser are built into the Python interpreter. This means that the code can be run directly in the idle mode without any additional setup or configuration. This is one of the advantages of using idle mode for testing and experimenting with Python code, as it allows for quick and easy testing without the need for additional tools or libraries.
# # And no variable assignment is needed to see the ouput. How does the lexer and parser differ between idle and script mode?

# # 3. input output
# type(1/2) #  idle output: <class 'float'>
# # explanation: The type function in Python returns the type of the object passed to it. In this case, the division operation (1/2) returns a float value (0.5), and the type function correctly identifies it as a float. The lexer and parser work together to evaluate the expression and determine its type. The lexer breaks the input into tokens, while the parser analyzes the structure of the code and evaluates the expression. This is a common example of how Python handles numeric operations and types.
# # the param in cpython is a built-in function that returns the type of an object. The type function takes one argument, which can be any object, and returns the type of that object. In this case, the argument is the result of the division operation (1/2), which is a float value. The type function evaluates the expression and returns the type of the result, which is <class 'float'>. This indicates that the result of the division operation is a float value, which is consistent with the behavior of Python 3.

# # 4. input output
# print(01) #  idle output: SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
# # explanation: In Python 3, leading zeros in decimal integer literals are not allowed. This is a change from Python 2, where leading zeros were allowed and interpreted as octal integers. The error message indicates that the user should use an 0o prefix for octal integers instead of leading zeros. The lexer and parser in Python 3 correctly identify the leading zero as an error and raise a SyntaxError. This change was made to improve the clarity and consistency of numeric literals in Python, and to avoid confusion between decimal and octal representations.
# # to add a leading zero to an integer you can change the range values and the representation will be fixed 5 numbers of integers.
# # For example, if you want to represent the number 1 as a 5-digit integer with leading zeros, you can use the following code:
# print(f"{1:05}") # This will output "00001".
# # This uses the f-string formatting feature in Python 3, which allows you to specify the format of the output string. The ":05" part specifies that the number should be formatted as a 5-digit integer with leading zeros. This is a common way to represent numbers with leading zeros in Python 3, and it is more flexible and clear than using leading zeros in the integer literal itself.
# # if converting this to an integer with int(), the leading zeros will be removed and the integer will be represented as 1.
# # For example:
# print(int(f"{1:05}")) # This will output 1.
# # This is because the int() function converts the string representation of the number back to an integer, and the leading zeros are not part of the integer value. This is a common behavior in Python, and it is important to understand how string formatting and integer conversion work together to produce the desired output.

# # 5. input output
# 1/(2/3) # idle output: 1.5

# # error handling to avoid division by zero errors in Python 3, you can use a try-except block to catch the ZeroDivisionError exception. For example:
# try:
#     result = 1/(2/0)
# except ZeroDivisionError:
#     print("Error: Division by zero")
# finally:
#     print("This will always execute")
# # This will output "Error: Division by zero" instead of raising an exception. This is a common way to handle errors in Python, and it is important to understand how to use try-except blocks to catch and handle exceptions in your code. The lexer and parser work together to identify the division operation and evaluate the expression, but if a division by zero error occurs, the exception is raised and caught by the except block.
# # finally block will always execute, regardless of whether an exception was raised or not. This is useful for cleaning up resources or performing any necessary finalization steps in your code.
# # Ultimately, this is a fundamental part of how Python works, and it is important to understand how these components interact to produce the final result.

# # The code and its output must be explained technically whenever asked. The explanation can be provided before or # # after the code, or in the form of code comments within the code. For any descriptive type of question, your answer # must be at least 150 words.
