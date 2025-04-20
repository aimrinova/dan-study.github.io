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
