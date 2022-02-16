if __name__ == '__main__':
    N = 12
    lst = []
    commands = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 'print', 'pop', 'reverse', 'print']

    for x in commands:
        cmd = 'lst' + '.' + str(x.split()[0]) + '(' + str(x.split()[1]) + ', ' + str(x.split()[2]) + ')'
        exec(cmd)
        print(lst)