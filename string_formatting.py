def print_formatted(number):
    # your code goes here    
    bin_length = len(str(bin(number))[2:])
    
    for x in range(1, number + 1):
        print(f'{x:{bin_length}d} {x:{bin_length}o} {x:{bin_length}X} {x:{bin_length}b}')
    

if __name__ == '__main__':
    print_formatted(17)