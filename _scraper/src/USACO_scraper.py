import argparse
import re
from scraper import *
from USACO_common import *

def get_contest_from_link(link: str) -> str:
    contest = link['href'].replace('index.php?page=', '').replace('results', '')
    contest = '20' + contest[-2:] + contest[:-2]

    # USACO offical site provide past context problems since 2014 - 2015
    if int(contest[:4]) >= 2015 or int(contest[:4]) == '2014Dec':
        return contest

    return ''


class USACOScraper(Scraper):
    def __init__(self, data_file: str, host: str, force_updated=False) -> None:
        super().__init__(data_file, host, force_updated)

    def fetch_problem(self, link: str) -> dict:
        contest = get_contest_from_link(link)

        if contest:
            if contest not in self.data:
                self.data[contest] = {}

                problem_links = get_page_soup(host + link['href']).find_all('a', string='View problem')

                for problem_link in problem_links:
                    problem_data = self.get_problems(problem_link['href'], self.data[contest])
                    print(problem_data)

                return self.data[contest]
            else:
                print(f'Contest {contest} already exists')

        return {}

    def get_problems(self, link: str, data) -> dict:
        problem_soup = get_page_soup(host + link)
        panel_text = problem_soup.select('.panel')[0].text.strip()
        problem_text = problem_soup.select('.problem-text')[0].text.strip()

        division_match = re.search(r'(Bronze|Silver|Gold|Platinum)', panel_text)
        title_match = re.search(r'Problem\s+(\d+)\. (.+)', panel_text)
        io_format_match = re.search(r'INPUT(:| FORMAT) \((.*)\)', problem_text)

        if not division_match or not title_match:
            raise Exception('Problem page format is not correct, need manual check')

        division = division_match.group(0)
        number = title_match.group(1)
        title = title_match.group(2)

        io_file = io_format_match.group(2) if io_format_match else 'interactive'
        if 'stdin' in io_file:
            io_file = 'stdio'
        else:
            io_file = io_file.replace('file ', '').replace('.in', '')

        data.setdefault(division, {})[number] = {
            'title': title,
            'link': host + link,
            'whole_title': panel_text,
            'io_file': io_file
        }
        return data[division][number]

    def update_data(self) -> dict:
        results_links = get_page_soup(host + 'index.php?page=contests').select('a[href*="results"]')

        for link in results_links:
            self.fetch_problem(link)

        self.data = dict(sorted(self.data.items(), key=contests_sort_key, reverse=True))

        return self.data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='USACO scraper')
    parser.add_argument('-f', '--force_updated', action='store_true', help='force updated problems data (will overwrite existing data).')
    args = parser.parse_args()
    USACOScraper(data_file, host, args.force_updated).run()
