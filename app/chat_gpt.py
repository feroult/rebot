import openai
import os

openai.api_key = os.environ.get('OPENAI_API_KEY')

history = ""

models = ['text-davinci-003', 'code-davinci-002']

model_index = 0


def generate_response(prompt, history):
    global model_index
    response = openai.Completion.create(
        engine=models[model_index],
        prompt=prompt + history,
        max_tokens=2000,
        temperature=0.7
    )
    return response["choices"][0]["text"]


def switch_model():
    global model_index
    model_index = model_index + 1
    if model_index == len(models):
        model_index = 0
    return models[model_index]
