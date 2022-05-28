def fibo(n: int) -> int:
    if n==0:return n
    ult: int = 0
    prox: int = 1
    for _ in range(1, n):
        ult, prox = prox, ult + prox
    return prox


def fib2(n: int, memo = {0:0, 1:1}) -> int:
    if n not in memo:
        memo[n] = fib2(n-1, memo) + fib2(n -2, memo)
    return memo[n]