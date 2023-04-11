def is_prime(x: int) -> bool:
    if x in [0, 1]:
        return False
    i = 2
    while i**2 <= x:
        if x % i == 0:
            return False
        i += 1
    return True


if __name__ == "__main__":
    x = int(input())
    print(is_prime(x))
