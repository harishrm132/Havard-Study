

# Unpack
# * for unpacking a list
# ** for unpacking a dictionary

# Constants in capital letters
BAL = 0

# docstring is a string that is used to document the code (Restuctured Text)
class Account:
    """
    Create Account with deposit & widthdraw options

    :param balance: Balance of the account
    :type balance: int
    :raise TypeError: If balance is not an integer
    """
    # Type Hints
    def __init__(self, balance: int) -> None:
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount) -> int:
        self._balance += amount

    def withdraw(self, amount) -> int:
        self._balance -= amount


def main():
    account = Account(BAL)
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)



if __name__ == "__main__":
    main()