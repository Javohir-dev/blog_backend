echo " BUILD START"
python -m pip install pipenv
python -m pipenv install -r requirements.txt
python manage.py collectstatic --noinput --clear
python manage.py migrate
echo " BUILD END"