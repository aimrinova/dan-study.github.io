# filename: weather_data.py
# -*- coding: utf-8 -*-
# Author:  Daniel Schubert using Visual Studio Code and .venv with Python 3.13.1
# Created on: 2025-04-13

def multiply_age_by_two(age: int = 36) -> None:
    """
    Multiplies the given age by 2.
    """
    print(f"Your age is: {age} and multiplied by 2: {age * 2}")

def display_my_location(city: str = "Berlin", country: str = "Germany", continent: str = "Europe") -> None:
    """
    Displays the city, country, and continent where the user lives.
    """
    print(f"City: {city}, Country: {country}, Continent: {continent}")

def display_examination_schedule(start_date: str = "10 April 2025", end_date: str = "18 April 2025") -> None:
    """
    Displays the examination schedule with start and end dates.
    """
    print(f"Examination Schedule: {start_date} - {end_date}")

class Person:
    """
    A class representing a person with attributes for age, location, and examination schedule.
    """
    def __init__(self, age: int = 36, city: str = "Berlin", country: str = "Germany", continent: str = "Europe",
                 start_date: str = "10 April 2025", end_date: str = "18 April 2025") -> None:
        self.age = age
        self.city = city
        self.country = country
        self.continent = continent
        self.start_date = start_date
        self.end_date = end_date

    def multiply_age_by_two(self) -> None:
        """
        Multiplies the person's age by 2.
        """
        print(f"Your age is: {self.age} and multiplied by 2: {self.age * 2}")

    # display the class attributes
    @property
    def display_class(self) -> None:
        """
        Displays the person's attributes.
        """
        multiply_age_by_two(self.age)
        print(f"City: {self.city}, Country: {self.country}, Continent: {self.continent}")


def main() -> None:
    """
    Main function to execute all functions.
    It calls the functions to display age, location, and examination schedule with default values.
    Every function has parameters to accept user input, but they are not used in this example.
    """
    # age = int(input("Enter your age: "))
    # multiply_age_by_two()
    # display_my_location()
    # display_examination_schedule()
    student_daniel = Person()
    print(student_daniel.display_class)  # Display the class attributes

if __name__ == "__main__":
    main()