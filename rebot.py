import openai
import os

EOT = '\x05'

openai.api_key = os.environ.get('OPENAI_API_KEY')

def generate_response(prompt, history):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt + history,
        max_tokens=2000,
        temperature=0.7
    )
    return response["choices"][0]["text"]

# Initialize the conversation history
history = ""

# Start the conversation
while True:
    prompt = input("# ")    
    if prompt == EOT:
        print("\nhistory cleared.\n")
        history = ""
        continue

    history += f"{prompt}\n"
    response = generate_response(prompt, history)
    print(f"{response}\n")
    history += f"{response}\n"
