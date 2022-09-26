# Catomancy

Catomancy is a small cat collection API based on the Django Rest Framework.

## Installation
To install this app, first set up a [virtual environment](https://docs.python.org/3.10/library/venv.html) and launch it as instructed. Then, use your CLI to navigate to the folder containing the requirements.txt file and run the following:

Windows, Mac:
```
pip install -r requirements.txt
```

Linux, UNIX:
```
pip3 install -r requirements.txt
```

Once the necessary packages are installed, navigate to the folder containing `manage.py` and type the following:

Windows, Mac:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Linux, UNIX:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

You are now ready to use the app.

## Usage

Still in the `manage.py` folder, type `python manage.py runserver` (for Windows/Mac) or `python3 manage.py runserver` (Linux, Unix).

Navigate to the URL designated in the CLI's output (it should be ̀ http://127.0.0.1:8000/`).

## Licence
This project uses the GNU general public licence. You are free to do as you wish with it, as it was designed for practice and cheerful nonsense anyway.