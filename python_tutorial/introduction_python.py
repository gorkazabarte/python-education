"""
An informal introduction to Python
"""

int1: int = 10
float1: float = 10.0
addition: float = int1 + float1
subtraction: float = int1 - float1
multiplication: float = int1 * float1
division: float = int1 / float1
floor_division: float = int1 // float1
module: float = int1 % float1
power: float = int1 ** float1

str1: str = 'paula moreno'
str2: str = "paula moreno"
str3: str = 'It\'s paula moreno'
str4: str = "It\'s paula moreno"
str5: str = "It's paula moreno"
str6: str = '"Yes", this is what she says'
str7: str = 'paula Moreno Moreno.\n I am learning Python programming.'
str8: str = r'This is a raw string and it will not scape characters with \n'

concatenation1: str = str1 + str2
concatenation2: str = 'paula' 'moreno'
replication: str = 2 * 'paula'
indexing_from_left: str = 'paula'[0]
indexing_from_right: str = 'paula'[-1]
slicing_from_left1: str = 'paula'[:3]
slicing_from_left2: str = 'paula'[1:3]
slicing_from_right1: str = 'paula'[1:]
slicing_from_right2: str = 'paula'[-3:-1]

try:
    str1[0] = 'g'
except TypeError as type_error:
    print(f'There is an error because strings are immutable {type_error}')

list1: list = [1, 4, 9, 16, 25]
indexing_list: list = list1[0]
slicing_list: list = list1[1:3]


def print_fibonucci(n: int) -> None:
    """ Print the numbers of Fibonucci series less than n """
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b


if __name__ == '__main__':
    print_fibonucci(20)

