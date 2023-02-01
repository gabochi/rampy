import sys

def crear(expr):
    lenght = 1 << 13
    out = []

    for t in range(lenght):
        sample = eval(expr)&255
        out.append(sample)
        
        if t%128 == 0: print()

        if sample<127:
            print('.',end='')
        else:
            print('#',end='')

    with open('test.raw','wb') as file:
        file.write(bytes(out))
