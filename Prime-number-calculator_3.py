import time
import sys

a = int(sys.argv[1])
t0 = time.time()

prime = [2]

for i in range(2, a):
    for p in prime:
        if i % p == 0:
            break
    else:
        prime.append(i)

print(prime)

t1 = time.time()

total = t1-t0
print(total)