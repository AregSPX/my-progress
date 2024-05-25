from pathlib import Path

x = Path('learning_python.txt')
contents = x.read_text()
contents = contents.replace('python', 'C#')
print(contents)
lines = contents.splitlines()
string = ''
for line in lines:
    string += line
print(string)

contents0 = ''
y = Path('guest.txt')
while True:
    name = input("What's your name?: ")
    if name != 'q':
        contents0 += f"\n{name}"
    if name == 'q':
        break
y.write_text(contents0)

