import openai

import os
import readline
import pygments
from pygments.formatters import TerminalFormatter
from pygments.lexers import guess_lexer

EOT = '\x05'

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')

openai.api_key = os.environ.get('OPENAI_API_KEY')

formatter = TerminalFormatter()


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

    lexer = guess_lexer(response)
    highlighted = pygments.highlight(response, lexer, formatter)
    # highlighted = highlight(response, PythonLexer(), TerminalFormatter())

    print(f"\n{highlighted}")
    history += f"{response}\n"
