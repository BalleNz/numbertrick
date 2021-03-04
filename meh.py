git remote add origin
import operator
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv,
    '%' : operator.mod,
}
from itertools import *
for j in permutations([15, 7, 49, 69, 49]):
    for x in product('*/-+', repeat = len(j)-1):
        a,b,c,d,e = j
        if (ops[x[3]](ops[x[2]](ops[x[1]](ops[x[0]](a, b), c), d), e)) == 28: print(j, x)
