import re

pattern = ""
text = 


matches = re.finditer(pattern.text)
for match in matches:
    print(match.span())
    print(match.span()[0])
    print(text[match.span()[0]]),
match.span([1]])