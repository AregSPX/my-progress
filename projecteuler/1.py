req_n = []

for n in range (1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        req_n.append(n)

N = 0
for n in req_n:
    N += n

print(N)