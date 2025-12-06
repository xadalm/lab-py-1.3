from src.fibo_fact.fibo import fibo
from src.fibo_fact.fibo_recursive import fibo_recursive
from src.fibo_fact.factorial import factorial
from src.fibo_fact.factorial_recursive import factorial_recursive
from src.sort.bubble_sort import bubble_sort
from src.sort.bucket_sort import bucket_sort
from src.sort.counting_sort import counting_sort
from src.sort.heap_sort import heap_sort
from src.sort.quick_sort import quick_sort
from src.sort.radix_sort import radix_sort
from src.stack.stack import Stack

def show_menu():
    print("\n\nГЛАВНОЕ МЕНЮ\n")
    print("Выберите раздел:")
    print("1. Числа Фибоначчи")
    print("2. Факториал")
    print("3. Сортировка")
    print("4. Стек")
    print("0. Выход")


def fibo_menu():
    print("\n--- Фибоначчи ---")
    print("1. Итеративный алгоритм")
    print("2. Рекурсивный алгоритм")
    choice = input("Выберите: ")
    if choice not in ("1", "2"):
        print("Неверный выбор. Возврат в меню.")
        return

    try:
        n = int(input("Введите число: "))
    except ValueError:
        print("Ошибка: введите целое число. Возврат в меню.")
        return

    if choice == "1":
        print(f"Результат (итеративный): {fibo(n)}")
    else:
        print(f"Результат (рекурсивный): {fibo_recursive(n)}")


def factorial_menu():
    print("\n--- Факториал ---")
    print("1. Итеративный алгоритм")
    print("2. Рекурсивный алгоритм")
    choice = input("Выберите: ")
    if choice not in ("1", "2"):
        print("Неверный выбор. Возврат в меню.")
        return
    
    try:
        n = int(input("Введите число: "))
    except ValueError:
        print("Ошибка: введите целое число. Возврат в меню.")
        return

    if choice == "1":
        print(f"Результат (итеративный): {factorial(n)}")
    else:
        print(f"Результат (рекурсивный): {factorial_recursive(n)}")


def sort_menu():
    print("\n--- Сортировка ---")
    print("1. Bubble Sort")
    print("2. Bucket Sort")
    print("3. Counting Sort")
    print("4. Heap Sort")
    print("5. Quick Sort")
    print("6. Radix Sort")
    
    choice = input("Выберите алгоритм: ")
    algorithms = {
        "1": bubble_sort,
        "2": bucket_sort,
        "3": counting_sort,
        "4": heap_sort,
        "5": quick_sort,
        "6": radix_sort,
    }
    if choice not in algorithms:
        print("Неверный выбор алгоритма. Возврат в меню.")
        return

    nums = input("Введите числа через пробел: ")
    if not nums:
        print("Ошибка: пустой ввод. Возврат в меню.")
        return
    try:
        arr = list(map(int, nums.split()))
    except ValueError:
        print("Ошибка: введите только целые числа. Возврат в меню.")
        return

    print(f"Результат сортировки: {algorithms[choice](arr)}")


def stack_menu():
    print("\n--- Стек ---")
    print("1. Push (добавить)")
    print("2. Pop (удалить)")
    print("3. Peek (посмотреть верхний элемент)")
    print("4. Показать весь стек")
    print("0. Назад в меню")
    stack = Stack()

    while True:
        choice = input("\nВыберите операцию: ")
        
        if choice == "1":
            value = input("Введите значение: ")
            if value == "":
                print("Ошибка: пустое значение. Попробуйте снова.")
                continue
            stack.push(value)
            print(f"Добавлено: {value}")
        elif choice == "2":
            try:
                result = stack.pop()
                print(f"Удалено: {result}")
            except Exception:
                print("Стек пуст или ошибка при удалении.")
        elif choice == "3":
            try:
                result = stack.peek()
                print(f"Верхний элемент: {result}")
            except Exception:
                print("Стек пуст или ошибка при просмотре.")
        elif choice == "4":
            print(f"Стек: {stack.items}")
        elif choice == "0":
            break
        else:
            print("Неверный выбор операции. Попробуйте снова.")

def main():
    try:
        while True:
            show_menu()
            choice = input("Выберите раздел: ").strip()
            if choice == "1":
                fibo_menu()
            elif choice == "2":
                factorial_menu()
            elif choice == "3":
                sort_menu()
            elif choice == "4":
                stack_menu()
            elif choice == "0":
                print("До свидания!")
                break
            else:
                print("Неверный выбор, попробуйте снова")
    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем")

if __name__ == "__main__":
    main()