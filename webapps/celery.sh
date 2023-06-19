pkill -f "celery worker"  
pkill celery
celery -A projeto beat -l info --logfile=celery.beat.log --detach 
celery -A projeto worker -l info --logfile=celery.log