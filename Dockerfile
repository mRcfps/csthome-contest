FROM python:3.6-alpine

# Install dependencies
COPY requirements.txt /
RUN pip install -r requirements.txt

# Add src and collect static files
COPY . /
RUN python manage.py collectstatic

CMD [ "gunicorn", "contest.wsgi", "-b", "0.0.0.0:8000" ]
