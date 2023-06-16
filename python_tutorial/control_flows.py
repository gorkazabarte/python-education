from typing import Any


def allow_driver(age: int) -> bool:
    return True if age > 18 else False


def is_allowed_driver(age: int) -> bool:
    if 0 < age < 18:
        return False
    elif age < 0:
        return False
    else:
        return True


def multiply_by_2(numbers: list[int, ...]) -> list[int, ...]:
    return [num * 2 for num in numbers]


def multiply_by_3(numbers: list[int, ...]) -> list[int, ...]:
    res: list[int, ...] = []
    for num in numbers:
        res.append(num * 3)
    return res


def is_present(lista: list[Any, ...], e: Any) -> bool:
    return any([element for element in lista if e == element])


def is_present(lista: list[Any, ...], e: Any) -> bool:
    for element in lista:
        if e == element:
            return True
        break
    return False


if __name__ == '__main__':
    print(allow_driver(23))
    print(multiply_by_2([1, 2, 3, 4, 5]))
    print(multiply_by_3([1, 2, 3, 4, 5]))
    print(is_present([1, 2, 3, 4, 5], 5))
