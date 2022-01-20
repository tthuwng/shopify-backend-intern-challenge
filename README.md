# Shopify Backend Intern Challenge

An inventory tracking web application for a logistics company

## Functionalities

[Challenge Description](https://docs.google.com/document/d/1z9LZ_kZBUbg-O2MhZVVSqTmvDko5IJWHtuFmIu_Xg1A/edit?usp=sharing)

- Basic CRUD Functionality
  - Create inventory items
  - Edit Them
  - Delete Them
  - View a list of them
- Additional feature: Allow image uploads AND store image with generated thumbnails

## Dependencies

1. [Python 3](https://www.python.org/)
2. [Flask](https://flask.palletsprojects.com/en/2.0.x/)
3. [sqlite3](https://docs.python.org/3.8/library/sqlite3.html)

## Instructions

```
# create & activate python virtual environment
python3 -m venv venv
source venv/bin/activate

# install Flask
pip install Flask

# set environment variables
export FLASK_APP=main
export FLASK_ENV=development

# run server
flask run
```

Demo can be viewed at: http://127.0.0.1:5000/
