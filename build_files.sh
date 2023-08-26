echo  "Building a Project"
python3.9 pip install -r requirements.txt

echo "make a database migration"
python3.9 manage.py makemigrations
python3.9 manage.py migrate

echo "collecting staticfiles"
python3.9 manage.py collectstatic
