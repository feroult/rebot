FROM python:3.8-slim

RUN pip install openai

RUN mkdir /app
WORKDIR /app

COPY rebot.py .

CMD ["python", "rebot.py"]
