biomoleculas = ('proteina', 'ácidos nucleicos', 'carboidrato', 'lipídeo', 'ácidos nucleicos', 'carboidrato', 'carboidrato', 'carboidrato')

print(biomoleculas)

print()

print(set(biomoleculas))

print()

c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection(c2)

print(c3)

print()

print(c1.difference(c2))

print()

print(c2.difference(c1))