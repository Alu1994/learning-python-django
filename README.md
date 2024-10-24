# learning-python-django
learning-python-django


## helpfull comands

### - executes/run project
```shell
python manage.py runserver
```

### - install virtual env
```shell
pip install virtualenv
```

### - creates virtual env
```shell
python -m venv (env_name)
```

### - Initializes virtual env
```shell
# - (executable) (path_to_file)
. ll_env/Scripts/activate
```

### - Generates requirements file with dependencies
```shell
pip freeze
pip freeze > requirements.txt
```

### - Install requirements file with dependencies
```shell
pip install -r requirements.txt
```

### - Finalizes virtual env
```shell
deactivate
```

### - install django
```shell
pip install Django
```

### - check django version
```shell
django-admin --version
```

### - create new django project
```shell
django-admin startproject (project_name) .
```

### - create migrations
```shell
python manage.py makemigrations learning_logs
```

### - apply migrations
```shell
python manage.py migrate
```

### - enter shell
```shell
python manage.py shell
```
