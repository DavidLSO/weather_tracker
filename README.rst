# Weather Tracker

## Requirements
1. Python 3.7
2. Google API Key
3. Dark Sky API Key
4. postgres

## Install
1. Create virtualenv python3 -m venv {name}
2. Start your env source bin activate
3. Install requirements pip install -r requirements/local.txt or requirements/production.txt
4. Run migrates python manage.py migrate
5. Start app python manage.py runserver

## Commands
In this project there is a command to create a file with the IPS that used the service

1. python manage.py export_data

## Environments

DJANGO_READ_DOT_ENV_FILE=True
DATABASE_URL=postgres://postgres:postgres@localhost:5432/weather_tracker
DJANGO_DEBUG=True
GOOGLE_API_KEY=
DARK_SKY_API_KEY=
EXPORT_PATH=
