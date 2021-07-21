import argparse
import datetime
import shutil

def setup_line_modifications(line: str) -> str:
    return line.replace("_PACKAGE_NAME = 'PACKAGE'",
                        f"_PACKAGE_NAME = '{args.package_name}'")


def init_line_modifications(line: str) -> str:
    return line.replace("from PACKAGE.__about__ import *  # noqa: F401 F403", f"from {args.package_name}.__about__ import *  # noqa: F401 F403")

def about_line_modifications(line: str) -> str:
    line = line.replace('YEAR', str(datetime.datetime.today().year))
    line = line.replace('REPOSITORY', args.repository)
    return line

parser = argparse.ArgumentParser()
parser.add_argument('--package_name', default=None, type=str)
parser.add_argument('--repository', type=str)
args = parser.parse_args()
if args.package_name is None:
    args.package_name = args.repository.split('/', 1)[-1]

# Update content of setup.py
with open('setup.py', 'r') as f:
    content = [setup_line_modifications(x) for x in f.readlines()]
with open('setup.py', 'w') as f:
    f.writelines(content)

# Update content of __init__.py
with open('PACKAGE/__init__.py', 'r') as f:
    content = [init_line_modifications(x) for x in f.readlines()]
with open('PACKAGE/__init__.py', 'w') as f:
    f.writelines(content)

# Update content of __about__.py
with open('PACKAGE/__about__.py', 'r') as f:
    content = [about_line_modifications(x) for x in f.readlines()]
with open('PACKAGE/__about__.py', 'w') as f:
    f.writelines(content)

shutil.move('PACKAGE', args.package_name)


