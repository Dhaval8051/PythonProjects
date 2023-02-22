from math_article import volume


def area_of_all():
    result = volume.area_of_the_circle(10)
    print(f"1) Area of circle is {result}")

    triang = volume.triangle_area(2, 3, 4)
    print(f"2) Area of triangle is {triang}")

    trape = volume.trapezium(4, 5, 6)
    print(f"3) Area of trapezium is {trape}")

    squar = volume.square_area(2)
    print(f"4) Area of square_area is {squar}")

    sphr = volume.Sphere(5)
    print(f"5) Area of Sphere is {sphr}")

    clylin = volume.Cylinder(5, 6)
    print(f"6) Area of Cylinder is {clylin}")

    hexagonal = volume.volumeHexagonal(5, 6, 7)
    print(f"7) Area of Pyramid is {hexagonal}")

    volume = volume.Volume_of_cone(6, 7)
    print(f"8) Area of cone is {volume}")



