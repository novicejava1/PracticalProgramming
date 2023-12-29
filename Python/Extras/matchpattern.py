def point(coord):
    match coord:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            print("No match")

point((0, 0))
point((0, 10))
point((10, 0))
point((25,34))
point(())
