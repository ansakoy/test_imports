def print_blah():
    print('Printing blah from {}'.format(__name__))


print('Printing without main condition. Module name is {}'.format(__name__))
if __name__ == '__main__':
    print_blah()