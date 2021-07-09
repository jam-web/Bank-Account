class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User:{self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
todd = User("Todd Oldham", "todd@todd.com")

guido.name = "Guido"
monty.name = "Monty"
todd.name = "Todd"

guido.make_deposit(100).make_deposit(100).make_withdrawal(50).display_user_balance()

monty.make_deposit(50).make_deposit(1000).make_deposit(200).make_withdrawal(500).make_withdrawal(100).display_user_balance()

todd.make_deposit(100).make_withdrawal(25).make_withdrawal(25).make_withdrawal(25).display_user_balance()

todd.transfer_money(guido, 250).display_user_balance()
guido.display_user_balance()