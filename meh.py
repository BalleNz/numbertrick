import operator
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv,
    '%' : operator.mod,
}
end = int(input())
from itertools import *
for j in permutations([*map(int, input().split())]):
    for x in product('*-+%/', repeat = len(j)-1):
        nm = [j[i] for i in range(len(j))]
        temp = nm[0];
        for q in range(len(j)//2 if not len(j)%2 else len(j)//2+1):
            temp = ops[x[q]](temp, nm[q+1])
        if temp == end: print(j, x)
