"""Simple calculator: addition, subtraction, percentage."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def percent(value: float, pct: float) -> float:
    """Return pct percent of value."""
    return value * (pct / 100)


def main() -> None:
    print("Калькулятор: +, -, %")
    op = input("Выберите операцию (+, -, %): ").strip()
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = subtract(a, b)
    elif op == "%":
        result = percent(a, b)
    else:
        print("Неизвестная операция")
        return

    print(f"Результат: {result}")


if __name__ == "__main__":
    main()
