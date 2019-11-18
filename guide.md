# Tips for deployment

## Docker build & run

- Remember add tags to building image.
- Remember to add '-p' parameter to expose port.
- Remeber run `docker exec -it` into docker container to run `python manage.py createsuperuser` to active django admin settings.
- For every iteration, no need to manually run `python manage.py migrate` which is run by default during Docker build phrase.

## Docker image for postgres

- Using ver 11.5.
- First startup, run `createdb galilee` to initialize the db settings.
- Remember some `psql` commands to manipulate postgresql instance.
