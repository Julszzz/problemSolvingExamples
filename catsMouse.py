"""
This function finds the closes position to the desired point
Using a Cat A and a Cat B, find which one catches the Mouse C
and print the result

The function arguments are catsMouse(CatA, CatB, MouseC)
"""
def catsMouse(x,  y, z):
    distanceA = abs(z - x)
    distanceB = abs(z - y)

    if distanceA == distanceB:
        return "Mouse C"
    elif distanceA < distanceB:
        return "Cat A"
    else:
        return "Cat B"
    
R = catsMouse(2, 6, 4)
print(R)