print("This problem takes dimension(x,y,z) of cuboid returning the vertices whose sum is not equal to n")

x = int(input('x\t'))
y = int(input('y\t'))
z = int(input('z\t'))
n = int(input('n\t'))

print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if not (a+b+c) == n])

