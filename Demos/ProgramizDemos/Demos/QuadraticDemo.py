'''
https://www.programiz.com/python-programming/examples/quadratic-roots

求解二次方跟

ax2+ bx + c = 0, where a, b and c are real numbers and a ≠ 0

'''


import cmath

a = 1
b = 5
c = 6

d = (b**2) - (4*a*c)

sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('The solution are {0} and {1}'.format(sol1, sol2))
