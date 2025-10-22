def fib_with_range(start, stop):
    prev2 = 0
    prev1 = 1
    outputs = []
    outputs.append(prev2)
    outputs.append(prev1)
    for fibo in range(start, stop):
        current = prev1 + prev2
        outputs.append(current)
        prev2 = prev1
        prev1 = current
    return outputs


def main():
    a = fib_with_range(2, 10)
    b = fib_with_range(0, 10)

    print("Using range(2, 10):")
    print(a)
    print("Count:", len(a))
    print()
    print("Using range(10):")
    print(b)
    print("Count:", len(b))


if __name__ == '__main__':
    main()
