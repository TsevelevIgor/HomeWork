from datetime import time


def log(filename=""):
    """Декоратор отображает информацию о функциях."""
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                time_1 = time()
                result = func(*args, **kwargs)
                time_2 = time()
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"my_function start - {time_1} \nmy_function ok \nmy_function stop - {time_2}")
                else:
                    print(f"my_function start - {time_1} \nmy_function ok \nmy_function stop - {time_2}")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"my_function error: {e}. Inputs: {args}, {kwargs}")
                else:
                    print(f"my_function error: {e}. Inputs: {args}, {kwargs}")
        return wrapper
    return my_decorator


@log(filename='mylog.txt')
def my_function(x: int, y: int) -> int:
    """Принимает два значения и складывает их"""
    return x + y


my_function(1, 2)
