import sys


def fib(n, k):
    if n <= 2:
        return 1
    fn_1 = 1
    fn_2 = 1
    fn = 0
    for _ in range(3, n + 1, 1):
        fn = fn_1 + k * fn_2
        fn_2, fn_1 = fn_1, fn
    return fn


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("python rabbit_fib.py n k")
        print("\tn = number of months")
        print("\tk = number of rabbit pairs")
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    result = fib(n, k)
    print(result)
    with open("output.txt", "w") as output_file:
        output_file.write(result)
