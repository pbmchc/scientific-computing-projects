from constants import CATEGORY_OUTPUT_LINE_LENGTH
from number_utils import format_decimal_places
from string_utils import limit_string_length

MAX_AMOUNT_LENGTH = 7
MAX_DESCRIPTION_LENGTH = 23


def get_category_ledger_row(record):
    amount = limit_string_length(format_decimal_places(record['amount']), MAX_AMOUNT_LENGTH)
    description = limit_string_length(record['description'], MAX_DESCRIPTION_LENGTH)

    return description + amount.rjust(CATEGORY_OUTPUT_LINE_LENGTH - len(description), ' ')

