Запуск top 
```
top cH -o PID -d 0.5
```
Перключать tasks \ threads -- H 

```
./manage.py runserver 0.0.0.0:8000 --noreaload --notreading
docker-compose exec my_webserver bash
gunicorn --bind 0.0.0.0:8000 --workers=4 --threads=4 my_webserver.wsgi

gunicorn --bind 0.0.0.0:8000 --workers=1 --threads=8 my_webserver.wsgi

gunicorn --bind 0.0.0.0:8000 --workers=8 my_webserver.wsgi

```

docker-compose up -d --force-recreate --build web
