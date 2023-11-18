def quadratic_calculator(a: float, b: float, c: float):
    denominator = 2**a
    discriminant = b**2 - (4 * a * c)

    if discriminant < 0:
        print("Roots are complex numbers.")

    elif discriminant == 0:
        x = -b / denominator
        print("The root of the equation is ", x)

    else:
        d = pow(discriminant, 0.5)

        x = -b + d
        y = -b - d

        x /= denominator
        y /= denominator

        print(f"The roots of the equation are {x} and {y}")


if __name__ == "__main__":
    # Regular Roots
    quadratic_calculator(1, -5, 6)

    # Single Root
    quadratic_calculator(1, -6, 9)

    # Complex Roots
    quadratic_calculator(2, 1, 1)

    # Weird Inputs
    quadratic_calculator(0, 0, -1)
