# start a python3 virtual environment, install django, and django rest framework
mkdir expense_calculator
cd expense_calculator
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install django django-rest-framework
django-admin startproject expense_calculator .
django-admin startapp expenses
python manage.py migrate
python manage.py runserver
