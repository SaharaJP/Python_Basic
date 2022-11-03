import os

zen = os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt'))
a = open(zen, 'r')
print(a.read())
