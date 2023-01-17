import pygments
from pygments.formatters import TerminalFormatter
from pygments.lexers import guess_lexer

formatter = TerminalFormatter()


def format(text, toggle_highlight):
    lexer = guess_lexer(text)
    result = f"{pygments.highlight(text, lexer, formatter)}" if toggle_highlight else text

    if len(result) == 0:
        return "\n"

    if result[0] != '\n':
        result = '\n' + result
    result = f"\033[1;32m{result}\033[0m"
    if result[len(result)-1] != '\n':
        result = result + '\n'

    return result
