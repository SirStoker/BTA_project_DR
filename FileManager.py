import json

class FileManager:
    def __init__(self, new_session=True):
        self.new_session = new_session

    def save_data(self, filename, data):
        if self.new_session:
            self.new_session = False
            self.write_json([data], filename)
        else:
            self.add_to_json(data, filename)


    def add_to_json(self, data, json_file_path):
         data_exist = self.read_json(json_file_path)
         data_exist.append(data)
         self.write_json(data_exist, json_file_path)


    def read_json(self, json_file_path):
        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        return data
        

    def write_json(self, list_of_dicts, json_file_path):
        with open(json_file_path, 'w') as file:
            json.dump(list_of_dicts, file, indent=4)


    def load_data(self, filename):
        with open(filename, 'r') as file:
            try:
                return json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                return []

        
            