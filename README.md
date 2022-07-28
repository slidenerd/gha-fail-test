# News

[https://pre-commit.com/#badging-your-repository]::

[https://github.com/PyCQA/flake8/issues/1256]::

[https://black.readthedocs.io/en/stable/#show-your-style]::

[https://pycqa.github.io/isort/#spread-the-word]::

[https://github.com/PyCQA/bandit#show-your-style]::

[https://github.com/python/mypy/blob/master/README.md]::

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit) [![linter: flake8](https://img.shields.io/badge/linter-flake8-success)](https://gitlab.com/pycqa/flake8) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/) [![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit) [![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

Load news items from various RSS feeds and store them to postgres database

[https://bryanavery.co.uk/github-naming-repositories/]::

## How this project was setup?

[https://stackoverflow.com/questions/12145232/create-an-automatically-numbered-list]::

### 1. Setup project

1. Create a new directory *news*

        mkdir news

1. Navigate to this directory

        cd news

1. Initialize git repository

        git init

1. Change branch name to *main* from *master*

        git branch -M main

1. Add a *.gitignore* file with Python specific exclusions
1. Add a *README.md* file
1. Add files and make an empty commit

        git add .
        git commit -m "build: setup project"

1. Link local with remote repository

        git remote add origin [https://github.com/Coinhexa/news.git](https://github.com/Coinhexa/news.git)

1. Save changes to remote repository

        git push -u origin main

### 2. Setup poetry

1. Create a new branch

        git checkout -b wip/setup-project

1. Install poetry for development

        curl -sSL https://install.python-poetry.org | python3 -

1. Check poetry is installed successfully

        poetry --version

1. Update poetry to latest stable version

        poetry self update

1. Show current poetry configuration

        poetry config --list

1. Make poetry create the virtual environment right within the project directory

        poetry config virtualenvs.in-project true

1. Create a new project inside an exisiting directory using

        # https://python-poetry.org/docs/cli/#init
        poetry init

1. It will ask a few questions on the command line and if you want the default answer selected or skip the question, press Enter

        Package name [code]:
        news
        Version [0.1.0]:
        # SKIP
        Description []:
        Load news items from various RSS feeds and store them to postgres database
        Author [Vivek Ramesh <coinhexa@gmail.com>, n to skip]:
        # SKIP
        License []:
        # SKIP
        Compatible Python versions [^3.10]:
        # SKIP
        Would you like to define your main dependencies interactively? (yes/no) [yes]
        no
        Would you like to define your development dependencies interactively? (yes/no) [yes]
        yes
        Search for package to add (or leave blank to continue):
        pytest
        Enter package # to add, or the complete package name if it is not listed:
        0
        Enter the version constraint to require (or leave blank to use the latest version):
        # SKIP
        Add a package:
        # SKIP
        Do you confirm generation? (yes/no) [yes]
        # SKIP

1. To Update pytest to the latest version forcefully beyond its constraints with poetry, run

        poetry add --dev pytest@latest

1. Add *src/news* and *tests* directories
1. Create *__init__.py* and *main.py* inside *src/news*
1. Create *__init__.py* and *test_main.py* and *test_news.py* inside *tests*
1. Add the following lines inside *src/news/__init__.py*

        """Main project."""

        __version__ = '0.1.0'

1. Add the following lines inside *src/news/main.py*

        """The main module."""


        def main():
            print('hello from news')
            return 1

1. Add the following lines inside *tests/__init__.py*

        """Main test file."""

1. Add the following lines inside *tests/test_main.py*

        """Write tests for the main function."""

        from news.main import main


        def test_main():
            assert main() == 1

1. Add the following lines inside *tests/test_news.py*

        """Write tests for the version number."""

        from news import __version__


        def test_version():
            assert __version__ == '0.1.0'

1. Add an entry point to run the project inside *pyproject.toml* file

        [tool.poetry.scripts]
        news = "news.main:main"

1. Install all dependencies and create lock file

        poetry install

1. Run the project using the command below

        poetry run news

1. Run tests using either of the commands below

        poetry run pytest tests

1. Save changes

        git add .
        git commit -m "build: setup poetry"
        git push origin wip/setup-project

### 3. Setup Tox

1. Switch branch

        git switch wip/setup-project

1. Install tox

        poetry add --dev tox

1. Create *tox.ini* file

        # https://python-poetry.org/docs/faq/#is-tox-supported
        [tox]
        isolated_build = true
        envlist = py310
        # https://tox.wiki/en/latest/config.html#conf-skipsdist
        skipsdist = true

        # We need this for passing environment variables down to tox
        # https://tox.wiki/en/latest/example/basic.html#passing-down-environment-variables
        [testenv]
        whitelist_externals = poetry
        commands =
                poetry install -v
                poetry run pytest tests/

1. Run tox

        poetry run tox

1. Run tox in verbose mode while recreating the environment

        # https://tox.wiki/en/latest/config.html#cmdoption-tox-v
        # https://tox.wiki/en/latest/config.html#cmdoption-tox-r
        poetry run tox --verbose --recreate

1. Save changes

        git add .
        git commit -m "build: setup tox"
        git push origin head

### 4. Setup pre-commit

1. Switch branch

        git switch wip/setup-project

1. Install pre-commit

        poetry add --dev pre-commit

1. Check if installation was successful

        poetry run pre-commit --version

1. Create *.pre-commit-config.yaml* with only one repo inside, namely *pre-commit-hooks*
1. Install pre-commit hooks

        poetry run pre-commit install

1. Modify *.pre-commit-config.yaml* file to add all the necessary checks

1. Run pre-commit

        poetry run pre-commit run --all-files

1. Run pre-commit in verbose mode

        poetry run pre-commit run --all-files --verbose

1. Update hooks to their latest version

        poetry run pre-commit autoupdate

1. Clean pre-commit cache

        poetry run pre-commit clean && poetry run pre-commit gc

1. Uninstall pre-commit

        poetry run pre-commit uninstall

1. Modify *tox.ini* and add a line under [testenv]

        # https://pre-commit.com/#usage-with-tox
        passenv = SSH_AUTH_SOCK

1. Save changes

        git add .
        git commit -m "build: setup pre-commit"
        git push origin head

### 5. Setup commitizen

1. Switch branch

        git switch wip/setup-project

1. Install commitizen

        poetry add --dev commitizen

1. Help

        poetry run cz --help

1. Run commitizen init

        poetry run cz init
        Please choose a supported config file: (default: pyproject.toml)
        pyproject.toml
        Please choose a cz (commit rule): (default: cz_conventional_commits)
        cz_conventional_commits
        # https://commitizen-tools.github.io/commitizen/bump/#tag_format
        Please enter the correct version format: (default: "$version")
        v$major.$minor.$patch$prerelease
        Do you want to install pre-commit hook?
        Yes

1. Change version to 0.1.0 under [tool.commitizen] inside *pyproject.toml*
1. Check if all previous commit messages follow conventional commit standards

        poetry run cz check --rev-range main..HEAD

1. Check if commitizen works by doing a commit message with incorrect format

        git add .
        git commit -m "this should fail"

1. Undo staged files if any from the previous step and now add the correct commit message
1. Save changes

        git add .
        poetry run cz commit # set message to build: setup commitizen
        git push origin head

### 6. Setup pytest-cov

1. Create new branch

        git checkout -b wip/setup-code-quality-tools

1. Install pytest-cov

        poetry add --dev pytest-cov

1. Check if coverage is installed properly

        poetry run coverage --version

1. Help

        # https://coverage.readthedocs.io/en/6.4.2/cmd.html#command-line-usage
        poetry run coverage help
        poetry run coverage help run
        poetry run coverage run --help

1. Erase collected data

        # https://coverage.readthedocs.io/en/6.4.2/cmd.html#erase-data-coverage-erase
        poetry run coverage erase

1. Debug coverage file

        # https://coverage.readthedocs.io/en/6.4.2/cmd.html#diagnostics-coverage-debug
        poetry run coverage debug --help
        poetry run coverage debug data
        poetry run coverage debug sys
        poetry run coverage debug config

1. Add the following sections to *pyproject.toml*

        # https://coverage.readthedocs.io/en/6.4.2/config.html#syntax
        [tool.coverage.run]
        # https://coverage.readthedocs.io/en/6.4.2/config.html#run-branch
        branch = true
        # https://coverage.readthedocs.io/en/6.4.2/config.html#run-source
        source = ["news"]

        [tool.coverage.report]
        # https://coverage.readthedocs.io/en/6.4.2/config.html#report-fail-under
        fail_under = 100

1. Modify the pytest command inside *tox.ini* so that it collects coverage only from src

        poetry run pytest --cov

1. Save changes

        git add .
        poetry run cz commit # set message to build: setup coverage with pytest-cov
        git push origin head

### 7. Setp pytest-sugar

1. Switch branch

        git switch wip/setup-code-quality-tools

1. Install pytest-sugar

        poetry add --dev pytest-sugar

1. Run pytest without sugar

        poetry run pytest --cov -p no:sugar

1. Save changes

        git add .
        poetry run cz commit # set message to build: setup pytest-sugar
        git push origin head

### 8. Setp pytest-clarity

1. Switch branch

        git switch wip/setup-code-quality-tools

1. Install pytest-clarity

        poetry add --dev pytest-clarity

1. Modify *tox.ini* to run pytest with pytest-clarity. The plugin will only be activated when the -vv option is supplied to pytest

        poetry run pytest --cov -vv

1. Save changes

        git add .
        poetry run cz commit # set message to build: setup pytest-clarity
        git push origin head

### 9. Setup Flake8

1. Switch branch

        git switch wip/setup-code-quality-tools

1. Install flake8

        poetry add --dev flake8

1. Check if flake8 is installed properly

        poetry run flake8 --version

1. Help

        poetry run flake8 --help

1. Add the following section to *tox.ini*
[flake8]

        # https://flake8.pycqa.org/en/latest/user/using-hooks.html#usage-with-the-pre-commit-git-hooks-framework
        # https://github.com/PyCQA/flake8/blob/main/src/flake8/defaults.py
        # See the defaults for everything above before you change anything

        # PEP-8 The following are ignored:
        # E731 do not assign a lambda expression, use a def
        # E203 whitespace before ':'
        # E501 line too long
        # W503 line break before binary operator
        # W605 invalid escape sequence
        # https://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-extend-exclude
        extend-exclude = .venv
        # https://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-extend-ignore
        extend-ignore = E731, E203, E501, W503, W605
        # https://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-max-complexity
        max-complexity = 10
        # https://stackoverflow.com/questions/65809122/how-to-format-this-code-so-that-flake8-is-happy/65908896#65908896
        # Make the changes as per the answer above to make flake8 compatible with black
        # https://black.readthedocs.io/en/stable/guides/using_black_with_other_tools.html#flake8
        max-line-length = 88

1. Add a hook for flake8 inside *.pre-commit-config.yml*

        - repo: https://github.com/PyCQA/flake8
          rev: 4.0.1
          # https://flake8.pycqa.org/en/latest/user/using-hooks.html
          hooks:
                - id: flake8
                  description: Command-line utility for enforcing style consistency across Python projects.
                  require_serial: true

1. Add a line inside *tox.ini* to run flake8 in verbose mode

        poetry run flake8 --verbose

1. Save changes

        git add .
        poetry run cz commit # set message to build: setup flake8
        git push origin head

### 10. Setup flake8-bugbear

1. Switch branch

        git switch wip/setup-code-quality-tools

1. Install flake8-bugbear

        poetry add --dev flake8-bugbear

1. Check if flake8-bugbear is installed properly. The command below should show flake8-bugbear in the output

        poetry run flake8 --version

1. Add a line to *tox.ini* configuration file under[flake8] to enable flake8-bugbear optional warnings

        # https://github.com/PyCQA/flake8-bugbear
        extend-select = B9

1. Modify *.pre-commit-config.yaml* file to add flake8-bugbear as an additional dependency

        - repo: https://github.com/PyCQA/flake8
          rev: 4.0.1
          # https://flake8.pycqa.org/en/latest/user/using-hooks.html
          hooks:
                - additional_dependencies: [flake8-bugbear==22.7.1]
                  id: flake8
                  description: Command-line utility for enforcing style consistency across Python projects.
                  require_serial: true

1. Save changes

        git add .
        poetry run cz commit # set message to build: setup flake8-bugbear
        git push origin head

### 11. Setup flake8-docstrings

1. Switch branch

        git switch wip/setup-code-quality-tools

1. Install flake8-docstrings

        poetry add --dev flake8-docstrings

1. Check if flake8-docstrings is installed properly. The command below should show flake8-docstrings in the output

        poetry run flake8 --version

1. Add a line to *tox.ini* configuration file under [flake8] to set flake8-docstrings convention

        # https://github.com/PyCQA/flake8-docstrings
        docstring-convention = google

1. Modify *.pre-commit-config.yaml* file to add flake8-docstrings as an additional dependency

        - repo: https://github.com/PyCQA/flake8
          rev: 4.0.1
          # https://flake8.pycqa.org/en/latest/user/using-hooks.html
          hooks:
                - additional_dependencies: [flake8-bugbear==22.7.1, flake8-docstrings==1.6.0]
                  id: flake8
                  args: [--verbose]
                  description: Command-line utility for enforcing style consistency across Python projects.
                  require_serial: true

1. Save changes

        git add .
        poetry run cz commit # set message to build: setup flake8-docstrings
        git push origin head

### 12. Setup black

1. Switch branch

        git switch wip/setup-code-quality-tools

1. Install black

        poetry add --dev black

1. Check if black is installed properly

        poetry run black --version

1. Help

        poetry run black --help

1. Add a hook for black inside *.pre-commit-config.yml*

        - repo: https://github.com/psf/black
          rev: 22.6.0
          # https://black.readthedocs.io/en/stable/integrations/source_version_control.html#version-control-integration
          hooks:
                - description: The uncompromising Python code formatter
                  id: black
                  args: [src, tests, --verbose]
                  require_serial: true

1. Add a comment to the *tox.ini* configuration file under the section [flake8] referencing the minimal setup needed to make flake8 work with black
1. Add a line inside *tox.ini* to run black in verbose mode

        poetry run black src tests --verbose

1. Run black without formatting to only show what will change

        poetry run black src tests --diff

1. Save changes

        git add .
        poetry run cz commit # set message to build: setup black
        git push origin head

### 13. Setup isort

1. Switch branch

        git switch wip/setup-code-quality-tools

1. Install isort

        poetry add --dev isort

1. Check if isort is installed properly

        poetry run isort --version

1. Help

        poetry run isort --help

1. Modify *pyproject.toml* file to add the following lines

        # https://pycqa.github.io/isort/docs/configuration/black_compatibility.html#using-a-config-file-such-as-isortcfg
        [tool.isort]
        # https://pycqa.github.io/isort/docs/configuration/profiles.html
        profile = black
        # https://pycqa.github.io/isort/docs/configuration/options.html#src-paths
        src_paths = src,tests
        # https://pycqa.github.io/isort/docs/configuration/options.html#skip-gitignore
        skip_gitignore = true
        # https://pycqa.github.io/isort/docs/configuration/options.html#force-single-line
        force_single_line = true
        # https://pycqa.github.io/isort/docs/configuration/options.html#atomic
        atomic = true
        # https://pycqa.github.io/isort/docs/configuration/options.html#color-output
        color_output = true

1. Add a hook for isort inside *.pre-commit-config.yaml*

        - repo: https://github.com/pycqa/isort
          rev: 5.10.1
          # https://pycqa.github.io/isort/docs/configuration/pre-commit.html#isort-pre-commit-step
          hooks:
                - args: [--verbose]
                  description: Library to sort imports alphabetically, and automatically separated into sections and by type
                  id: isort
                  require_serial: true

1. Add a line inside *tox.ini* to run isort in verbose mode

        poetry run isort . --verbose

1. Show the changes that isort will make without making those changes

        poetry run isort . --diff

1. Show current isort configuration

        poetry run isort . --show-config

1. Show files on which isort will run

        poetry run isort . --show-files

1. Modify *main.py* with incorrectly ordered imports to check if isort fixes them before committing
1. Save changes

        git add .
        poetry run cz commit # set message to build: setup isort
        git push origin head

### 14. Setup bandit

1. Switch branch

        git switch wip/setup-code-quality-tools

1. Install bandit

        poetry add --dev bandit

1. Check if bandit is installed properly

        poetry run bandit --version

1. Help

        poetry run bandit --help

1. Add a hook for bandit inside *.pre-commit-config.yaml* file

        - repo: https://github.com/PyCQA/bandit
        rev: 1.7.4
        # https://bandit.readthedocs.io/en/latest/start.html#version-control-integration
        hooks:
                - args: [--verbose]
                  description: Bandit is a tool for finding common security issues in Python code
                  # The config file's exclude seems to have no effect here, so adding a separate exclude clause
                  exclude: tests/.*$
                  id: bandit

1. We run bandit only on files contained in the *src* folder and not on *tests*
1. Add a line inside *tox.ini* to run bandit in verbose mode recursively inside *src* folder

        poetry run bandit src --recursive --verbose

1. Save changes

        git add .
        poetry run cz commit # set message to build: setup bandit
        git push origin head

### 15. Setup mypy

1. Switch branch

        git switch wip/setup-code-quality-tools

1. Install mypy

        poetry add --dev mypy

1. Check if mypy is installed properly

        poetry run mypy --help

1. Modify *pyproject.toml* file to add the following lines

        # https://mypy.readthedocs.io/en/stable/config_file.html#example-pyproject-toml
        [tool.mypy]
        # What mypy excludes by default https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-exclude
        # https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-pretty
        pretty = true
        # https://mypy.readthedocs.io/en/stable/config_file.html#configuring-error-messages
        show_column_numbers = true
        show_error_codes = true
        show_error_context = true
        # https://mypy.readthedocs.io/en/stable/config_file.html#confval-strict
        strict = true
        # https://mypy.readthedocs.io/en/stable/config_file.html#configuring-warnings
        warn_unreachable = true

1. Add a hook for mypy inside *.pre-commit-config.yaml* file

        - repo: https://github.com/pre-commit/mirrors-mypy
          rev: v0.971
          hooks:
                - args: ["--verbose"]
                  description: Type checking for Python
                  exclude: tests/.*$
                  id: mypy

1. Add an empty *py.typed* file
1. We run mypy only on files contained in the *src* folder and not on *tests*
1. Add a line inside *tox.ini* to run mypy in verbose mode inside the *src* folder

        poetry run mypy src --verbose

1. Save changes

        git add .
        poetry run cz commit # set message to build: setup mypy
        git push origin head

### 16. Setup typeguard

1. Switch branch

        git switch wip/setup-code-quality-tools

1. Install typeguard

        poetry add --dev typeguard

1. Modify *main.py* by adding the function below to check if typeguard works

        def check_if_typeguard_works(num: int) -> int:
                """A function to check if typeguard is running correctly."""
                return num

1. Modify *test_main.py* by adding the following lines to test the function defined above

        import pytest
        from news.main import check_if_typeguard_works
        def test_typeguard() -> None:
                """This function will test if typeguard is working or not."""
                import json

                data = json.loads('{ "language": "wtf" }')
                with pytest.raises(TypeError):
                        check_if_typeguard_works(data["language"])

1. Tests should fail if run currently

        poetry run pytest --cov

1. To make the tests suceed, setup pytest with typeguard checks

        poetry run pytest --typeguard-packages=news --cov

1. Modify the pytest command inside *tox.ini*

        # https://typeguard.readthedocs.io/en/latest/userguide.html#using-the-pytest-plugin
        poetry run pytest --typeguard-packages=news --cov

1. Save changes

        git add .
        poetry run cz commit # set message to build: setup typeguard
        git push origin head

### 17. Setup pyupgrade

1. Switch branch

        git switch wip/setup-code-quality-tools

1. Modify *.pre-commit-config.yaml* file to add a hook for pyupgrade

        - repo: https://github.com/asottile/pyupgrade
          rev: v2.37.2
          hooks:
                - id: pyupgrade

1. Save changes

        git add .
        poetry run cz commit # set message to build: setup pyupgrade
        git push origin head

### 18.Setup darglint

1. Switch branch

        git switch wip/setup-code-quality-tools

1. Install darglint

        poetry add --dev darglint

1. Check if darglint was installed successfully

        poetry run darglint --version

1. Run darglint in verbose mode

        poetry run darglint src --verbosity=2
        poetry run darglint tests --verbosity=2

1. Modify *.pre-commit-config.yaml* file to add a hook for darglint

        - repo: https://github.com/terrencepreilly/darglint
          rev: v1.8.1
          hooks:
                - description: A functional docstring linter which checks whether a docstring's description matches the actual function/method implementation.
                  id: darglint

1. Modify *tox.ini* to add a setting for darglint under [flake8]

        # https://github.com/terrencepreilly/darglint#flake8
        docstring_style = google

1. Save changes

        git add .
        poetry run cz commit # set message to build: setup darglint
        git push origin head

### 19. Setup xdoctest

1. Switch branch

        git switch wip/setup-code-quality-tools

1. Install xdoctest

        poetry add --dev xdoctest

1. Help

        poetry run xdoctest --help

1. Modify *main.py* to add an incorrect doc to check if xdoctest catches it

        Example:
                >>> add(0, 1)
                2

1. Change the above result with the correct one following the error

        Example:
                >>> add(0, 1)
                1

1. Modify the pytest command inside *tox.ini* to run xdoctest

        poetry run pytest --typeguard-packages=news --xdoctest --cov

1. Save changes

        git add .
        poetry run cz commit # set message to build: setup xdoctest
        git push origin head

### 20. Add badges in README

1. Switch branch

        git switch wip/setup-code-quality-tools

1. Find README badges wherever available for the above libraries and add them to *README.md*
1. Save changes

        git add .
        poetry run cz commit # set message to docs: add badges to README
        git push origin head

### 21. Add GitHub templates

1. Switch branch

        git switch wip/setup-code-quality-tools

1. Add templates for issue, feature, pull request and question and a config file to disable creating blank issues
1. Save changes

        git add .
        poetry run cz commit # set message to docs: setup github templates
        git push origin head
