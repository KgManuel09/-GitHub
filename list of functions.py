def ps(x, y):
    tl = x + y
    return tl


def ms(x, y):
    tl = x - y
    return tl


def my(x, y):
    tl = x * y
    return tl


def dn(x, y):
    tl = x / y
    return tl


def de(x, y):
    tl = x ** y
    return tl


def pt(x, y):
    tl = x % y
    return tl


def fn(x, y):
    tl = x // y
    return tl


def me(c):
    tl = abs(c)
    return tl


def sqrt(c):
    tl = c ** 1/2
    return tl


def cbrt(c):
    tl = c ** 1/3
    return tl


def rd(c, d):
    tl = round(c, d)
    return tl


def fl(d):
    for i in range(1, d):
        tl = d * i
        return tl

