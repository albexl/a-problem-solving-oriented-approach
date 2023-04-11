from sqrt import is_prime


def count_primes(l: int, r: int) -> int:
    return sum(bool(is_prime(i)) for i in range(l, r + 1))


if __name__ == "__main__":
    l = int(input())
    r = int(input())
    print(count_primes(l, r))
