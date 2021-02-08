
import time
import os

import schedule


def job():
    print("I'm working...")
    os.system("cd /home/work/workspace/projects/Automation/Automation")
    os.system("gunicorn wsgi:application --bind localhost:8000")
    os.system("x-www-browser http://127.0.0.1:8000/save_work")

schedule.every(20).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)