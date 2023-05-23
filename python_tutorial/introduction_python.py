"""
An informal introduction to Python
"""

int1: int = 10
float1: float = 10.0
addition: float = int1 + float1
substraction: float = int1 - float1
multiplication: float = int1 * float1
division: float = int1 / float1
floor_division: float = int1 // float1
module: float = int1 % float1
power: float = int1 ** float1

str1: str = 'Gorka Zabarte Moreno'
str2: str = "Gorka Zabarte Moreno"
str3: str = 'It\'s Gorka Zabarte Moreno'
str4: str = "It\'s Gorka Zabarte Moreno"
str5: str = "It's Gorka Zabarte Moreno"
str6: str = '"Yes", this is what she says'
str7: str = 'Gorka Zabarte Moreno.\n I am learning Python programming.'
str8: str = r'This is a raw string and it will not scape characters with \n'

concatenation1: str = str1 + str2
concatenation2: str = 'gorka' 'zabarte'
replication: str = 2 * 'gorka'
indexing_from_left: str = 'gorka'[0]
indexing_from_right: str = 'gorka'[-1]
slicing_from_left1: str = 'gorka'[:3]
slicing_from_left2: str = 'gorka'[1:3]
slicing_from_right1: str = 'gorka'[1:]
slicing_from_right2: str = 'gorka'[-3:-1]

try:
    str1[0] = 'g'
except TypeError as type_error:
    print(f'There is an error because strings are immutable {type_error}')

list1: list = [1, 4, 9, 16, 25]
indexing_list: list = list1[0]
slicing_list: list = list1[1:3]
