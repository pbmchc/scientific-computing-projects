import re
from constants import ADDITION_OPERATOR, SUBTRACTION_OPERATOR

ALLOWED_OPERATORS = [ADDITION_OPERATOR, SUBTRACTION_OPERATOR]
MAX_OPERAND_LENGTH = 4
MAX_PROBLEMS_LENGTH = 5
NON_DIGIT_CHARACTER_REGEX = r'\D'


def validate_arithmetic_problems(problems):
    if len(problems) > MAX_PROBLEMS_LENGTH:
        return "Error: Too many problems."
    for p in problems:
        error = _validate_arithmetic_problem(p)
        if error:
            return error

    return None


def _validate_arithmetic_problem(problem):
    left_operand, operator, right_operand = problem.split()

    if operator not in ALLOWED_OPERATORS:
        return "Error: Operator must be '+' or '-'."

    if _has_invalid_operands_length(left_operand, right_operand):
        return "Error: Numbers cannot be more than four digits."

    if _has_invalid_operands_characters(left_operand, right_operand):
        return "Error: Numbers must only contain digits."

    return None


def _has_invalid_operands_length(*operands):
    return any(len(o) > MAX_OPERAND_LENGTH for o in operands)


def _has_invalid_operands_characters(*operands):
    return any(bool(re.search(NON_DIGIT_CHARACTER_REGEX, o)) for o in operands)
