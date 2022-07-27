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
