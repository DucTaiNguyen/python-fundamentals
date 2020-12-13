import math
def find_side_by_cosine_rule(a,b,angleC):
    asquared = a**2
    bsquared = b**2
    two_abcosC = 2*a*b*math.cos(angleC)
    csquared =asquared + bsquared - two_abcosC
    result = math.sqrt(csquared)
    print("result is: ",result)
    return result
find_side_by_cosine_rule(6,7,math.pi/3)
find_side_by_cosine_rule(8,9,math.pi/4)
find_side_by_cosine_rule(4,6,math.pi/6)