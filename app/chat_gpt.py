import openai
import os

openai.api_key = os.environ.get('OPENAI_API_KEY')

history = ""


def generate_response(prompt, history):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt + history,
        max_tokens=2000,
        temperature=0.7
    )
    return response["choices"][0]["text"]
