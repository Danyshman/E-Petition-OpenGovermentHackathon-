# e_petition
Winner of Open Government Hakathon

### Set up

* create a virtual environment inside a root folder

```bash
virtualenv --no-site-packages --distribute -p /usr/bin/python3 venv
```

* enter virtual environment

```bash
source venv/bin/activate
```

* install dependencies

```bash
pip install -r requirements.txt
```

* run migrations

```bash
python manage.py migrate
```

### Start server

* enter virtual environment

```bash
source venv/bin/activate
```

* start django server

```bash
python manage.py runserver``