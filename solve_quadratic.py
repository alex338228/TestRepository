import math


def solve_quadratic(a: float, b: float, c: float):
    """Return roots of equation ax^2 + bx + c = 0.

    Returns:
        tuple[str, tuple[float, ...] | None]: message and roots if they exist.
    """
    if a == 0:
        if b == 0:
            if c == 0:
                return "Бесконечно много решений.", None
            return "Решений нет.", None
        x = -c / b
        return "Линейное уравнение.", (x,)

    d = b ** 2 - 4 * a * c

    if d < 0:
        return "Действительных корней нет.", None
    if d == 0:
        x = -b / (2 * a)
        return "Один корень.", (x,)

    sqrt_d = math.sqrt(d)
    x1 = (-b + sqrt_d) / (2 * a)
    x2 = (-b - sqrt_d) / (2 * a)
    return "Два корня.", (x1, x2)


def main():
    print("Решение квадратного уравнения ax^2 + bx + c = 0")
    try:
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        c = float(input("Введите c: "))
    except ValueError:
        print("Ошибка: нужно вводить числа.")
        return

    message, roots = solve_quadratic(a, b, c)
    print(message)
    if roots:
        if len(roots) == 1:
            print(f"x = {roots[0]}")
        else:
            print(f"x1 = {roots[0]}")
            print(f"x2 = {roots[1]}")


if __name__ == "__main__":
    main()
