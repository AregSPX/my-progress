from pathlib import Path

z = Path('exceptt.txt')
result = ''

while True:
    n1 = input("Type the first number (type q to quit): ")
    if n1 == 'q':
            break
    try:
        n1 = int(n1)
       
    except ValueError:
        print("Please type numbers only.")
        continue    
    
    n2 = input("Type the second number (type q to quit): ")
    if n2 == 'q':
            break
    try:
        n2 = int(n2)  
    except ValueError:
        print("Please type numbers only.")    
        continue
        
    result += f'\n{n1}, {n2}' 
       
z.write_text(result)
