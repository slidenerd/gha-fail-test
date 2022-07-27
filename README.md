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
