"""
Author: Parisa Arbab
Date: Feb 6 2024
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link:https://youtu.be/A-DA7TFSZ5g

Questions:
 What is the base case of your recursive function?
 Does everyone in the bottom row carry the same weight?
"""


def weight_on_person(row, column, base_weight=128):
    """
    Calculate the total weight on a person's back in a human pyramid, accurately reflecting the cumulative effect
    of weight distribution from the structure above them.

    Args:
    - row (int): Zero-indexed row number where the person is located.
    - column (int): Zero-indexed column number where the person is located.
    - base_weight (int): Weight of each person in the pyramid. Defaults to 128 pounds.

    Returns:
    - float: The total weight on the person's back in pounds.
    """
    if row == 0:
        # The top person carries no weight from others
        return 0
    if column < 0 or column > row:
        # Out of bounds
        return 0
    if column == 0:
        # Left edge of the pyramid
        return weight_on_person(row - 1, 0, base_weight) / 2 + base_weight / 2
    if column == row:
        # Right edge of the pyramid
        return weight_on_person(row - 1, column - 1, base_weight) / 2 + base_weight / 2

    # Weight from the person directly above and to the left and right
    weight_above_left = weight_on_person(row - 1, column - 1, base_weight) / 2
    weight_above_right = weight_on_person(row - 1, column, base_weight) / 2

    return base_weight + weight_above_left + weight_above_right

# Prompt the user for row and column numbers
row = int(input("Enter the row number of the person (0-indexed): "))
column = int(input("Enter the column number of the person (0-indexed): "))

# Calculate and display the total weight on the specified person
weight = weight_on_person(row, column)
print(f"Total weight on person's back at row {row}, column {column}: {weight} pounds")
