FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 1357

CMD [ "gunicorn", "-b", "0.0.0.0:1357", "app:app" ]