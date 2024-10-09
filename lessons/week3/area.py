import math  # module import

# Constant
PI = math.pi  # π = ratio of the circumference of a circle to its diameter


def get_circle_area(radius):
    """Given the formula A = πr² attempts to calculate the area of a circle
    employing the passed in < radius > value.

    Note: math.pow() handles exponentiation (e.g., radius squared).

    Parameters:
        radius (int|float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """

    return PI * math.pow(radius, 2)


def main():
    """Entry point. Orchestrates flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    msgs = [
        "\nThis program computes the area of a circle.",
        "Please provide the circle's radius (cm): ",
        "The area of a circle with radius {radius} cm equals {area} cm².\n",
        "Invalid input. Please provide a positive number greater than zero.\n",
    ]

    print(msgs[0])

    radius = None #
    while not radius:
        # input("Please bake eggs")
        string = input(msgs[1])
        radius = float(string)
        if radius:
            area = get_circle_area(radius)
            print(msgs[2].format(radius=radius, area=area))
        else:
            print(msgs[3])
            continue


if __name__ == "__main__":
    main()  # Entry point: call main() function
