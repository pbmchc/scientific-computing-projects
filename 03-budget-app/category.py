from functools import reduce


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description):
        can_withdraw = self.check_funds(amount)

        if can_withdraw:
            self.deposit(-amount, description)

        return can_withdraw

    def get_balance(self):
        return reduce(lambda acc, curr: acc + curr['amount'], self.ledger, 0)

    def transfer(self, amount, category):
        can_transfer = self.check_funds(amount)

        if can_transfer:
            self.withdraw(amount, 'Transfer to ' + category.name)
            category.deposit(amount, 'Transfer from ' + self.name)

        return can_transfer

    def check_funds(self, amount):
        return self.get_balance() >= amount
