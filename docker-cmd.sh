#!/bin/sh
# vim:sw=4:ts=4:et
set -e
cd webapps
if [ -z ${IS_WORKER+x} ]; then
  python manage.py migrate --noinput
  python manage.py collectstatic --noinput
  python manage.py shell -c "from django.contrib.auth.models import User; exit(User.objects.exists())" && \
  python manage.py createsuperuser --noinput
  python manage.py runserver 0.0.0.0:9001
  
else
  celery -A projeto beat -l info --logfile=celery.beat.log --detach && \
  celery -A projeto worker -l info --logfile=celery.log 
fi
