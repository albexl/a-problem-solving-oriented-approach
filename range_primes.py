from sqrt import is_prime


def count_primes(l: int, r: int) -> int:
    """Counts the amount of prime numbers in a range.

    Args:
        l (int): Range start.
        r (int): Range end.

    Returns:
        int: The amount of prime numbers in the range `[L, R]`.
    """
    primes = 0
    for i in range(l, r + 1):
        if is_prime(i):
            primes += 1
    return primes


if __name__ == "__main__":
    l = int(input())
    r = int(input())
    print(count_primes(l, r))
