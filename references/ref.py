a = 1
b = 2
c = b

print( id(1) == id(a) )
print( id(2) == id(b) )
print( id(c) == id(b) )
print( id(2) == id(c) )

c = 4
print( id(c) == id(b) )
print( id(c) == id(b) )

d = [1,2,3]

e = d

e[0] = 1111
print(d)

f = [1111, 2, 3]

print( id(f) == id(e) )

g = [1]
h = [1]

print( id(g) == id(h) )


