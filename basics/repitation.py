# Repitation operation
from decimal import Decimal
c = [Decimal('100.20')]*2
print("id(c[0] = {} , id(c[1]) = {}".format(id(c[0]),id(c[1])))
print(c[1] is c[0])

f = [1,2]*3
print(f)

s = 'abc'*3
print(s)

#Output
#id(c[0] = 140409218452032 , id(c[1]) = 140409218452032
#True
#[1, 2, 1, 2, 1, 2]
#abcabcabc
