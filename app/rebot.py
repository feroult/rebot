from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings

bindings = KeyBindings()

@bindings.add('escape', 'x')
def _(event):
    event.current_buffer.validate_and_handle()

session = PromptSession()


if __name__ == '__main__':
    while True:
        answer = session.prompt('Give me some input: ', key_bindings=bindings, multiline=True)
        print('You said: %s' % answer)