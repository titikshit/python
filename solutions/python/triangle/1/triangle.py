def equilateral(sides):
    a, b, c = sides
    return a > 0 and a == b == c


def isosceles(sides):
    a, b, c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return False
        
    if a + b <= c or b + c <= a or a + c <= b:
        return False

    return a == b or b == c or c == a


def scalene(sides):
    a, b, c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return False
        
    if a + b <= c or b + c <= a or a + c <= b:
        return False
        
    return a != b and b != c and c != a

