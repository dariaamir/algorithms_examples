"""
 Fast algorithm to calculate fibonacci numbers
 Input: number of a fibonacci number
 Output: value of the required number
"""


def fib(number):
    fib_list = [0, 1]
    limit = number + 1

    for i in range(2, limit):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[number]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()