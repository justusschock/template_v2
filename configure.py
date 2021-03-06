import argparse
import os
import shutil

def setup_cfg_mods(line: str) -> str:
    line = line.replace("PACKAGE", args.package_name)
    line = line.replace("REPOSITORY", args.repository)
    line = line.replace("OWNER_EMAIL", f"{args.owner}@users.noreply.github.com")
    line = line.replace("OWNER", args.owner)
    if os.path.isfile('LICENSE.rst'):
        line = line.replace("LICENSE", "LICENSE.rst")
    elif not os.path.isfile('LICENSE') and 'LICENSE' in line:
        line = ''

    return line


parser = argparse.ArgumentParser()
parser.add_argument('--package_name', default=None, type=str)
parser.add_argument('--repository', type=str)
parser.add_argument('--owner', default=None, type=str)
args = parser.parse_args()
if args.package_name is None:
    args.package_name = args.repository.split('/', 1)[-1].replace('-', '_')

if args.owner is None:
    args.owner = args.repository.split('/', 1)[0]

with open('setup.cfg', 'r') as f:
    content = [setup_cfg_mods(l) for l in f.readlines()]
with open('setup.cfg', 'w') as f:
    f.writelines(content)

shutil.move("PACKAGE", args.package_name)




