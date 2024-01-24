FROM python:3.11
LABEL authors="hp77"


# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install flower

COPY . /code/
EXPOSE 8000 5555
# Command to run both Flask and Celery
#CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "main:app", "--preload", "&&", "celery", "-A", "task", "worker", "--loglevel=info"]

RUN chmod +x ./docker_helpers/server-entrypoint.sh
RUN chmod +x ./docker_helpers/worker-entrypoint.sh
