import copy
import random
from arguments_utils import convert_to_arguments_list


class Hat:
    def __init__(self, **balls):
        self.contents = convert_to_arguments_list(balls)

    def draw(self, number_of_balls):
        max_number_of_balls = len(self.contents)
        sample_length = number_of_balls if number_of_balls <= max_number_of_balls else max_number_of_balls
        draw_result = random.sample(self.contents, sample_length)

        for ball in draw_result:
            self.contents.remove(ball)

        return draw_result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    return None
