# map : Sequence 자료형의 각 element에 동일한 function을 적용
def f(x, y):
    return x + y
f(1, 4)

f = lambda x, y: x + y
f(1, 4)

ex = [1, 2, 3, 4, 5]
f = lambda x: x ** 2
print(list(map(f, ex)))

ex = [1, 2, 3, 4, 5]
f = lambda x, y: x + y
print(list(map(f, ex, ex)))

list(map(
    lambda x: x ** 2 if x % 2 == 0 else x,
    ex))

# python 3에는 list를 꼭 붙여줘야함
ex = [1, 2, 3, 4, 5]
print(list(map(lambda x: x + x, ex)))
print((map(lambda x: x + x, ex)))

f = lambda x: x ** 2
print(map(f, ex))
for i in map(f, ex):
    print(i)

result = map(f, ex)
print(result)
print(next(result))

import sys
sys.getsizeof(ex)
sys.getsizeof(map(lambda x: x + x, ex))
sys.getsizeof(list(map(lambda x: x + x, ex)))

# Reduce : map 과 달리 list에 똑같은 함수를 적용해서 통합
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
factorial(5)
