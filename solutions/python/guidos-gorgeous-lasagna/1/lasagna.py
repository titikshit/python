"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(time_elapsed):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - time_elapsed


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(no_of_layers):
    """Calculate the preparation time for no. of layers.

    :param no_of_layers: int - the number of layers in the lasagnia.
    :return: int - total time taken for preparation(in minutes).

    This function takes one integer representing the number of layers 
    in lasagnia and then calculate the total time for preparation based
    on the time it takes to prepare a single layer.
    """
    return no_of_layers * PREPARATION_TIME



#TODO: define the 'elapsed_time_in_minutes()' function below.
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



# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
