from abc import abstractmethod, ABCMeta
from datetime import datetime
from random import randint

class Account(metaclass=ABCMeta):

    @abstractmethod
    def open_new_account(self, name, initial_deposit):
        pass

    @abstractmethod
    def generate_account_number(self):
        pass

    @abstractmethod
    def retrieve_account(self, account_number):
        pass


class SavingsAccount(Account):

    def __init__(self):
        self.savings_accounts = {}
        self.transaction_history = {}
        self.current_account_number = None
        self.account_counter = randint(1000000000, 9999999999)

    def open_new_account(self, name, initial_deposit):
        account_number = self.generate_account_number()
        self.savings_accounts[account_number] = {"name": name, "balance": initial_deposit}
        self.transaction_history[account_number] = [
            {"type": "Opening", "amount": initial_deposit, "timestamp": datetime.now()}
        ]
        return account_number

    def generate_account_number(self):
        return self.account_counter

    def retrieve_account(self, account_number):
        return self.savings_accounts.get(account_number, None)

    def deposit(self, amount_deposit):
        if self.current_account_number in self.savings_accounts:
            self.savings_accounts[self.current_account_number]["balance"] += amount_deposit
            self.transaction_history[self.current_account_number].append(
                {"type": "Deposit", "amount": amount_deposit, "timestamp": datetime.now()}
            )
            return True
        return False

    def withdraw(self, amount_withdraw):
        if self.current_account_number in self.savings_accounts:
            if self.savings_accounts[self.current_account_number]["balance"] >= amount_withdraw:
                self.savings_accounts[self.current_account_number]["balance"] -= amount_withdraw
                self.transaction_history[self.current_account_number].append(
                    {"type": "Withdrawal", "amount": amount_withdraw, "timestamp": datetime.now()}
                )
                return True
        return False

    def view_account_balance(self):
        return self.savings_accounts.get(self.current_account_number, {}).get("balance", None)

    def view_transaction_history(self):
        return self.transaction_history.get(self.current_account_number, [])