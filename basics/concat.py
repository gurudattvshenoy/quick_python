# Concatenation operation

l = [1,2,3] + [4,5,6]
print(l)
# Concat + oper. is Not supported => list + tuple
#lt =  [1,2,3] + (4,5,6)
#TypeError: can only concatenate list (not "tuple") to list

#print('abc'+['d','e','f'])
#TypeError: can only concatenate str (not "list") to str
print(list('abc')+['d','e','f'])

# Output
#[1, 2, 3, 4, 5, 6]
#['a', 'b', 'c', 'd', 'e', 'f']
