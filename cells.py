import numpy as np
import matplotlib.pyplot as plt
import sys

# sprawdzanie rodzaju i ilości argmuentów

if len(sys.argv) != 4:
    sys.exit("Zła liczba argumentów.")
try:
    number = int(sys.argv[1])
    state_string = sys.argv[2]
    steps = int(sys.argv[3])
except:
    sys.exit("Zły rodzaj argumentów.")

# zamiana inital_state na np.array

state = np.array(list(state_string))


# funkcja przyporządkowująca tripletowi bit zasady

def rule_index(triplet):
    sL, sC, sR = triplet
    L = int(sL)
    C = int(sC)
    R = int(sR)
    index = 26 - (9 * L + 3 * C + R)
    return int(index)


# funkcja tworząca macierz wyników

def CA_run(rule_number, initial_state, n_steps):
    shift = 3 ** 27
    rule_string = np.base_repr(rule_number + shift, 3)[-27:]  # numer zasady w base 3 + trochę przeskoków, żeby numer
    # miał 27 bitów długości, bo base_repr nie ma 'width'
    rule = np.array([int(i) for i in rule_string])

    m_cells = len(initial_state)
    CA = np.zeros((n_steps, m_cells))
    CA[0, :] = initial_state  # pierwszy wiersz to initial_state

    for step in range(1, n_steps):
        all_triplets = np.stack([np.roll(CA[step - 1, :], 1),
                                 CA[step - 1, :],
                                 np.roll(CA[step - 1, :], -1)])

        CA[step, :] = rule[np.apply_along_axis(rule_index, 0, all_triplets)]  # kolejne wiersze wypełniane według zasady

    return CA


# funkcja rysująca wynik

plt.rcParams['image.cmap'] = 'binary'

data = CA_run(number, state, steps)

fig, ax = plt.subplots(figsize=(16, 9))
ax.matshow(data)
ax.axis(False)

plt.show()
