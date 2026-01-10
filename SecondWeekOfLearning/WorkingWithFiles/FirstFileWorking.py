fl = open('exampleForTesting.txt')
for i in fl.readlines():
    print(i, end='')
fl.read()