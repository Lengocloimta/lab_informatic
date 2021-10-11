'''
Напишите декоратор swap, который делает так,
что задекорированная функция принимает все свои неименованные аргументы в порядке, обратном тому,
в котором их передали (для аргументов с именем не вполне правильно учитывать порядок, в котором они были переданы).
'''
def decorator_swap(func):
    def wrapper(*args,**kwargs):
            new_args = []
            for i in range(len(args)):
                new_args.append(args[len(args)-1-i])
            return func(*new_args,**kwargs )
    return wrapper

@decorator_swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show=True)


