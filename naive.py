def is_prime(x: int) -> bool:
    """This function takes an integer `x` as
    argument and checks whether is prime or not.

    Args:
        x (int): The integer number to test for primality.

    Returns:
        bool: True if the number `x` is prime, False otherwise.
    """
    if x in [0, 1]:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


if __name__ == "__main__":
    x = int(input())
    print(is_prime(x))
