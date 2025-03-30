def countAndSay(func):
    def wrapper(*args):
        print('Сейчас посчитаю!')
        result = func(*args)
        return result
    return wrapper

@countAndSay
def foo(a,b):
    return print(a+b)

foo(1,3)