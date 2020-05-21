from datetime import datetime
from subprocess import call

from datetime import date

from apscheduler.schedulers.blocking import BlockingScheduler

from main import send_msg


sched = BlockingScheduler()

# The job will be executed on May 21-2020 Time(13:45)
sched.add_job(send_msg, 'date', run_date=datetime(2020, 5, 21,13,45,1))

sched.start()