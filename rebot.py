import openai

import os
import readline
import pygments
from pygments.formatters import TerminalFormatter
from pygments.lexers import guess_lexer


EOT = '\x05'

# readline.parse_and_bind('tab: complete')
# readline.parse_and_bind('set editing-mode vi')

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
toggle_highlight = False

# Start the conversation
while True:
    prompt = input("# ")

    if prompt == "/clear":
        print("\nhistory cleared.\n")
        history = ""
        continue

    if prompt == "/hl":
        print(f"\nhighligh {'on' if toggle_highlight else 'off'}.\n")
        toggle_highlight = not toggle_highlight
        continue

    history += f"{prompt}\n"
    response = generate_response(prompt, history)

    lexer = guess_lexer(response)
    result = f"\n{pygments.highlight(response, lexer, formatter)}" if toggle_highlight else f"{response}\n"

    print(f"\n{result}")
    history += f"{response}\n"
