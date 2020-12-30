import copy
import random
from arguments_utils import convert_to_arguments_list


class Hat:
    def __init__(self, **balls):
        self.contents = convert_to_arguments_list(balls)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    return None
