## First run

#### Helpful links
[Install virtualenvwrapper for ubuntu](http://roundhere.net/journal/virtualenv-ubuntu-12-10/)

[Install virtualenvwrapper for windows](https://pypi.python.org/pypi/virtualenvwrapper-win/)


#### Create virtual environment
```cmd
mkvirtualenv parserville
```

#### Activate virtual environment
```cmd
workon parserville
```

#### Install packaged from requirements.txt file into virtual environment
```cmd
pip install -r requirements.txt
```

##### Don't forget setup 'src' as working directory

#### Run migration commands
*In case when cannot found db, create empty folder 'db' inside src
```cmd
python manage.py migrate
python manage.py makemigrations parseville
python manage.py migrate parseville
```

#### First run of server
```cmd
python manage.py runserver 0.0.0.0:8000
```

## Management commands
** Setup first queries to db
```cmd
python manage.py initialization
```

** Parse companies info
```cmd
python manage.py parse
```

** Parse vacancy info
```cmd
python manage.py parsevacancy
```

## API description*
* / index page
* /api/get-vacancies 
* /api/get-companies
