def countAndSay(func):
    def wrapper(*args):
        print('Сейчас посчитаю!')
        result = func(*args)
        return result
    return wrapper

@countAndSay
def summ(a,b):
    return print(a+b)

@countAndSay
def mult(a,b):
    return print(a*b)