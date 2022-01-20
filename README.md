Shopify Backend Intern Challenge

### [Functionalities](https://docs.google.com/document/d/1z9LZ_kZBUbg-O2MhZVVSqTmvDko5IJWHtuFmIu_Xg1A/edit?usp=sharing):

- Basic CRUD Functionality
  - Create inventory items
  - Edit Them
  - Delete Them
  - View a list of them
- Additional feature: Allow image uploads AND store image with generated thumbnails

### Dependencies:

1. [Python 3](https://www.python.org/)
2. [Flask](https://flask.palletsprojects.com/en/2.0.x/)
3. [sqlite3](https://docs.python.org/3.8/library/sqlite3.html)

## Instructions

1. Clone the repository
2. Create & activate python virtual environment

```
python3 -m venv venv
. venv/bin/activate # for macOS/Linux
venv\Scripts\activate # for Windows
```

3. Install Flask

```
pip install Flask
```

4. Run the server

```
FLASK_APP=main.py FLASK_ENV=development
flask run
```

Local API calls can be made at: http://127.0.0.1:5000/
