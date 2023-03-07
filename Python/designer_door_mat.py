
def doorMat(height, width):    

    a = int((int(height) - 1) / 2)

    x = 1
    b = int((int(width) - 3 * x) / 2)

    c = (int(width) - 7) * '-' + 'WELCOME' + (int(width) - 7) * '-'


    for i in range(a):
        for j in range(b):
            print((b - x * 3) * '-' + x * ".|." + (b - x * 3) * '-')
            x = x + 2

    print(c)

    for i in range(a):
        for j in range(b):
            print((b - x * 3) * '-' + x * ".|." + (b - x * 3) * '-')
            x = x - 2

height, width = input().split()

doorMat(height, width)