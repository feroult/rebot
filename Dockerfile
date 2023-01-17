FROM python:3.11-slim

RUN pip install openai pygments prompt_toolkit

RUN mkdir /app
WORKDIR /app

COPY app/* .

CMD ["python", "rebot.py"]
