from time import ctime
from functools import wraps


def log(file_name=None):
    def log_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                if file_name:
                    with open(file_name, mode="a", encoding="utf-8") as file:
                        file.write(f"{ctime()}: Начало работы функции {function.__name__}\n")
                        # file.write(f"Функция {args, kwargs} успешно завершила работу\n")
                        # file.write(f"Передаваемые параметры {args, kwargs}\n")
                else:
                    print(f"{ctime()}: Начало работы функции {function.__name__}")
                    # print(f"Передаваемые параметры {args, kwargs}")
                result = function(*args, **kwargs)
                if file_name:
                    with open(file_name, mode="a", encoding="utf-8") as file:
                        file.write(f"{ctime()}: Функция успешно завершила работу\n")
                        # file.write(f"Передаваемые параметры {args, kwargs}\n")
                else:
                    print(f"{ctime()}: Функция успешно завершила работу")
                    # print(f"Передаваемые параметры {args, kwargs}")
            except Exception as error:
                error_type = type(error).__name__
                if file_name:
                    with open(file_name, mode="a", encoding="utf-8") as file:
                        file.write(f"{ctime()}: Ошибка в работе функции {function.__name__}: {error_type}\n")
                        # file.write(f"Функция {args, kwargs} успешно завершила работу\n")
                        file.write(f"Аргументы функции: {args, kwargs}\n")
                else:
                    print(f"{ctime()}: Ошибка в работе функции {function.__name__}: {error_type}")
                    print(f"Аргументы функции {function.__name__}: {args, kwargs}")
            return result
        return wrapper
    return log_decorator
