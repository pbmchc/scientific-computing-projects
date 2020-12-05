from constants import ADDITION_OPERATOR
from arithmetic_problem_validator import validate_arithmetic_problems

ARRANGEMENT_OPERATOR_PART_LENGTH = 2
ARRANGEMENT_PROBLEM_SEPARATOR = '    '
ARRANGEMENT_RESULT_SEPARATOR = '-'


def arithmetic_arranger(problems, evaluate_problems=False):
    error = validate_arithmetic_problems(problems)

    if error:
        return error

    arranged_problems_list = [_arrange_arithmetic_problem(p, evaluate_problems) for p in problems]
    arranged_parts_count = len(arranged_problems_list[0])

    arranged_problems = ''
    for part_index in range(arranged_parts_count):
        arrangement_columns = [p[part_index] for p in arranged_problems_list]
        arranged_problems += ARRANGEMENT_PROBLEM_SEPARATOR.join(arrangement_columns)

        if part_index != arranged_parts_count - 1:
            arranged_problems += '\n'

    return arranged_problems


def _arrange_arithmetic_problem(problem, evaluate_problem):
    left_operand, operator, right_operand = problem.split()

    arrangement_line_length = _get_arrangement_line_length(left_operand, right_operand)
    arrangement_top_row = _format_arrangement_part(left_operand, arrangement_line_length)
    arrangement_bottom_row = operator + _format_arrangement_part(right_operand, arrangement_line_length - 1)
    arrangement_result_separator = arrangement_line_length * ARRANGEMENT_RESULT_SEPARATOR

    arrangement = (arrangement_top_row, arrangement_bottom_row, arrangement_result_separator)

    if evaluate_problem:
        operation = _add_operands if operator == ADDITION_OPERATOR else _subtract_operands
        result = operation(left_operand, right_operand)
        arrangement_result = _format_arrangement_part(str(result), arrangement_line_length)

        return arrangement + (arrangement_result,)

    return arrangement


def _get_arrangement_line_length(*operands):
    longest_operand = max(operands, key=len)
    longest_operand_length = len(longest_operand)

    return longest_operand_length + ARRANGEMENT_OPERATOR_PART_LENGTH


def _format_arrangement_part(part, length):
    return part.rjust(length, ' ')


def _add_operands(left_operand, right_operand):
    return int(left_operand) + int(right_operand)


def _subtract_operands(left_operand, right_operand):
    return int(left_operand) - int(right_operand)
