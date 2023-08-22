import os
from slugify import slugify

host = 'http://www.usaco.org/'
name = 'USACO'
languages = ('cpp', 'java', 'py')

curr_path = (os.path.dirname(os.path.abspath(__file__)))
root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
data_file = os.path.join(root_path, f'data/{name}.json')
problems_root_path = os.path.join(root_path, f'../{name}')
cpp_template_path = os.path.join(problems_root_path, '_template.cpp')
java_template_path = os.path.join(problems_root_path, '_template.java')
py_template_path = os.path.join(problems_root_path, '_template.py')

divisions = ['Bronze', 'Silver', 'Gold', 'Platinum']

def get_problem_relative_path(contest, division):
    return f'{contest}/{division}'

def get_problem_abosulute_path(contest, division):
    return os.path.join(problems_root_path, get_problem_relative_path(contest, division))


def contests_sort_key(contest):
    month_order = {'jan': 0, 'feb': 1, 'mar': 2, 'apr': 3, 'may': 4, 'jun': 5,
                   'jul': 6, 'aug': 7, 'sep': 8, 'oct': 9, 'nov': 10, 'dec': 11, 'open': 12}

    year, month = contest[0][:4], contest[0][4:]

    return int(year), month_order[month]

def slugify_title(title):
    return slugify(title, separator="", lowercase=False)
