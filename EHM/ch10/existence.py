from pathlib import Path

a = Path('cat.txt')
b = Path('dog.txt')

try:
    ccat = a.read_text()
except FileNotFoundError:
    pass
else:
    print(ccat)
try:
    cdog = b.read_text()
except FileNotFoundError:
    print(f"The file {b} doesnt exist")
else:
    print(cdog)