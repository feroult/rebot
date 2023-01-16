import openai

import os
import readline
import pygments
from pygments.formatters import TerminalFormatter
from pygments.lexers import guess_lexer


EOT = '\x05'

# readline.parse_and_bind('tab: complete')
# readline.parse_and_bind('set editing-mode vi')


def my_callback(key):
    print("hhhhaaa")
    if key == 'q':
        print('You pressed q!')
        exit()


readline.set_completer(my_callback)

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

    if prompt == "/r":
        print("\nchat restarted.\n")
        history = ""
        continue

    if prompt == "/hl":
        toggle_highlight = not toggle_highlight
        print(f"\nhighlight {'on' if toggle_highlight else 'off'}.\n")
        continue

    history += f"{prompt}\n"
    response = generate_response(prompt, history)

    lexer = guess_lexer(response)
    result = f"{pygments.highlight(response, lexer, formatter)}" if toggle_highlight else f"{response}"

    if len(result) == 0:
        print()
        continue

    if result[0] != '\n':
        print()
    print(f"\033[1;32m{result}\033[0m")
    if result[len(result)-1] != '\n':
        print()

    history += f"{response}\n"
