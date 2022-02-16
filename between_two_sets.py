def getTotalX(a, b):

    lst = []

    for x in range(min(a), max(b) + 1):
        if all(y%x == 0 for y in b):
            lst.append(x)
    
    lst2 = []
    
    for x in lst:
        if all(x%y == 0 for y in a):
            lst2.append(x)

    return len(lst2)


getTotalX([2, 4], [16, 32, 96])