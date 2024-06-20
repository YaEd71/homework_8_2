#Три собственных класса исключений: `InvalidDataException`, `ProcessingException` и `MyCustomException`.
class InvalidDataException(Exception):
    pass

class ProcessingException(Exception):
    pass

class MyCustomException(Exception):
    pass
# Функция generate_exception(argument) генерирует исключения в зависимости от переданного аргумента.
def generate_exception(argument):
    if argument == 1:
        raise InvalidDataException("Произошло исключение с недопустимыми данными.")
    elif argument == 2:
        raise ProcessingException("Произошло исключение при обработке.")
    elif argument == 3:
        raise MyCustomException("Произошло мое пользовательское исключение.")
# Функция `main_function(argument)` обрабатывает эти исключения с использованием блоков `try`, `except`, `else`
# и `finally`,а затем передает их дальше по стеку вызовов с помощью оператора `raise`
def main_function(argument):
    try:
        generate_exception(argument)
    except InvalidDataException as e:
        print(f"Обработка исключения InvalidDataException: {e}")
        raise
    except ProcessingException as e:
        print(f"Обработка ProcessingException: {e}")
        raise
    except MyCustomException as e:
        print(f"Обработка MyCustomException: {e}")
        raise
    else:
        print("Никаких исключений не было.")
    finally:
        print("Завершаю работу...")
# В основной части программы вызываются функции с разными аргументами и каждое исключение обрабатывается в блоке `except`
try:
    main_function(1)
except Exception as e:
    print(f"Исключение обрабатывается в основной программе: {e}")

try:
    main_function(2)
except Exception as e:
    print(f"Исключение обрабатывается в основной программе: {e}")

try:
    main_function(3)
except Exception as e:
    print(f"Исключение обрабатывается в основной программе: {e}")

#Таким образом демонстрируется передача исключений по стеку вызовов и их обработка в разных частях программы.