"""
Task description:
Input: two integers n, m: 1≤ n ≤10^(18) и 2≤ m ≤10^(5)
Output: remainder of dividing the n-th Fibonacci number by m

Sample Input: 10 2
Sample Output: 1
"""


def fib_mod(n, m):
    current, previous = 1, 0
    i, period = 2, 0

    f_circle = [previous, current]

    while period == 0:
        current, previous = (current + previous) % m, current % m

        if current == 1 and previous == 0:
            period = i - 1
            del f_circle[-1]
            break
        f_circle.append(current)
        i += 1

    num = (n % period)
    return f_circle[num]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
