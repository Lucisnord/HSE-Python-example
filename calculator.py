
**calculator.py:**
```python
"""
Простой калькулятор для выполнения базовых арифметических операций
"""

def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание второго числа из первого"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление первого числа на второе"""
    if b == 0:
        raise ValueError("Нельзя делить на ноль!")
    return a / b

def power(a, b):
    """Возведение в степень"""
    return a ** b

def modulus(a, b):
    """Остаток от деления"""
    if b == 0:
        raise ValueError("Нельзя делить на ноль!")
    return a % b

def main():
    """Основная функция калькулятора"""
    print("=== Простой калькулятор ===")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    
    try:
        choice = input("Выберите операцию (1/2/3/4): ")
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        if choice == '1':
            result = add(num1, num2)
            operator = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operator = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operator = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operator = "/"
        elif choice == '5':
            result = power(num1, num2)
            operator = "^"
        elif choice == '6':
            result = modulus(num1, num2)
            operator = "%"           
        else:
            print("Неверный выбор!")
            return
        
        print(f"\nРезультат: {num1} {operator} {num2} = {result}")
        
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
