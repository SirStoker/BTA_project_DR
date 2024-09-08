import json

class FileManager:
    def load_data(self, filename):
        pass
        # TODO:
        # Implement a process that reads the contents of the `filename` file 
        # and returns the text.

    def save_data(self, filename, data):
        try:
            with open(filename, 'r') as file:
                try:
                    data_file = json.load(file)
                except json.JSONDecodeError:
                    data_file = []
        except FileNotFoundError:
            data_file = []

        data_file.append(data)
    
        with open(filename, 'w') as file:
            json.dump(data_file, file, indent=4)
            file.write('\n')
        

    def read_json(self, json_file_path):
        pass
        # TODO:
        # Implement a process that reads the contents of a file whose path is stored in the `json_file_path` variable 
        # and returns a list of dictionaries
        
    def write_json(self, list_of_dicts, json_file_path):
        pass
        # TODO:
        # Implement a process that writes a list of dictionaries from list_of_dicts to the `json_file_path` file

    def add_to_json(self, data, json_file_path):
        pass
        # TODO:
        # Implement a process that gets the dictionary in the data variable and adds it to the JSON `json_file_path`

            