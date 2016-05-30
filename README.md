#첫걸음

##가상 환경만들기

    mkdir KPUBCRAWING

    python -m venv myvenv
    myvenv\Scripts\activate

##장고설치
    pip install django == 1.8

    django-admin startproject kpubcrawl .

    python manage.py migrate

##어플리케이션 제작
    python manage.py startapp seoulcrawl

##models
    class info_client:
        firstname

    python manage.py makemigrations seoulcrawl
    python manage.py migrate seoulcrawl
##urls정규표현식
    ^ 문자열이 시작할 떄
    $ 문자열이 끝날 때
    \d 숫자
    + 바로 앞에 나오는 항목이 계속 나올 때
    () 패턴의 부분을 저장할 때