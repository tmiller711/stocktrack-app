FROM python:3.8-slim

WORKDIR /app
RUN apt-get update && apt-get install -y ufw nginx sudo python3 pip certbot

# install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# setup environment variables
ENV DJANGO_SETTINGS_MODULE='stocktrackapp.settings.prod'
ARG DJANGO_SECRET_KEY

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# setup static files
RUN python3 manage.py collectstatic --no-input

# install gunicorn
RUN pip install gunicorn

# configure nginx
RUN ufw allow 'Nginx HTTP'
RUN ufw allow http
RUN ufw allow https
COPY conf/nginx /etc/nginx/sites-enabled/
RUN rm /etc/nginx/sites-enabled/default

# setup ssl
# COPY conf/certbot /app/certbot

EXPOSE 80 443

CMD nginx && gunicorn stocktrackapp.wsgi -w 4 -b 0.0.0.0:8000