import matplotlib.pyplot as plt
import math as m


def frange(a, b, d):
    lista = []
    i = a
    while i < b:
        lista.append(i)
        i += d
    return lista


def plotf(f, a, b):
    x = frange(a, b, 0.1)
    y = [f(i) for i in x]
    plt.plot(x, y)

    plt.xlabel("x")
    plt.ylabel(r"$xsin(x) - x^2$")

    plt.title("Wykres funkcji")

    plt.show()


def fun(x):
    return x * m.sin(x) - x ** 2


a = int(input("a = "))
b = int(input("b = "))

plotf(fun, a, b)
