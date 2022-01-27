def countApplesAndOranges(s, t, a, b, apples, oranges):
        
    print(len([x for x in apples if a + x >= s and a + x <= t]))
    print(len([x for x in oranges if b + x >= s and b + x <= t]))