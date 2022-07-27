# News

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
