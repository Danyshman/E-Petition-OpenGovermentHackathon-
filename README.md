# E_petition
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
~~
### Start server

* enter virtual environment

```bash
source venv/bin/activate
```

* start django server

```bash
python manage.py runserver
```


##### Set automatic check for emails that have not been checked in two weeks and send them to responsible government branch

* you must use linux server that supports cron, make sure you have it by running ``crontab -l``


* open your crontab file

```bash
crontab -e
```

* schedule a new task that will run everyday at 10 am by inserting this line 

```bash
0 10 * * * * cd {path/to/this/project} && {path/to/this/project}/venv/bin/python manage.py sendreminders
```

change ``path/to/this/project`` to your absolute path
