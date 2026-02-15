import cmath
import math


def solve_quadratic(a: float, b: float, c: float):
    """Return roots of equation ax^2 + bx + c = 0."""
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


def cbrt(z: complex) -> complex:
    """Complex cube root."""
    if z == 0:
        return 0j
    r, phi = cmath.polar(z)
    return cmath.rect(r ** (1 / 3), phi / 3)


def solve_cubic(a: float, b: float, c: float, d: float):
    """Return roots of equation ax^3 + bx^2 + cx + d = 0."""
    if a == 0:
        return solve_quadratic(b, c, d)

    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)

    delta = (q / 2) ** 2 + (p / 3) ** 3

    u = cbrt(-q / 2 + cmath.sqrt(delta))
    v = cbrt(-q / 2 - cmath.sqrt(delta))

    omega = complex(-0.5, math.sqrt(3) / 2)

    y1 = u + v
    y2 = u * omega + v * (omega ** 2)
    y3 = u * (omega ** 2) + v * omega

    shift = b / (3 * a)
    roots = (y1 - shift, y2 - shift, y3 - shift)

    # Clean tiny imaginary/real parts caused by floating-point errors.
    cleaned_roots = tuple(
        complex(
            0 if abs(root.real) < 1e-12 else root.real,
            0 if abs(root.imag) < 1e-12 else root.imag,
        )
        for root in roots
    )

    return "Корни кубического уравнения.", cleaned_roots


def format_root(root):
    if isinstance(root, complex):
        if root.imag == 0:
            return f"{root.real}"
        sign = "+" if root.imag >= 0 else "-"
        return f"{root.real} {sign} {abs(root.imag)}i"
    return f"{root}"


def main():
    print("Выберите тип уравнения:")
    print("1 — квадратное (ax^2 + bx + c = 0)")
    print("2 — кубическое (ax^3 + bx^2 + cx + d = 0)")
    choice = input("Введите 1 или 2: ").strip()

    if choice == "1":
        try:
            a = float(input("Введите a: "))
            b = float(input("Введите b: "))
            c = float(input("Введите c: "))
        except ValueError:
            print("Ошибка: нужно вводить числа.")
            return

        message, roots = solve_quadratic(a, b, c)
    elif choice == "2":
        try:
            a = float(input("Введите a: "))
            b = float(input("Введите b: "))
            c = float(input("Введите c: "))
            d = float(input("Введите d: "))
        except ValueError:
            print("Ошибка: нужно вводить числа.")
            return

        message, roots = solve_cubic(a, b, c, d)
    else:
        print("Ошибка: выберите 1 или 2.")
        return

    print(message)
    if roots:
        for i, root in enumerate(roots, start=1):
            print(f"x{i} = {format_root(root)}")


if __name__ == "__main__":
    main()
