"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# constants created
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


# removed pass and completed the function
def bake_time_remaining(time_elapsed):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - time_elapsed


# avoided using magic number and ,ade the function
def preparation_time_in_minutes(no_of_layers):
    """Calculate the preparation time for no. of layers.

    :param no_of_layers: int - the number of layers in the lasagnia.
    :return: int - total time taken for preparation(in minutes).

    This function takes one integer representing the number of layers 
    in lasagnia and then calculate the total time for preparation based
    on the time it takes to prepare a single layer.
    """
    return no_of_layers * PREPARATION_TIME



# defined the elapsed_time_in_minutes function
def elapsed_time_in_minutes(no_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    :param no_of_layers: int - the number of layers in thwe lasagnia.
    :param elapsed_bake_time: int - total time elapsed in baking.
    :return: int - total time of preparation an baking(in minutes).

    This function takes two integers representing no. of layers in
    lasagnia and time spent in baking. Then calculates the total elapsed
    minutes spent cooking the lasagnia.
    """
    return preparation_time_in_minutes(no_of_layers) + elapsed_bake_time



# added docstrings to all my functions