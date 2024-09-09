from FileManager import FileManager
from HistoryMessages import HistoryMessages
import requests

class CurrencyExchange:
    def __init__(self, balance = 0):
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        self.balance = balance

    def write_to_history(self, hist_dict):
        self.file_manager.add_to_json(hist_dict, self.hist_file_path) 
    

    def get_exchange_rates(self):
        url = 'https://fake-api.apps.berlintech.ai/api/currency_exchange'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code}")
 
    
    def exchange_currency(self, currency_from, currency_to, amount):
        exchange_rates = self.get_exchange_rates()
        status = 'failure'
        error_message = None

        if currency_from not in exchange_rates or currency_to not in exchange_rates:
            error_message = "Currency exchange failed"
            print(error_message)

        try:
            amount = float(amount)
            if amount <= 0:
                error_message = "Amount must be a positive number"
                print(error_message)
        except ValueError:
            error_message = 'Currency exchange failed!'
            print(error_message)

        if error_message:
            history_message = HistoryMessages.exchange(status, amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            return None

        status = 'success'
        source_rate = exchange_rates[currency_from]
        target_rate = exchange_rates[currency_to]

        amount_in_eur = amount / source_rate
        converted_amount = amount_in_eur * target_rate

        history_message = HistoryMessages.exchange(status, amount, converted_amount, currency_from, currency_to)
        self.write_to_history(history_message)

        return converted_amount
