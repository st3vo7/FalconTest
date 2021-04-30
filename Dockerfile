FROM python:3.7

# Add your code here


CMD gunicorn --bind :5000 --log-level debug  "smallapp.api:create_api()"