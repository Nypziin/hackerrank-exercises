import re

if __name__ == '__main__':
    n = input()
    frase = [input() for i in range(int(n))]

    for i in frase:
        try:
            re.compile(i)
            print('True')
        except:
            print('False')






