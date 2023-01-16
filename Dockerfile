FROM python:3.11-alpine

RUN apk add kbd

RUN pip install openai pygments keyboard

RUN mkdir /app
WORKDIR /app

COPY app/* .

CMD ["python", "rebot.py"]
