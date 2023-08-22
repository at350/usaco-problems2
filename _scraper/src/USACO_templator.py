from pathlib import Path
from typing import Literal
from templator import *
from USACO_common import *


def get_file_io(io_file: str, lang: Literal["cpp", "java", "py"], indent: int) -> str:
    if lang == 'java':
        if io_file == 'stdio' or io_file == 'interactive':
            return f'{" "*indent}BufferedReader in = new BufferedReader(new InputStreamReader(System.in));\n{" "*indent}PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));\n'
        return f'{" "*indent}BufferedReader in = new BufferedReader(new FileReader("{io_file}.in"));\n{" "*indent}PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("{io_file}.out")));\n'
    if io_file == 'stdio' or io_file == 'interactive':
        return ''
    if lang == 'cpp':
        return f'{" "*indent}freopen("{io_file}.in", "r", stdin);\n{" "*indent}freopen("{io_file}.out", "w", stdout);\n'
    if lang == 'py':
        return f'{" "*indent}sys.stdin = open("{io_file}.in", "r")\n{" "*indent}sys.stdout = open("{io_file}.out", "w")\n'


class USACOTemplator(Templator):
    def __init__(self, data_file: str) -> None:
        super().__init__(data_file)

    def generate_templates(self) -> None:
        cpp_indent = 4
        with open(cpp_template_path, 'r') as cpp_template:
            cpp_template = cpp_template.read()

        java_indent = 8
        with open(java_template_path, 'r') as java_template:
            java_template = java_template.read()

        py_indent = 4
        with open(py_template_path, 'r') as py_template:
            py_template = py_template.read()

        for contest, contest_data in self.data.items():
            for division, division_data in contest_data.items():
                for problem, problem_data in division_data.items():
                    whole_title = problem_data['whole_title']
                    file_name = slugify_title(problem_data['title'])

                    problem_path = Path(get_problem_abosulute_path(contest, division))
                    if not problem_path.exists():
                        os.makedirs(problem_path)

                    if 'cpp' in languages:
                        with open(f'{problem_path}/{problem}.cpp', 'w') as f:
                            first_line, second_line = whole_title.split(' \n ')
                            f.write(f'// {first_line}\n')
                            f.write(f'// {second_line}\n')
                            f.write(f'// link: {problem_data["link"]}\n')
                            f.write('// status: unsolved\n')
                            f.write('// tag:\n')
                            f.write('\n')
                            f.write(cpp_template.replace(
                                f'{" "*cpp_indent}// __IO_PLACEHOLDER__\n', get_file_io(problem_data['io_file'], 'cpp', cpp_indent)))

                    if 'java' in languages:
                        with open(f'{problem_path}/{file_name}.java', 'w') as f:
                            first_line, second_line = whole_title.split(' \n ')
                            f.write(f'// {first_line}\n')
                            f.write(f'// {second_line}\n')
                            f.write(f'// link: {problem_data["link"]}\n')
                            f.write('// status: unsolved\n')
                            f.write('// tag:\n')
                            f.write('\n')
                            f.write(java_template.replace(
                                f'{" "*java_indent}// __IO_PLACEHOLDER__\n', get_file_io(problem_data['io_file'], 'java', java_indent))
                                .replace('public class _template', f'public class {file_name}'))

                    if 'py' in languages:
                        with open(f'{problem_path}/{problem}.py', 'w') as f:
                            first_line, second_line = whole_title.split(' \n ')
                            f.write(f'# {first_line}\n')
                            f.write(f'# {second_line}\n')
                            f.write(f'# link: {problem_data["link"]}\n')
                            f.write('# status: unsolved\n')
                            f.write('# tag:\n')
                            f.write('\n')
                            f.write(py_template.replace(
                                f'{" "*py_indent}# __IO_PLACEHOLDER__\n', get_file_io(problem_data['io_file'], 'py', py_indent)))

                    print(
                        f'Generated template for, {first_line}, {second_line}')


if __name__ == '__main__':
    USACOTemplator(data_file).run()
