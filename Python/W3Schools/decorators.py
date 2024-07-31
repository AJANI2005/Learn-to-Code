

def uppercase(func):
    def wrapper(arg1):
        value : str = func(arg1)
        result = value.upper()
        return result
    return wrapper


@uppercase
def say_hi(name):
    return f"Hello {name}"

print(say_hi("Nathan"))