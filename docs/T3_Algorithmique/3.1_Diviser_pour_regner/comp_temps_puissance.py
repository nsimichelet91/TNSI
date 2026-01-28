import matplotlib.pyplot as plt
import time

def puissance(a, n):
    if n == 0:
        return 1
    else:
        return a * puissance(a, n-1)


def puissance_mod(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return puissance_mod(a*a, n//2)
    else:
        return a * puissance_mod(a*a, (n-1)//2)


def mesure_puissance(n):
    t0 = time.perf_counter()
    p = puissance(3,n)
    return time.perf_counter()-t0

def mesure_puissance_mod(n):
    t0 = time.perf_counter()
    p = puissance_mod(3,n)
    return time.perf_counter()-t0


x = list(range(200))

y1 = [mesure_puissance(k) for k in x]
y2 = [mesure_puissance_mod(k) for k in x]

plt.clf()
#plt.figure(figsize=(25, 15))  # Largeur, Hauteur
plt.plot(x, y1, label='classique')
plt.plot(x, y2, label='modulaire')
plt.yscale('log')  # Échelle logarithmique
plt.xlabel('n')
plt.ylabel('Temps (s)')
plt.title('Comparaison des temps d\'exécution')
plt.legend(loc='upper left')
plt.show()