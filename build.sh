set -o errexit
pip install -r reqirements.txt
python3 manage.py collectstatic --no-input
python3 manage.py migrate
python3 mange.py superuser