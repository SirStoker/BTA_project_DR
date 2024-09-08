from FileManager import FileManager
from HistoryMessages import HistoryMessages


class Account:
    def __init__(self, balance = 0):
        self.balance = balance
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):
        self.file_manager.save_data(self.hist_file_path, hist_dict) 


    def deposit(self, amount):
        status = 'failure'

        try:
            amount = int(amount)
            if amount > 0:
                self.balance += amount 
                print(f'\tYou have deposited _ {amount} € _ into your account')
                status = 'success'
            else:
                print(f'\t_!!_ Invalid amount entered: _ {amount} _. Please try again.')
        except ValueError:
            print(f'\t_!!_ Invalid amount entered: _ {amount} _. Please try again.')
    
        history_message = HistoryMessages.deposit(status, amount, self.balance)
        self.write_to_history(history_message)
        
        print(history_message) # это потом убрать


    def debit(self, amount):
        status = 'failure'
        try:
            amount = int(amount)
            if 0 < amount <= self.balance:
                self.balance -= amount
                status = 'success'
                print(f'\tYou have withdrawn _ {amount} € _ from your account.\n\t>> Your current balance is _ {self.balance} € <<') 
            elif amount > self.balance:
                print(f'\t_!!_ You are exceeding your account limit. Please try a smaller amount.') 
            elif amount <= 0:
                print(f'\t_!!_ Invalid amount entered: _ {amount} _. Please try again.')

        except ValueError:
            print(f'\t_!!_ Invalid amount entered: _ {amount} _. Please try again.')
        
        history_message = HistoryMessages.debit(status, amount, self.balance)
        self.write_to_history(history_message)
        

    def get_balance(self):
        return f"_ {self.balance} € "

    def dict_to_string(self, dict):
        if dict["operation_type"] != "exchange":
            return f'type: {dict["operation_type"]} status: {dict["status"]} amount: {dict["amount_of_deposit"]} balance: {dict["total_balance"]}'
        else:
            return f'type: {dict["operation_type"]} status: {dict["status"]} pre exchange amount: {dict["pre_exchange_amount"]} exchange amount: {dict["exchange_amount"]} currency from: {dict["currency_from"]} currency to: {dict["currency_to"]}'
        

    def get_history(self):
        pass
        # TODO:
        # implement a process that returns transaction history line by line
        # use the dict_to_string method to create a string from a dictionary