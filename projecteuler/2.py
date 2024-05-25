fib_seq = [1,2]
N = 0

while True:
    n = fib_seq[-1] + fib_seq[-2]
    fib_seq.append(n)
    if n >= 4000000:
        del fib_seq[-1]
        break

for n in fib_seq:
    if n % 2 == 0:
        N += n

print(N)
print(fib_seq)