def fibonacci(fib_list: list, n: int):

    a = fib_list[-1] + fib_list[-2]
    fib_list.append(a)

    if len(fib_list) < n:
        fibonacci(fib_list, n)


def main() -> None:
    fib_list = [0, 1]

    fibonacci(fib_list, 16)

    print(fib_list)

if __name__ == "__main__":
    main()