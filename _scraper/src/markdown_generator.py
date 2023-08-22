import json
import os

default_stat = {
    'AC': 0, # Accepted
    'WA': 0, # Wrong Answer
    'TLE': 0, # Time Limit Exceeded
    'MLE': 0, # Memory Limit Exceeded
    'CE': 0, # Compile Error
    'RE': 0, # Runtime Error
    'PE': 0, # Presentation Error
    'unsolved': 0 # Not tried yet
}

class MarkDownGenerator:
    def __init__(self, data_file: str) -> None:
        self.data_file = data_file
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)

    def run(self) -> None:
        self.generate_statistics()


    def generate_statistics(self) -> None:
        raise NotImplementedError

if __name__ == '__main__':
    raise Exception('This file is not meant to be run directly')
