"""
input for input variable
print for output variable

today's talking about float point num
>>> x = 5
>>> x
5
>>> x = 6 / 2
>>> x
3.0
floating point number == decimal number
floating point number can generated through divisions
or
through predefined variable
>>> y = 5.2
>>> y
5.2

How to convert input string or float into integer
>>> y = 5.0
>>> int(y)
5
"""

"""
import techniques

import module
or
from module import function

% - reminder for python division
>>> x = 5 % 2
>>> x
1
"""

#application for asking what day today
#what the day is three days after Saturday

x = (6 + 3) % 7
print(x)

"""
formula = (today's day + how many days after today) % 7
"""

"""
python REPL environment
R- Read
E- Eval
P- Print
L- Loop

REPL environment can be used for solve bug in real-time when IT environment is simple

help(obj) solve issues
>>> dir() - show the module available in the current environment
>>> import math - import math module
>>> help(math) - find functions under math module with help function
>>> cls - clear everything within the module

how to import cmd in python
>>> import os - import operating system module
>>> dir(os)
functions within os module
>>> help(os.system) - exec system method within os module
>>> os.system("cls")
0
"""
"""
python is good for data science and data analysis
"""

"""
apply python to convert different from one base to another

common base in computational mathematics
bin- binary
oct- octal
dec- decimal
hex- hexadecimal
"""

"""
type of base functions:
int - integer
bin - binary
hex - hexadecimal
oct - octal

int/bin/hex/oct(p1, p2)
p1 = integer representation
p2 = type of number(e.g. int, float)
"""

"""
decimal: 1, 2, 3, 4, 5, 6 ... 16
hex: 1, 2, 3, 4, 5, 6 ... 9, A, B, C, D, E ... F
binary: 2; 2 ** n; n == decimal

hex prefix: 0x
e.g.
0xb - 11 in hex
"b" - 11

oct prefix: 0o
bin prefix: 0b
"""

"""
conversion between bases
"""

"""
print's argument
sep- separate
end- end

print parameter (optional):
file: a file like object
sep: string inserted between values
end: string appended after the last value
flush: whether to forcibly flush the stream
"""