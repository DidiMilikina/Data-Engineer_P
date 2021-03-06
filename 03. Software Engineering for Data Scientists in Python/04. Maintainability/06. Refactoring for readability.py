'''
Refactoring for readability
Refactoring longer functions into smaller units can help with both readability and modularity. In this exercise, you will refactor a function into smaller units. The function you will be refactoring is shown below. Note, in the exercise, you won't be using docstrings for the sake of space; in a real application, you should include documentation!

def polygon_area(n_sides, side_len):
    """Find the area of a regular polygon

    :param n_sides: number of sides
    :param side_len: length of polygon sides
    :return: area of polygon

    >>> round(polygon_area(4, 5))
    25
    """
    perimeter = n_sides * side_len

    apothem_denominator = 2 * math.tan(math.pi / n_sides)
    apothem = side_len / apothem_denominator

    return perimeter * apothem / 2
Instructions
100 XP
Move the logic for calculating the perimeter into the polygon_perimeter function.
Complete the definition of the polygon_apothem function, by moving the logic seen in the context. The math module has already been imported for you.
Utilize the new unit functions to complete the definition of polygon_area.
Use the more unitized polygon_area to calculate the area of a regular hexagon with legs of size 10.
'''
SOLUTION

def polygon_perimeter(n_sides, side_len):
    return n_sides * side_len

def polygon_apothem(n_sides, side_len):
    denominator = 2 * math.tan(math.pi / n_sides)
    return side_len / denominator

def polygon_area(n_sides, side_len):
    perimeter = polygon_perimeter(n_sides, side_len)
    apothem = polygon_apothem(n_sides, side_len)

    return perimeter * apothem / 2

# Print the area of a hexagon with legs of size 10
print(polygon_area(n_sides=6, side_len=10))