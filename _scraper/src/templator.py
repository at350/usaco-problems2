import json
import os

class Templator:
    def __init__(self, data_file: str) -> None:
        self.data_file = data_file
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)

    def run(self) -> None:
        self.generate_templates()


    def generate_templates(self) -> None:
        raise NotImplementedError

if __name__ == '__main__':
    raise Exception('This file is not meant to be run directly')
