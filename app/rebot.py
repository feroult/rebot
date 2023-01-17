import chat_gpt
import console
import formatter


history = ""
toggle_highlight = False
toggle_multiline = False

while True:
    prompt = console.prompt("# ", toggle_multiline)

    if prompt == "/r":
        print("\nchat restarted.\n")
        history = ""
    elif prompt == "/hl":
        toggle_highlight = not toggle_highlight
        print(f"\nhighlight {'on' if toggle_highlight else 'off'}.\n")
    elif prompt == "/ml":
        toggle_multiline = not toggle_multiline
        print(f"\nmultiline {'on' if toggle_multiline else 'off'}.\n")
    else:
        response = chat_gpt.generate_response(prompt, history)
        print(formatter.format(response, toggle_highlight))
        history += f"{prompt}\n{response}\n"
