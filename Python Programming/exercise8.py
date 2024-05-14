import math


def discriminant(a: float, b: float, c: float) -> float:
    """
  This function calculates the discriminant of a quadratic equation.

  Params:
      a: The coefficient of the x^2 term.
      b: The coefficient of the x term.
      c: The constant term.

  Returns:
      The discriminant of the quadratic equation.
  """
    return b ** 2 - 4 * a * c


def find_roots(a, b, c) -> [float]:
    """
    This function finds the real roots of a quadratic equation.

    Params:
      a: The coefficient of the x^2 term.
      b: The coefficient of the x term.
      c: The constant term.

    Returns:
      All real roots of the quadratic equation.
    """
    d = discriminant(a, b, c)
    if d < 0:
        return []
    elif d == 0:
        x = -b / (2 * a)
        return [x]
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    return [x1, x2]


def main():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    assert a != 0, 'Equation is not quadratic'

    roots = find_roots(a, b, c)
    print(f'The quadratic equation has {len(roots)} real roots:')
    for root in roots:
        print(f'x = {root}')


if __name__ == '__main__':
    main()
