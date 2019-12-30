"""
 Calculates Greatest Common Factor (using euclidean algorithm)
 Input: 2 numbers, separated by a space
 Output: GCF of these numbers
"""


def gcf(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcf(a % b, b)
    elif a <= b:
        return gcf(a, b % a)


def main():
    a, b = map(int, input().split())
    print(gcf(a, b))


if __name__ == "__main__":
    main()