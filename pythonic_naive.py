def is_prime(x: int) -> bool:
    return False if x in {0, 1} else all(x % i != 0 for i in range(2, x))


if __name__ == "__main__":
    x = int(input())
    print(is_prime(x))
