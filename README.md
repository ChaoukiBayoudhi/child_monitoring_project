# Child monitoring project

A Django project with 4 models and a REST API (Django REST Framework).

## Tech stack

- Python 3
- Django
- Django REST Framework
- Database: PostgreSQL

## Project structure

- `child_monitoring_project/`: project settings and root URLs
- `child_app/`: Django app
- Tests: `child_app/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Person` | `child_app` | firstName, lastName, photo, birthdate |
| `Parent` | `child_app` | nb_children |
| `Child` | `child_app` | level, parent |
| `Task` | `child_app` | name, description, duration, start_date, end_date, state, task_type, child |

## URL routes

Declared in `urls.py`:

- `/parents/ (router)`
- `/children/ (router)`
- `/tasks/ (router)`
- `/blog/`
- `/monitoring/`

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install django djangorestframework psycopg2-binary
python manage.py migrate
python manage.py runserver
```

There is no `requirements.txt`; the packages above are the ones the settings and imports refer to.

`settings.py` is configured for PostgreSQL: create the database and use your own credentials before running `migrate`.

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
