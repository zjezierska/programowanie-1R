import matplotlib.pyplot as plt
import math as m


def gfrange(a, b, d):
    lista = []
    i = a
    while i < b:
        lista.append(i)
        i += d
    return lista


x1 = gfrange(-0.5, 0.5, 0.05)
y1 = [i for i in x1]
plt.plot(x1, y1, label="y = x")

y2 = [m.sin(i) for i in x1]
plt.plot(x1, y2, label="y = sin(x)")

y3 = [m.tan(i) for i in x1]
plt.plot(x1, y3, label="y = tg(x)")

plt.xlabel("Argumenty")
plt.ylabel("Funkcje")

plt.title("Trzy krzywe na jednym wykresie")

plt.legend()

n = input("W jakim formacie zapisać plik? ")

if n == "png":
    plt.savefig("trigplot.png")
elif n == "jpg":
    plt.savefig("trigplot.jpg")
elif n == "svg":
    plt.savefig("trigplot.svg")
elif n == "pdf":
    plt.savefig("trigplot.pdf")
else:
    print("Nie ma takiego rozszerzenia!")

plt.show()
