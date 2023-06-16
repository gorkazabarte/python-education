def allow_driver(age: int) -> bool:
    return True if age > 18 else False


def is_allowed_driver(age: int) -> bool:
    if 0 < age < 18:
        return False
    elif age < 0:
        return False
    else:
        return True


if __name__ == '__main__':
    allow_driver(23)
