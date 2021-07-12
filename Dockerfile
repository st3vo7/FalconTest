FROM python:3.7
COPY code/requirements.txt code/requirements.txt
RUN pip3 install -r code/requirements.txt
COPY code/ .
CMD gunicorn --bind :5000 --log-level debug  "smallapp.api:create_api()"