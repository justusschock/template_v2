import setuptools
setuptools.setup()

_PATH_ROOT = os.path.realpath(os.path.dirname(__file__))
_PACKAGE_NAME = 'PACKAGE'

# adapted from https://github.com/PyTorchLightning/metrics
def _load_py_module(fname, pkg=_PACKAGE_NAME):
    spec = spec_from_file_location(os.path.join(pkg, fname), os.path.join(_PATH_ROOT, pkg, fname))
    py = module_from_spec(spec)
    spec.loader.exec_module(py)
    return py

def _load_requirements(path_dir: str, file_name: str = 'requirements.txt', comment_char: str = '#') -> List[str]:
    """Load requirements from a file

    >>> _load_requirements(_PROJECT_ROOT)  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    ['numpy...', 'torch...']
    """
    with open(os.path.join(path_dir, file_name), 'r') as file:
        lines = [ln.strip() for ln in file.readlines()]
    reqs = []
    for ln in lines:
        # filer all comments
        if comment_char in ln:
            ln = ln[:ln.index(comment_char)].strip()
        # skip directly installed dependencies
        if ln.startswith('http'):
            continue
        if ln:  # if requirement is not empty
            reqs.append(ln)
    return reqs
about = _load_py_module('__about__.py')

# https://packaging.python.org/discussions/install-requires-vs-requirements /
# keep the meta-data here for simplicity in reading this file... it's not obvious
# what happens and to non-engineers they won't know to look in init ...
# the goal of the project is simplicity for researchers, don't want to add too much
# engineer specific practices
setup(
    name=_PACKAGE_NAME,
    version=about.__version__,
    description=about.__docs__,
    author=about.__author__,
    author_email=about.__author_email__,
    url=about.__homepage__,
    download_url=os.path.join(about.__homepage__, 'archive', 'master.zip'),
    license=about.__license__,
    packages=find_packages(exclude=['tests', 'tests.*', 'docs']),
    #long_description=about.__long_doc__,
    #long_description_content_type='text/markdown',
    include_package_data=True,
    zip_safe=False,
    keywords=['deep learning', 'machine learning', 'pytorch', 'metrics', 'AI'],
    python_requires='>=3.7',
    setup_requires=[],
    install_requires=_load_requirements(_PATH_ROOT),
    project_urls={
        # TODO
    },
   
)