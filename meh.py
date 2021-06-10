from random import randint
import operator
from itertools import *
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv,
}
def f(end):
    c_temp, c, k = 0, 0, (end+100)//2**(len(str(end))+2)
    while c < 100:
        for j in permutations([randint(1, 2*end) for _ in range(2, k)]):
            if c%5: c += 1; break
            if c_temp > 50: c_temp = 0;  break
            for x in product('*-+/', repeat = len(j)-1):
                nm = [j[i] for i in range(len(j))]; temp = nm[0]
                for q in range(len(j)-1): temp = ops[x[q]](temp, nm[q+1])
                if temp != end: c_temp += 1
                elif temp == end:
                    c += 1; print(*list(map(lambda x: ''.join(x), sum([[str(j[i]), x[i]] if i != len(x) else [str(j[i])] for i in range(len(j))], []))), sep = '')
f(int(input()))
