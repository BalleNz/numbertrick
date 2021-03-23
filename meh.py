import operator
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv,
    '%' : operator.mod,
}
while True:
    end = int(input())
    from itertools import *
    for j in permutations([*map(int, input().split())]):
        for ln in range(2, len(j)):
            for x in product('*-+%/', repeat = ln-1):
                nm = [j[i] for i in range(ln)]
                temp = nm[0];
                for q in range(ln//2 if not ln%2 else ln//2+1):
                    temp = ops[x[q]](temp, nm[q+1])
                if temp == end: print(j[:ln], x)
