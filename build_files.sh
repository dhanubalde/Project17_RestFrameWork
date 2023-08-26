pip install -r requirements.txt

python3.10.12 manage.py makemigrations --noinput
python3.10.12 manage.py migrate --noinput

python3.10.12 manage.py collectstatic --noinput
