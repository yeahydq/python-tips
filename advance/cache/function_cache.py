import functools

# https://zhuanlan.zhihu.com/p/27643991

def track(func):
    @functools.wraps(func)
    def inner(*args, **kwds):
        result = func(*args, **kwds)
        print("{} --> ({}) --> {} ".format(func.__name__, args[0], result))
        return result
    return inner


@track
def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


@functools.lru_cache()
@track
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n - 2) + fib_with_cache(n - 1)


if __name__ == '__main__':
    fib(10)
    # fib_with_cache(30)
