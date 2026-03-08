"""
This code checks if two kangaroos reach the same position after several jumps
prints YES if True, NO if false

Inputs are x1 initial position of kangaroo 1
           v1 distance jumped by kangaroo 1
           x2 and v2 are the same for kangaroo 2
"""
def kangaroo(x1, v1, x2, v2):
    if  x1 < x2 and v1 > v2 or x1 > x2 and v1 < v2:
        if ((x1 - x2) % (v2 - v1) == 0):
            return "YES"
        else:
            return "NO"        
    else:
        return "NO"

print(kangaroo(0,3,4,2))