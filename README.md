# trello-clone
A Trello made using Django Rest Framework, Redis, SASS and React.

## Features
- Register and Login
    - JWT Authentication to connect DRF and React
    - Can login with username or email
- Projects (Teams)
    - Create Projects
    - Invite members to join projects via one time link
    - Change member access level - Admin or Normal
        - Admin can edit project details, invite new members, and change other members' access levels.
- Boards
    - Create personal boards or project boards
    - Recently Viewed Boards
    - Starred Boards
    - Create and reorder lists
    - Create, reorder, and change list of cards
        - Add labels to cards
        - Assign members to cards
        - Add attachments to cards
        - Add comments to cards
    - Search
        - Autocomplete (Debounced)
    - Unsplash API Integration
        - Set environment variable REACT_APP_UNSPLASH_API_ACCESS_KEY with access key
    - Automatically adapt header and board title styling based on brightness of board background
- Notifications
    - When someone assigns you to a card
    - When someone comments on a card you're assigned to
    - When you're invited to a project
    - When someone makes you admin of a project

## Getting Started
1. Install [Python](https://www.python.org/downloads/), [Redis](https://redis.io/download).
2. Clone the repo
```
git clone https://github.com/amirkeyhani/trello
$ cd trello
```
3. Install [pipenv](https://pypi.org/project/pip/), a python virtual environment manager. Install backend dependencies and run migrations to create database. Default database is SQLite.
```
$ pip install pip
$ pip install virtualenv
$ cd backend
$ py -m venv env
$ run python manage.py migrate
```
4. Install frontend dependencies.
```
$ cd frontend
$ npm install
```
5. Run redis
``` 
$ redis-server
```
6. Run both frontend and backend servers with following commands in appropriate directories.
```
$ python manage.py runserver
$ npm start
```