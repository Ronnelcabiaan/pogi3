class CBankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = initial_balance          # Private attribute
        self._transaction_history = []            # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_history.append(f"Deposited: {amount}")
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_history.append(f"Withdrew: {amount}")
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance  # Public method to access private balance

    def get_account_number(self):
        return self.__account_number  # Public method to access private account number

    def get_transaction_history(self):
        return self._transaction_history  # Public method to access protected transaction history

# Example usage
if __name__ == "__main__":
    account = CBankAccount("123456789", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Account Number: {account.get_account_number()}")
    print(f"Current Balance: {account.get_balance()}")
    print("Transaction History:")
    for transaction in account.get_transaction_history():
        print(transaction)