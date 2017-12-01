def LHS(a,b):
    c = (a-b) * (a-b)
    return c

def RHS(a,b):
    c = (a*a) - (2 *a * b) + (b*b)
    return c

num_a = int(input("Enter a number: "))
num_b = int(input("Enter another number"))

lhs = LHS(num_a, num_b)
rhs = RHS(num_a, num_b)

if lhs == rhs:
    print ("LHS equals RHS proved")




