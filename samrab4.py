def is_prime(n):
    """
    Проверяет, является ли число n простым.

    Args:
        n: Целое число.

    Returns:
        True, если n простое, иначе False.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    """
    Находит следующее простое число после n.
    Если n не является простым числом, возвращает 0.

    Args:
        n: Целое число.

    Returns:
        Следующее простое число после n, если n - простое, иначе 0.
    """
    if not is_prime(n):
        return 0

    next_num = n + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1


