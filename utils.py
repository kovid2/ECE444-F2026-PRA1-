def reversed(number: int) -> int:
    return int(str(number)[::-1])


def formatter(number: int):
    return bin(number), oct(number)