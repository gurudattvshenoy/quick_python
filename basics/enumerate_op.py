# Enumerate operation

print("--------------------------------------")
s = "Learning python"
print("result of enumerate on string -{}".format(s))
print(list(enumerate(s)))
print("--------------------------------------")
l = ['a','b','c','d']
print("result od enumerate on list -{}".format(l))
print(list(enumerate(l)))
print("--------------------------------------")

s = {1,2,3,4}
print("result od enumerate on set -{}".format(s))
print(list(enumerate(s)))
print("--------------------------------------")


d = {'a':1,'b':3}
print("result od enumerate on dict -{}".format(d))
print(list(enumerate(d)))
print("--------------------------------------")

#Output 
#--------------------------------------
#result of enumerate on string -Learning python
#[(0, 'L'), (1, 'e'), (2, 'a'), (3, 'r'), (4, 'n'), (5, 'i'), (6, 'n'), (7, 'g'), (8, ' '), (9, 'p'), (10, 'y'), (11, 't'), (12, 'h'), (13, 'o'), (14, 'n')]
#--------------------------------------
#result od enumerate on list -['a', 'b', 'c', 'd']
#[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
#--------------------------------------
#result od enumerate on set -{1, 2, 3, 4}
#[(0, 1), (1, 2), (2, 3), (3, 4)]
#--------------------------------------
#result od enumerate on dict -{'a': 1, 'b': 3}
#[(0, 'a'), (1, 'b')]
#--------------------------------------
