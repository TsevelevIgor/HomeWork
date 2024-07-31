def log(filename=""):
    """Декоратор отображает информацию о функциях."""
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "w") as file:
                        file.write("my_function ok")
                else:
                    print("my_function ok")
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
