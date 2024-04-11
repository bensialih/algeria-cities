
sleep 5;

# run migrations
python3 manage.py migrate;

# seed all cities into database
python3 manage.py load_cities;

# create test admin user
export DJANGO_SUPERUSER_PASSWORD=testpass;
python3 manage.py createsuperuser \
	--noinput \
	--username abdel \
	--email "foo@bar.com";

# create static files for geo
python3 /app/manage.py collectstatic --noinput;

# run server
python3 /app/manage.py runserver 0.0.0.0:8000;
