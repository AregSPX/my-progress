from pathlib import Path
import json


X = Path('jjk.json')
if X.exists():
    C = X.read_text()
    n = json.loads(C)
    print(f"I know your favourite number! It's {n}.")
else:
    n = input("What's your favourite number?: ")
    try:
        n = int(n)
    except ValueError:
        print("Please type a number.")
    else:
        C = json.dumps(n)
        X.write_text(C)
        print("We will remember it the next time!")





