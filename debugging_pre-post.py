# filename: future_addonNotes/debugging_pre-post.py
# -*- coding: utf-8 -*-
# author: Daniel Schubert
# date: 2025-05-03

# This script demonstrates the use of pre- and post-conditions for debugging.
# It adds pre- and post-condition checks, and function call checks to ensure that the function behaves as expected.
# It also includes a decorator to check for pre- and post-conditions.

import inspect
import logging
import sys
import traceback

from typing import Any, Optional, TypeVar, cast, ParamSpec
from collections.abc import Callable
from functools import wraps


# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Without ParamSpec, I would have to use a generic type for the function signature.
F = TypeVar('F', bound=Callable[..., Any])
# ParamSpec allows us to capture the parameter types of a callable.
P = ParamSpec('P')
R = TypeVar('R')


# Define a decorator for pre- and post-condition checks
def pre_post_conditions(
        pre_condition: Optional[Callable[P, bool]] = None,
        post_condition: Optional[Callable[[R], bool]] = None
        ) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Decorator to check pre- and post-conditions for a function.
    """
    # The decorator takes a function (func) with parameters P and return type R, and returns a new function with the same signature.
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        # The wrapper accepts arguments matching the original function’s signature (via P.args and P.kwargs) and returns a value of type R.
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            # Check pre-condition
            if pre_condition and not pre_condition(*args, **kwargs):
                logger.error(f"Pre-condition failed for {func.__name__} with args: {args}, kwargs: {kwargs}")
                raise ValueError("Pre-condition failed")

            # Call the original function
            result = func(*args, **kwargs)

            # Check post-condition
            if post_condition and not post_condition(result):
                logger.error(f"Post-condition failed for {func.__name__} with result: {result}")
                raise ValueError("Post-condition failed")

            return result

        return cast(Callable[P, R], wrapper)

    return decorator


# Example pre-condition: check if the denominator is non-zero
def non_zero_denominator(a: float, b: float) -> bool:
    return b != 0

# Example post-condition: check if the result is a finite number
def is_finite(result: float) -> bool:
    return result != float('inf') and result != float('nan')


if __name__ == "__main__":
    #    @pre_post_conditions(pre_condition=lambda *args: non_zero_denominator(*args), post_condition=is_finite)
    @pre_post_conditions(pre_condition=non_zero_denominator, post_condition=is_finite)
    def divide(a: float, b: float) -> float:
        """
        Function that divides two numbers.
        """
        return a / b

    try:
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        result = divide(a, b)
        print(f"Result: {result}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        traceback.print_exc(file=sys.stdout)
    finally:
        # This will always execute after the try block, even if an error occurs
        logger.info(">> Finally block executed — clean up, close files, release locks here.")
        # Perform any necessary cleanup here