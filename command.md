docker-compose run --rm app sh -c "django-admin startproject e_commerce ."
docker volume ls
docker volume rm e-commerce-maestro_dev-db-data
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"
docker exec -it e-commerce_api /bin/sh
docker-compose -f docker-compose-deploy.yml down --volumes
docker-compose -f docker-compose-deploy.yml build
docker-compose -f docker-compose-deploy.yml up
docker-compose -f docker-compose-deploy.yml down
