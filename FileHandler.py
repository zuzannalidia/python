class FileHandler:
    @staticmethod
    def save_to_file(file_name, data):
        with open(file_name, 'w') as file:
            file.write(data)

    @staticmethod
    def load_from_file(file_name):
        with open(file_name, 'r') as file:
            data = file.read()
            return data
