from django.contrib import admin
from django_celery_beat.models import ClockedSchedule, CrontabSchedule, IntervalSchedule,PeriodicTask, PeriodicTasks, SolarSchedule
admin.site.unregister(IntervalSchedule)
admin.site.unregister(CrontabSchedule)
admin.site.unregister(SolarSchedule)
admin.site.unregister(ClockedSchedule)
admin.site.unregister(PeriodicTask)