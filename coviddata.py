import matplotlib.pyplot as plt

cases = {}
kraje = []
with open("full_data.csv") as f:
    for line in f:
        dane = line.split(",")
        date = dane[0]
        country = dane[1]
        if country not in kraje:
            print(country)
            kraje.append(country)

        cases_today = dane[2]
        if country not in cases.keys():
            cases[country] = {}
        cases[country][date] = cases_today

d = input("> ")
if d in kraje:
    x = cases[d].keys()
    y = cases[d].values()
    plt.plot(x, y)
    plt.xlabel("data")
    plt.ylabel("ilość zachorowań")
    plt.show()
else:
    print("Nie ma takiego kraju!")
