import os
import json
from bs4 import BeautifulSoup
import requests


def get_page_content(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful
    return response.text


def get_page_soup(url: str) -> BeautifulSoup:
    return BeautifulSoup(get_page_content(url), 'html.parser')


class Scraper:
    def __init__(self, data_file: str, host: str, force_updated: bool) -> None:
        self.data_file = data_file
        self.host = host
        self.force_updated = force_updated
        self.data = {}

    def run(self) -> None:
        if not self.force_updated and os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)

        try:
            self.update_data()
        finally:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=2)

    def update_data(self) -> None:
        raise NotImplementedError


if __name__ == '__main__':
    raise Exception('This file is not meant to be run directly')
