import openai
import sys

# set the API key
openai.api_key = "YOUR_API_KEY"

def generate_response(prompt):
    # make the API request
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        stop=None,
    )
    # return the generated response
    return response["choices"][0]["text"]

while True:
    # get the question from the command line
    prompt = input("What is your question? (Enter 'q' to quit) ")

    if prompt.strip().lower() == 'q':
        break

    # generate the response
    response = generate_response(prompt)
    print(response)
