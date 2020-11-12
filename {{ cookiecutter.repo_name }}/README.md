# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

# Usage

To use it:

    $ {{ cookiecutter.script_name }} --help


# Build environment installation

First, make sure we have the right python versions
`sudo add-apt-repository ppa:deadsnakes/ppa
 sudo apt-get install -y python3.7 python3.7-venv python3.9 python3.9-venv`

 Next, install poetry:
 `pip3 install poetry`

 Finally, make it runnable
 `poetry run poetry install`

## IDE
A number of Visual Studio Code config settings are in the .vscode/ directory,
and are applicable if you open the {{ cookiecutter.project_name }}.code-workspace

## Testing
Default test run (just pytest on modern python version): `poetry run nox`

Full test of everything-- lint, multiple py versions, style: `poetry run nox -s all`
