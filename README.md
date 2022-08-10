# Fetch Electricity Data Using Django Rest Framework
Steps:
1. pip3 install requirements.txt
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py runserver


- Used a scheduler to fetch data on every 15 min which runs after 15 min of the server starting.(may fail in the first run)
Running function is in scheduler/scheduler.py
Scheduler is in scheduler/updater.py
Scheduler is configured in appconfig using ready method.

- Scheduler is used Independently.(Not as an Django App.)
- Pulls data and pushes to db perfectly.
- Used Class-Based API View 
- Pagination And filtering(search) added as viewed on documentation but not working. A little look from you may help.
Thank you
