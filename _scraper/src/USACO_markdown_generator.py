from markdown_generator import *
from USACO_common import *


class USACOStat(MarkDownGenerator):
    def __init__(self, data_file: str) -> None:
        super().__init__(data_file)
        self.stat = {division: default_stat.copy() for division in divisions}
        self.total = {division: 0 for division in divisions}

    def generate_division_statistics(self, division: str) -> str:
        return f'#### {division} Solved {self.stat[division]["AC"]}/{self.total[division]} {self.stat[division]["AC"]/self.total[division]*100:.2f}%\n'

    def generate_statistics(self) -> None:
        md_text = ""

        for contest, contest_data in self.data.items():
            md_text += f'# {contest}\n\n'
            md_text += '| Problem | Problem Title | Problem Link | Code | Status |\n'
            md_text += '|---------|---------------|--------------|------|--------|\n'
            for division, division_data in contest_data.items():
                for problem, problem_data in division_data.items():
                    codefile = ''
                    for lang in languages:
                        if lang == 'cpp':
                            file_name =  f'{problem}.{lang}'
                            codefile = f'{get_problem_relative_path(contest, division)}/{file_name}'
                            with open(f'{get_problem_abosulute_path(contest, division)}/{file_name}', 'r') as f:
                                for line in f:
                                    if line.startswith('// status:'):
                                        status = line.split(
                                            '// status:')[1].strip()

                            if status != 'unsolved':
                                break

                        if lang == 'java':
                            file_name = f'{slugify_title(problem_data["title"])}.{lang}'
                            codefile = f'{get_problem_relative_path(contest, division)}/{file_name}'
                            with open(f'{get_problem_abosulute_path(contest, division)}/{file_name}', 'r') as f:
                                for line in f:
                                    if line.startswith('// status:'):
                                        status = line.split(
                                            '// status:')[1].strip()

                            if status != 'unsolved':
                                break

                        if lang == 'py':
                            file_name =  f'{problem}.{lang}'
                            codefile = f'{get_problem_relative_path(contest, division)}/{file_name}'
                            with open(f'{get_problem_abosulute_path(contest, division)}/{file_name}', 'r') as f:
                                for line in f:
                                    if line.startswith('# status:'):
                                        status = line.split(
                                            '# status:')[1].strip()

                    md_text += f'| {division} {problem} | {problem_data["title"]} | [Link]({problem_data["link"]}) | [{codefile}]({codefile}) | {status} |\n'
                    self.stat[division][status] += 1
                    self.total[division] += 1
            md_text += '\n'

        with open(f'{problems_root_path}/README.md', 'w') as f:
            f.write('# USACO\n' +
                    ''.join(self.generate_division_statistics(division) for division in divisions) + md_text)


if __name__ == '__main__':
    USACOStat(data_file).run()
