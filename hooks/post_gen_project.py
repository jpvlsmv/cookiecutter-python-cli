#!/usr/bin/env python
import os
from subprocess import run

def addback_newlines():
    """Adds newlines back to every file, to make them PEP8 compliant."""
    root_path = os.getcwd()
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            if path.endswith('.py'):
                with open(path, 'rb') as f:
                    contents = f.read()

                if not contents.endswith(b'\n'):
                    with open(path, 'wb') as f:
                        f.write((contents + b'\n').lstrip())

def initialize_repo():
    try:
        run("git init".split())
        run(("git remote add github " +
                   "https://{{ cookiecutter.github_username }}@github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git").split())
    except CalledProcessError as e:
        print('Repository initialization failed' + e)

def initialize_venv():
    try:
        run("python -m venv .venv".split())
        run("poetry run pip install nox".split())
    except CalledProcessError as e:
        print('Virtual Environment setup failed' + e)
        
if __name__ == '__main__':
    addback_newlines()
    initialize_repo()
    initialize_venv()
