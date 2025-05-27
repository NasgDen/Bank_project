from functools import wraps
from time import ctime


def log(file_name=None):
    def log_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                start_time = ctime()
                result = function(*args, **kwargs)
                end_time = ctime()
                if file_name:
                    with open(file_name, mode="a", encoding="utf-8") as file:
                        file.write(f"{start_time}: Начало работы функции {function.__name__}\n")
                        file.write(f"{end_time}: Функция {function.__name__} успешно завершила работу\n")
                        file.write(f"Передаваемые параметры {args, kwargs}\n")
                else:
                    print(f"{start_time}: Начало работы функции {function.__name__}")
                    print(f"{end_time}: Функция {function.__name__} успешно завершила работу")
                    print(f"Передаваемые параметры {args, kwargs}")
                return result
            except Exception as error:
                error_time = ctime()
                error_type = type(error).__name__
                if file_name:
                    with open(file_name, mode="a", encoding="utf-8") as file:
                        file.write(f"{error_time}: Ошибка в работе функции {function.__name__}: {error_type}\n")
                        file.write(f"Аргументы функции: {args, kwargs}\n")
                else:
                    print(f"{error_time}: Ошибка в работе функции {function.__name__}: {error_type}")
                    print(f"Аргументы функции {function.__name__}: {args, kwargs}")
                return error_type
        return wrapper
    return log_decorator
