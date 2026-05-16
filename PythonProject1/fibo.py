# 斐波那契数列模块

def fib(n):
    """返回第n项斐波那契数"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

def fib2(n):
    """返回第n项斐波那契数"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result