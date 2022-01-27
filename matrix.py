matrix = [[1,2,0,1,0], [1,1,1,0,1], [2,2,0,1,0], [1,2,0,1,0], [0,1,0,2,0]]

def replace(matrix):
    for line in matrix:
        for index in range(0, len(line)):
            if line[index] == 1:
                line[index] = "A"
            elif line[index] == 2:
                line[index] = "B"
            elif line[index] == 0:
                line[index] = "Z"

replace(matrix)

print(matrix)
