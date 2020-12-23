from constants import CATEGORY_OUTPUT_LINE_LENGTH
from category_utils import get_category_ledger_row, get_category_operations_total
from number_utils import format_decimal_places
from string_utils import limit_string_length


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        can_withdraw = self.check_funds(amount)

        if can_withdraw:
            self.deposit(-amount, description)

        return can_withdraw

    def transfer(self, amount, category):
        can_transfer = self.check_funds(amount)

        if can_transfer:
            self.withdraw(amount, 'Transfer to ' + category.name)
            category.deposit(amount, 'Transfer from ' + self.name)

        return can_transfer

    def get_balance(self):
        return get_category_operations_total(self.ledger)

    def get_withdrawals_total(self):
        return abs(get_category_operations_total(filter(lambda operation: operation['amount'] < 0, self.ledger)))

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        return self._get_category_output()

    def __repr__(self):
        return self._get_category_output()

    def _get_category_output(self):
        category_name = limit_string_length(self.name, CATEGORY_OUTPUT_LINE_LENGTH)
        header = category_name.center(CATEGORY_OUTPUT_LINE_LENGTH, '*')
        rows = '\n'.join(map(get_category_ledger_row, self.ledger))
        total = 'Total: ' + format_decimal_places(self.get_balance())

        return header + '\n' + rows + '\n' + total
