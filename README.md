# https://www.youtube.com/watch?v=Xts8NmyAc8c

mkdir rest_api
cd rest_api
python -m venv virtualenv
source virtualenv/bin/activate
pip install --upgrade pip
pip install Django
django-admin startproject drf .
django-admin startapp apiApp

python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser --username admin --email admin@example.com
python manage.py createsuperuser
pako
123123
python manage.py runserver

pip install djangorestframework