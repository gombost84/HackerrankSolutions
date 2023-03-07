def divisibleSumPairs(n, k, ar):
    i = 0
    
    for x in range(0, len(ar)):
        for y in range(x + 1, len(ar)):
            if (ar[x] + ar[y]) % k == 0:
                i += 1
                
    return i


print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))