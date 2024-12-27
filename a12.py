lst = [1, 2, 3, 4, 5]

odd = [x for x in lst if x % 2 != 0] 
even = [x for x in lst if x % 2 == 0]  

print("Odd elements:", odd)
print("Even elements:", even)
