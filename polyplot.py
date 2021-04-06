import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def gfrange(a, b, d):
    lista = []
    i = a
    while i < b:
        lista.append(i)
        i += d
    return lista


x = gfrange(1, 5.5, 0.1)

y1 = [3 * (i - 1) for i in x]
y2 = [3 * (i - 1) * (i - 2) for i in x]
y3 = [3 * (i - 1) * (i - 2) * (i - 3) for i in x]
y4 = [3 * (i - 1) * (i - 2) * (i - 3) * (i - 4) for i in x]
y5 = [3 * (i - 1) * (i - 2) * (i - 3) * (i - 4) * (i - 5) for i in x]

with PdfPages('polyplot.pdf') as pdf:
    plt.figure(figsize=(3, 3))
    plt.plot(x, y1)
    plt.title("y1")
    pdf.savefig()
    plt.close()

    plt.figure(figsize=(3, 3))
    plt.plot(x, y2)
    plt.title("y2")
    pdf.savefig()
    plt.close()

    plt.figure(figsize=(3, 3))
    plt.plot(x, y3)
    plt.title("y3")
    pdf.savefig()
    plt.close()

    plt.figure(figsize=(3, 3))
    plt.plot(x, y4)
    plt.title("y4")
    pdf.savefig()
    plt.close()

    plt.figure(figsize=(3, 3))
    plt.plot(x, y5)
    plt.title("y5")
    pdf.savefig()
    plt.close()
