# TemanRaga

TemanRaga adalah

## Install Guide

Disclaimer: this instruction guide was run with Windows, other OS might have slightly diffrent approach.

Clone

```bash
git clone https://github.com/TemanRaga/temanraga-be
```

Create environment

```bash
python -m venv env
```

Activate environment

```bash
env/bin/activate
```

Install requirement

```bash
pip install -r requirements.txt
```

Run

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Development

- Create a new branch from `main` with:
  ```bash
  $ git checkout -b <your_name/scope>
  ```
- example:
  - `bambang/my_scope`
- Do your changes, then push to remote repository to be merged
  ```bash
  $ git add .
  $ git commit -m "<tag>(<scope>): <description>"
  $ git push origin <your branch>
  ```
- examples of a _good_ commit message:
  - `feature(class): Implemented class model`
  - `fix(auth): Fix logging in not returning token`
  - `refactor(class search): Optimize searching`
- Submit merge request on the remote repository, wait for approvals, then merge if approved. You don't have to squash/delete the source branch after merge.
- After merge:
  ```bash
  $ git checkout main (or the target branch on the merge request)
  $ git pull origin main
  ```
- **Repeat**

# API Documentation

> Will be added later
