import copy
import random
from arguments_utils import convert_to_arguments_list
from list_utils import is_part_of_list


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
    expected_balls_list = convert_to_arguments_list(expected_balls)
    performed_draws = 0
    successful_draws = 0

    while performed_draws < num_experiments:
        hat_copy = copy.deepcopy(hat)
        draw_result = hat_copy.draw(num_balls_drawn)

        if is_part_of_list(expected_balls_list, root_list=draw_result):
            successful_draws += 1

        performed_draws += 1

    return successful_draws / num_experiments
