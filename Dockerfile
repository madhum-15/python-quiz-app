FROM python:3.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        sqlite3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY manage.py /usr/src/app/
COPY static /usr/src/app/static
COPY db.sqlite3 /usr/src/app/
COPY templates /usr/src/app/templates
COPY student /usr/src/app/student
COPY quiz /usr/src/app/quiz
COPY teacher /usr/src/app/teacher
COPY onlinequiz /usr/src/app/onlinequiz

EXPOSE 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]

