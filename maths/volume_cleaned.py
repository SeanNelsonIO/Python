
from __future__ import annotations

from math import pi, pow


def vol_cube(side_length: int | float) -> float:
    
    return pow(side_length, 3)


def vol_spherical_cap(height: float, radius: float) -> float:
    
    return 1 / 3 * pi * pow(height, 2) * (3 * radius - height)


def vol_spheres_intersect(
    radius_1: float, radius_2: float, centers_distance: float
) -> float:
    
    if centers_distance == 0:
        return vol_sphere(min(radius_1, radius_2))

    h1 = (
        (radius_1 - radius_2 + centers_distance)
        * (radius_1 + radius_2 - centers_distance)
        / (2 * centers_distance)
    )
    h2 = (
        (radius_2 - radius_1 + centers_distance)
        * (radius_2 + radius_1 - centers_distance)
        / (2 * centers_distance)
    )

    return vol_spherical_cap(h1, radius_2) + vol_spherical_cap(h2, radius_1)


def vol_cuboid(width: float, height: float, length: float) -> float:
    
    return float(width * height * length)


def vol_cone(area_of_base: float, height: float) -> float:
    
    return area_of_base * height / 3.0


def vol_right_circ_cone(radius: float, height: float) -> float:
    
    return pi * pow(radius, 2) * height / 3.0


def vol_prism(area_of_base: float, height: float) -> float:
    
    return float(area_of_base * height)


def vol_pyramid(area_of_base: float, height: float) -> float:
    
    return area_of_base * height / 3.0


def vol_sphere(radius: float) -> float:
    
    return 4 / 3 * pi * pow(radius, 3)


def vol_hemisphere(radius: float):
    
    return 2 / 3 * pi * pow(radius, 3)


def vol_circular_cylinder(radius: float, height: float) -> float:
    
    return pi * pow(radius, 2) * height


def vol_conical_frustum(height: float, radius_1: float, radius_2: float):
    
    return (
        1
        / 3
        * pi
        * height
        * (pow(radius_1, 2) + pow(radius_2, 2) + radius_1 * radius_2)
    )


def main():
    
    print("Volumes:")
    print("Cube: " + str(vol_cube(2)))  
    print("Cuboid: " + str(vol_cuboid(2, 2, 2)))  
    print("Cone: " + str(vol_cone(2, 2)))  
    print("Right Circular Cone: " + str(vol_right_circ_cone(2, 2)))  
    print("Prism: " + str(vol_prism(2, 2)))  
    print("Pyramid: " + str(vol_pyramid(2, 2)))  
    print("Sphere: " + str(vol_sphere(2)))  
    print("Hemisphere: " + str(vol_hemisphere(2)))  
    print("Circular Cylinder: " + str(vol_circular_cylinder(2, 2)))  
    print("Conical Frustum: " + str(vol_conical_frustum(2, 2, 4)))  
    print("Spherical cap: " + str(vol_spherical_cap(1, 2)))  
    print("Spheres intersetion: " + str(vol_spheres_intersect(2, 2, 1)))  


if __name__ == "__main__":
    main()
