FROM python:3.8-slim

# Install the ChatGPT client
RUN pip install openai

# Create a working directory
RUN mkdir /app
WORKDIR /app

# Copy the chatgpt client script
COPY rebot.py .

# run the chatgpt client script
CMD ["python", "rebot.py"]
