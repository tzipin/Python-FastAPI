import datetime


# 1
def run_time(func):
    def inner(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        end = datetime.datetime.now()
        return end - start

    return inner


@run_time
def sum():
    sum = 0
    for i in range(100000000):
        sum += i


# print(sum())

# 2
dict = {}


def cache(func):
    def inner(n):
        if dict.keys().__contains__(n):
            return dict[n]
        else:
            dict[n] = func(n)
            return dict[n]

    return inner


@run_time
@cache
def fibunachi(n):
    if n == 0:
        return 0
    if n == 2 or n == 1:
        return 1
    else:
        return fibunachi(n - 1) + fibunachi(n - 2)


print(fibunachi(100))
print(fibunachi(100))
