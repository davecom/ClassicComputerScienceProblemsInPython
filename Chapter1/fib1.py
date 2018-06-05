def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)


if __name__ == "__main__":
    print(fib1(5))
