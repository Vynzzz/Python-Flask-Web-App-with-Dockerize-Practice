FROM python:3.14.0
LABEL maintainer='vynzraynes@gmail.com'

COPY . /WebApp
WORKDIR /WebApp

RUN pip install -r requirements.txt
EXPOSE 1234

CMD ["python3","-m","app.main"]
