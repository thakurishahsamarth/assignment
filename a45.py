n = 7
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
if is_prime and n > 1:
    print("Prime")
else:
    print("Not Prime")