FROM python:3.7
ADD . usr/src/app/
RUN pip install -r requirements.txt

FROM python:3.7
COPY  usr/src/app/
ENV PORT 8080
CMD ["python-quiz-app"]
