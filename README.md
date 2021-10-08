# InternetStore

1. docker-compose run web python manage.py loaddata fixture.json
2. docker-compose run web python manage.py makemigrations
3. docker-compose run web python manage.py migrate
4. sudo docker-compose up --build
