from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings

bindings = KeyBindings()


@bindings.add('escape', 'x')
def _(event):
    event.current_buffer.validate_and_handle()


session = PromptSession()


def prompt(prefix):
    answer = session.prompt(prefix,
                            key_bindings=bindings, multiline=True)
    return answer
