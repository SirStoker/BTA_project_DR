from FileManager import FileManager
from HistoryMessages import HistoryMessages


class Account:
    def __init__(self, balance=0):
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
                # print(f'\tYou have deposited _ {amount} € _ into your account')
                status = 'success'
            else:
                print('Invalid amount for deposit!')
        except ValueError:
            print('Invalid amount for deposit!')
    
        history_message = HistoryMessages.deposit(status, amount, self.balance)
        self.write_to_history(history_message)


    def debit(self, amount):
        status = 'failure'
        try:
            amount = int(amount)
            if 0 < amount <= self.balance:
                self.balance -= amount
                status = 'success'
                # print(f'\tYou have withdrawn _ {amount} € _ from your account.\n\t>> Your current balance is _ {self.balance} € <<') 
            elif amount > self.balance:
                print('Invalid amount for debit!') 
            elif amount <= 0:
                print('Invalid amount for debit!')
        except ValueError:
            print('Invalid amount for debit!')
        
        history_message = HistoryMessages.debit(status, amount, self.balance)
        self.write_to_history(history_message)
        

    def get_balance(self):
        return self.balance

    def dict_to_string(self, dict):
        if dict["operation_type"] != "exchange":
            return f'type: {dict["operation_type"]} status: {dict["status"]} amount: {dict["amount_of_deposit"]} balance: {dict["total_balance"]}'
        else:
            return f'type: {dict["operation_type"]} status: {dict["status"]} pre exchange amount: {dict["pre_exchange_amount"]} exchange amount: {dict["exchange_amount"]} currency from: {dict["currency_from"]} currency to: {dict["currency_to"]}'
        

    def get_history(self):
        data_dicts = self.file_manager.load_data(self.hist_file_path)
        if self.file_manager.new_session:
            print('____ >> OLD Transaction History << ____')
            self.print_history(data_dicts)
        else:
            print('____ >> Your Transaction History << ____')
            self.print_history(data_dicts)
            

    def print_history(self, hist_dict):
        for item in hist_dict:
                print(self.dict_to_string(item))