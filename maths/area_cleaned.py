
from math import pi, sqrt


def surface_area_cube(side_length: float) -> float:
    
    if side_length < 0:
        raise ValueError("surface_area_cube() only accepts non-negative values")
    return 6 * side_length**2


def surface_area_sphere(radius: float) -> float:
    
    if radius < 0:
        raise ValueError("surface_area_sphere() only accepts non-negative values")
    return 4 * pi * radius**2


def surface_area_hemisphere(radius: float) -> float:
    
    if radius < 0:
        raise ValueError("surface_area_hemisphere() only accepts non-negative values")
    return 3 * pi * radius**2


def surface_area_cone(radius: float, height: float) -> float:
    
    if radius < 0 or height < 0:
        raise ValueError("surface_area_cone() only accepts non-negative values")
    return pi * radius * (radius + (height**2 + radius**2) ** 0.5)


def surface_area_cylinder(radius: float, height: float) -> float:
    
    if radius < 0 or height < 0:
        raise ValueError("surface_area_cylinder() only accepts non-negative values")
    return 2 * pi * radius * (height + radius)


def area_rectangle(length: float, width: float) -> float:
    
    if length < 0 or width < 0:
        raise ValueError("area_rectangle() only accepts non-negative values")
    return length * width


def area_square(side_length: float) -> float:
    
    if side_length < 0:
        raise ValueError("area_square() only accepts non-negative values")
    return side_length**2


def area_triangle(base: float, height: float) -> float:
    
    if base < 0 or height < 0:
        raise ValueError("area_triangle() only accepts non-negative values")
    return (base * height) / 2


def area_triangle_three_sides(side1: float, side2: float, side3: float) -> float:
    
    if side1 < 0 or side2 < 0 or side3 < 0:
        raise ValueError("area_triangle_three_sides() only accepts non-negative values")
    elif side1 + side2 < side3 or side1 + side3 < side2 or side2 + side3 < side1:
        raise ValueError("Given three sides do not form a triangle")
    semi_perimeter = (side1 + side2 + side3) / 2
    area = sqrt(
        semi_perimeter
        * (semi_perimeter - side1)
        * (semi_perimeter - side2)
        * (semi_perimeter - side3)
    )
    return area


def area_parallelogram(base: float, height: float) -> float:
    
    if base < 0 or height < 0:
        raise ValueError("area_parallelogram() only accepts non-negative values")
    return base * height


def area_trapezium(base1: float, base2: float, height: float) -> float:
    
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("area_trapezium() only accepts non-negative values")
    return 1 / 2 * (base1 + base2) * height


def area_circle(radius: float) -> float:
    
    if radius < 0:
        raise ValueError("area_circle() only accepts non-negative values")
    return pi * radius**2


def area_ellipse(radius_x: float, radius_y: float) -> float:
    
    if radius_x < 0 or radius_y < 0:
        raise ValueError("area_ellipse() only accepts non-negative values")
    return pi * radius_x * radius_y


def area_rhombus(diagonal_1: float, diagonal_2: float) -> float:
    
    if diagonal_1 < 0 or diagonal_2 < 0:
        raise ValueError("area_rhombus() only accepts non-negative values")
    return 1 / 2 * diagonal_1 * diagonal_2


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  

    print("[DEMO] Areas of various geometric shapes: \n")
    print(f"Rectangle: {area_rectangle(10, 20) = }")
    print(f"Square: {area_square(10) = }")
    print(f"Triangle: {area_triangle(10, 10) = }")
    print(f"Triangle: {area_triangle_three_sides(5, 12, 13) = }")
    print(f"Parallelogram: {area_parallelogram(10, 20) = }")
    print(f"Rhombus: {area_rhombus(10, 20) = }")
    print(f"Trapezium: {area_trapezium(10, 20, 30) = }")
    print(f"Circle: {area_circle(20) = }")
    print("\nSurface Areas of various geometric shapes: \n")
    print(f"Cube: {surface_area_cube(20) = }")
    print(f"Sphere: {surface_area_sphere(20) = }")
    print(f"Hemisphere: {surface_area_hemisphere(20) = }")
    print(f"Cone: {surface_area_cone(10, 20) = }")
    print(f"Cylinder: {surface_area_cylinder(10, 20) = }")
