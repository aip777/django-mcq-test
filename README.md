### Clone project & Install Requirements
Activate python virtualenv
* virtualenv -p python3 .
* source bin/activate
* pip install -r requirements.txt

### Migrate
* cd src && python manage.py migrate

### Create Admin User

* python manage.py createsuperuser

### Run Server
* python manage.py runserver
