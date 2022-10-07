COFFEEACADEMY

INFORME

CASO APRESENTE ERRO EXECUTAR EM LINHA DE COMANDO:

(Windows - Obs.: não sei se o comando 'del' funciona no linux - usar comando correspondente)
1- del .\*\migrations\0*.py
2- del .\db.sqlite3
3- python manage.py makemigrations
4- python manage.py migrate
4- python manage.py runserver
