class Wallet():
    def __init__(self):
        self.balance = 0

    def add_balance(self, val):
        self.balance += val

    def get_balance(self):
        return self.balance

    def deduct_balance(self, val):
        self.balance -= val
