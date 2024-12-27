lst = [1, 2, 3, 4, "a", "b"]
integers = []
strings = []
others = []

for element in lst:
    if isinstance(element, int):  
        integers.append(element)
    elif isinstance(element, str):  
        strings.append(element)
    else:  
        others.append(element)
print("Integers:", integers)
print("Strings:", strings)
print("Others:", others)
