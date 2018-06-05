from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}  # our old base cases


def fib3(n: int) -> int:
    if n in memo:  # our new base cases
        return memo[n]
    else:
        memo[n] = fib3(n - 1) + fib3(n - 2)  # memoization
    return memo[n]


if __name__ == "__main__":
    print(fib3(5))
    print(fib3(50))