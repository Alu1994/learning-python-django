# learning-python-django

## helpfull comands

### - Executes/run project
```shell
python manage.py runserver
```

### - Install virtual env
```shell
pip install virtualenv
```

### - Creates virtual env
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

### - Install django
```shell
pip install Django
```

### - Check django version
```shell
django-admin --version
```

### - Create new django project
```shell
django-admin startproject (project_name) .
```

### - Create migrations
```shell
python manage.py makemigrations learning_logs
```

### - Apply migrations
```shell
python manage.py migrate
```

### - Enter shell
```shell
python manage.py shell
```
