class MathUtils:
    def add(a: int, b: int) -> int:
        return a + b

    def subtract(a: int, b: int) -> int:
        return a - b

    def multiply(a: int, b: int) -> int:
        return a * b

    def divide(a: int, b: int) -> float:
        try:
            return float(f'{a / b:.2f}')
        except ZeroDivisionError:
            return -1.0


#print(MathUtils.divide(-2, -2))
