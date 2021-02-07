#lambda : 함수 이름 없이, 함수처럼 쓸 수 있는 익명함수
def f(x, y):
    return x + y

print(f(1, 4))

f = lambda x, y: x + y
print(f(1, 4))

f = lambda x: x ** 2
print(f(3))

f = lambda x: x / 2
print(f(3))

print((lambda x: x + 1)(5))
