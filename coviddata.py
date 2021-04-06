import matplotlib.pyplot as plt

cases_pol = {}

with open("full_data.csv") as f:
    for line in f:
        dane = line.split(",")
        date = dane[0]
        country = dane[1]
        cases = dane[2]
        if country == "Poland":
            cases_pol[date] = cases

x = cases_pol.keys()
y = cases_pol.values()
plt.plot(x, y)
plt.xlabel("data")
plt.ylabel("ilość zachorowań")
plt.show()
