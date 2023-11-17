# Write a function that returns the root of a quadratic equation,
# It should take 3 parameters and return a tuple of at most 2 numbers.


def quadratic_calculator(a: float, b: float, c: float):
    x = 0
    y = 0


    # Your code goes here
    # This is my answer 
    x=(-b+((b)**2-(4*a*c))**0.5)/2*a
    y=(-b-((b)**2-(4*a*c))**0.5)/2*a
    return (x, y)


if __name__ == "__main__":
    x, y = quadratic_calculator(1, 5, 6)

    print(f"The roots of the equation are {x} and {y}")
