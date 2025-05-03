# filename: future_addonNotes/debugging_pre-post.py
# -*- coding: utf-8 -*-
# author: Daniel Schubert
# date: 2025-05-03


# This script demonstrates the use of pre- and post-conditions for debugging.
# It adds pre- and post-condition checks, and function call checks to ensure that the function behaves as expected.
# It also includes a decorator to check for pre- and post-conditions.
from typing import Callable, Any, Optional, Tuple, TypeVar, cast
from functools import wraps
import inspect
import logging
import sys
import traceback

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

T = TypeVar('T')
R = TypeVar('R')
F = TypeVar('F', bound=Callable[..., Any])

# Define a decorator for pre- and post-condition checks
def pre_post_conditions(pre_condition: Optional[Callable[..., bool]] = None,
                         post_condition: Optional[Callable[[Any], bool]] = None) -> Callable[[F], F]:
    """
    Decorator to check pre- and post-conditions for a function.
    """
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
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

        return cast(F, wrapper)

    return decorator


# Example pre-condition: check if the denominator is non-zero
def non_zero_denominator(a: float, b: float) -> bool:
    return b != 0

# Example post-condition: check if the result is a finite number
def is_finite(result: float) -> bool:
    return result != float('inf') and result != float('nan')


if __name__ == "__main__":
    #    @pre_post_conditions(pre_condition=lambda *args, **kwargs: non_zero_denominator(args), post_condition=is_finite)
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