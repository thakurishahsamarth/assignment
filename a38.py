total = 0
for n in range(3, 100):
    if n % 3 == 0 or n % 5 == 0:
        total += n
print(total)