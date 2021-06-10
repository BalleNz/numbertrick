from random import randint
import operator
from itertools import *
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv,
    '%' : operator.mod,
}
def f(end):
    c_temp, c, k = 0, 0, (end+100)//2**(len(str(end))+3)
    if k in [0, 1, 2]: k = 4
    while c < 100:
        for j in permutations([randint(1, 2*end) for _ in range(k)]):
            if c%2: c += 1; break
            if c_temp > 50: c_temp = 0;  break
            for x in product('*-+/%', repeat = len(j)-1):
                if c%2: break
                nm = [j[i] for i in range(len(j))]; temp = nm[0]
                for q in range(len(j)-1): temp = ops[x[q]](temp, nm[q+1])
                if temp != end: c_temp += 1
                elif temp == end:
                    c += 1; print('('*(len(j)-1), f'{str(j[0])} ', *list(map(lambda x: ''.join(x), sum([[f'{x[i].replace("/", "//")} {str(j[i+1])})'] if not i%2 else [f' {x[i].replace("/", "//")} {str(j[i+1])}) '] for i in range(len(j)-1)], []))), sep = '')
f(int(input()))
