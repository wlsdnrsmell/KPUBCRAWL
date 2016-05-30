<h>첫걸음</h>
<h>가상 환경만들기</h>

mkdir KPUBCRAWING

python -m venv myvenv
myvenv\Scripts\activate

<h>장고설치</h>
pip install django == 1.8

django-admin startproject kpubcrawl .

python manage.py migrate

<h>어플리케이션 제작</h>
python manage.py startapp seoulcrawl

<h>models</h>
class info_client:
    firstname

python manage.py makemigrations seoulcrawl
python manage.py migrate seoulcrawl