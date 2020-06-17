#! python3
# bullet-point-adder.py - Marking the lists from Wiki
import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)
