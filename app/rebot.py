import chat_gpt
import console
import formatter


history = ""
toggle_highlight = False

# Start the conversation
while True:
    prompt = console.prompt("# ")

    if prompt == "/r":
        print("\nchat restarted.\n")
        history = ""
    elif prompt == "/hl":
        toggle_highlight = not toggle_highlight
        print(f"\nhighlight {'on' if toggle_highlight else 'off'}.\n")
    else:
        response = chat_gpt.generate_response(prompt, history)
        print(formatter.format(response, toggle_highlight))
        history += f"{prompt}\n{response}\n"
