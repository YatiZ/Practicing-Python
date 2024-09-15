

import pyperclip
import re

with open('book/chapter-7/sample.txt', 'r') as file:
    text_to_copy =file.read()

# text_to_copy = "Hello world 454-322-1243 and 092-392-0212 and his email is zuzu62113@gmail.com"
pyperclip.copy(text_to_copy)

# create regex for ph no
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

# regex for email
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)


# find matches in clipboard text
text = str(pyperclip.paste())
print(text)

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x'+groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

print(matches)

# copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone and emaill found')
