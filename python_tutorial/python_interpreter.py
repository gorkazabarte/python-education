"""
Execute the following Python module as follows:
>>> python3 python_tutorial/python_interpreter.py gorka zabarte moreno 23
Arguments passing: ['python_tutorial/python_interpreter.py', 'gorka', 'zabarte', 'moreno', '23']
"""


from sys import argv

print(f'Arguments passing: {argv}. Length: {len(argv)}')

