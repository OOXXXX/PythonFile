from random import randint
from itertools import permutations

#列出4个数字和2个运算符可能组成的表达式形式
exps = ('((%s %s %s) %s %s) %s %s',
        '(%s %s %s) %s (%s %s %s)',
        '(%s %s (%s %s %s)) %s %s',
        '%s %s ((%s %s %s) %s %s)',
        '%s %s (%s %s (%s %s %s))')
ops = r'+-*/'

def test24(s):
    result = []
    
    #枚举4个数的所有可能顺序
    for a in permutations(s):
        #查找能实现24的表达式
        t = [exp % (a[0], op1, a[1], op2, a[2], op3, a[3]) for op1 in ops for op2 in ops for op3 in ops for exp in exps]
        if t:
            result.append(t)
    return result

for i in range(1):
    print('='*1)
    #生成随机数字
    lst = [randint(1, 5) for j in range(4)]
    r = test24(lst)
    if r:
        for j in range(len(r)):
            print(r[j])
    else:
        print('No answer', lst)
