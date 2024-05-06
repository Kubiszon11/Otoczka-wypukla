import random
import matplotlib.pyplot as plt
import numpy as np

ile_tygrysow = 10
promien_losowania = 50
wszystkie_punkty = []


class Tygrys:
    def __init__(self):
        self.x = random.uniform(-promien_losowania, promien_losowania)
        self.y = random.uniform(-promien_losowania, promien_losowania)
        self.centrum = [self.x,self.y]
        self.a = random.uniform(0, 10)
        self.b = 2
        self.gamma = random.uniform(0, np.pi/4)
        self.beta = random.uniform(0, np.pi/6)
        self.p1 = [self.x + self.a, self.y + self.a]#
        self.p2 = [self.x - self.a, self.y + self.a]#
        kat = np.pi - np.pi/4 - self.beta/4 - self.gamma/2
        self.p3 = [self.x + self.b, self.y + self.b/(np.tan(kat))]#
        #self.p3 = [self.p1[0] +(self.p1[0]-self.centrum[0])*np.cos(self.gamma) - (self.p1[1]-self.centrum[1])*np.sin(self.gamma),self.p1[0] +(self.p1[0]-self.centrum[0])*np.sin(self.gamma) - (self.p1[1]-self.centrum[1])*np.cos(self.gamma)]
        #self.p4 =[self.p3[0] +(self.p3[0]-self.centrum[0])*np.cos(2*kat) - (self.p3[1]-self.centrum[1])*np.sin(2*kat),self.p3[0] +(self.p3[0]-self.centrum[0])*np.sin(2*kat) - (self.p3[1]-self.centrum[1])*np.cos(2*kat)]

       # self.p4 = [self.x + self.b, self.y - self.b/(np.tan(np.pi/2 - self.beta/2))]
        self.p4 = [self.x - self.b*np.sin(np.pi + self.gamma),self.y +  self.b*np.cos(np.pi + self.gamma) ]
        self.p6 = [self.x + self.b * np.sin(np.pi + self.gamma), self.y + self.b * np.cos(np.pi + self.gamma)]


        self.p5 = [self.x - self.b, self.y + self.b/(np.tan(kat))]#
       # self.p5 =[self.p6[0] +(self.p6[0]-self.centrum[0])*np.cos(2*kat) - (self.p6[1]-self.centrum[1])*np.sin(2*kat),self.p6[0] +(self.p6[0]-self.centrum[0])*np.sin(2*kat) - (self.p6[1]-self.centrum[1])*np.cos(2*kat)]
        #self.p6 = [self.x - self.b, self.y - self.b/(np.tan(np.pi/2 - self.beta/2))]
        #self.p6 = [self.p4[0] +(self.p4[0]-self.centrum[0])*np.cos(self.beta) - (self.p4[1]-self.centrum[1])*np.sin(self.beta),self.p4[0] +(self.p4[0]-self.centrum[0])*np.sin(self.beta) - (self.p4[1]-self.centrum[1])*np.cos(self.beta)]


        self.x1 = [self.x, self.p1[0], self.p2[0], self.p3[0], self.p4[0], self.p5[0]]
        self.y1 = [self.y, self.p1[1], self.p2[1], self.p3[1], self.p4[1], self.p5[1]]


def wzajemne_polozenie_punktow(pewny, podejrzany, iterowany):
    # opcja = (podejrzany.y - pewny.y) * (iterowany.x - podejrzany.x) - (podejrzany.x - pewny.x) * (
    #             iterowany.y - podejrzany.y)
    opcja = (podejrzany[1] - pewny[1]) * (iterowany[0] - podejrzany[0]) - (podejrzany[0] - pewny[0]) * (iterowany[1] - podejrzany[1])

    if opcja == 0:
        return 0
    elif opcja > 0:
        return 1
    elif opcja < 0:
        return 2


# def algorytm_jarvisa(tygryski):
#     otoczka = []
#     poczatkowy = min(tygryski, key=lambda punkt: punkt.y)
#
#     pewny = poczatkowy
#     podejrzany = None
#
#     while podejrzany != poczatkowy:
#         otoczka.append(pewny)
#         podejrzany = None
#         for iterowany in tygryski:
#             if podejrzany is None or wzajemne_polozenie_punktow(pewny, podejrzany, iterowany) == 2:
#                 podejrzany = iterowany
#         pewny = podejrzany
#
#     return otoczka

def algorytm_jarvisa(tygryski):
    otoczka = []
    poczatkowy = min(tygryski, key=lambda punkt: punkt[1])

    pewny = poczatkowy
    podejrzany = None

    while podejrzany != poczatkowy:
        otoczka.append(pewny)
        podejrzany = None
        for iterowany in tygryski:
            if podejrzany is None or wzajemne_polozenie_punktow(pewny, podejrzany, iterowany) == 2:
                podejrzany = iterowany
        pewny = podejrzany

    return otoczka


# def rysuj_plansze(tygrysy, otoczka_wypukla):
#     xs = [punkt.x for punkt in tygrysy]
#     ys = [punkt.y for punkt in tygrysy]
#     plt.scatter(xs, ys, color='orange', marker='o')
#
#     xp1 = [punkt.p1[0] for punkt in tygrysy]
#     yp1 = [punkt.p1[1] for punkt in tygrysy]
#     plt.scatter(xp1, yp1, color='red', marker='o')
#
#     xp2 = [punkt.p2[0] for punkt in tygrysy]
#     yp2 = [punkt.p2[1] for punkt in tygrysy]
#     plt.scatter(xp2, yp2, color='red', marker='o')
#
#     xp3 = [punkt.p3[0] for punkt in tygrysy]
#     yp3 = [punkt.p3[1] for punkt in tygrysy]
#     plt.scatter(xp3, yp3, color='red', marker='o')
#
#     xp4 = [punkt.p4[0] for punkt in tygrysy]
#     yp4 = [punkt.p4[1] for punkt in tygrysy]
#     plt.scatter(xp4, yp4, color='red', marker='o')
#
#     xp5 = [punkt.p5[0] for punkt in tygrysy]
#     yp5 = [punkt.p5[1] for punkt in tygrysy]
#     plt.scatter(xp5, yp5, color='red', marker='o')
#
#     for i in tygrysy:
#         ksztalt = []
#         ksztalt.append(i.p1)
#         ksztalt.append(i.p2)
#         ksztalt.append(i.p4)
#         ksztalt.append(i.p3)
#         ksztalt.append(i.p1)
#         ksztalt.append(i.p5)
#         ksztalt.append(i.p2)
#         wszystkie_punkty.append(ksztalt)
#         kx = [punkt[0] for punkt in ksztalt]
#         ky = [punkt[1] for punkt in ksztalt]
#         plt.plot(kx, ky, color='orange', linestyle='-', linewidth=2)
#
#     otoczka_wypukla.append(otoczka_wypukla[0])
#     hx = [punkt.x for punkt in otoczka_wypukla]
#     hy = [punkt.y for punkt in otoczka_wypukla]
#     plt.plot(hx, hy, color='black', linestyle='-', linewidth=2, label='Otoczka wypukla')
#
#     plt.title('Otaczanie Tygrysow')
#     plt.legend()
#     plt.show()
def rysuj_plansze(tygrysy, otoczka_wypukla):
    xs = [punkt.x for punkt in tygrysy]
    ys = [punkt.y for punkt in tygrysy]
    plt.scatter(xs, ys, color='orange', marker='o')

    xp1 = [punkt.p1[0] for punkt in tygrysy]
    yp1 = [punkt.p1[1] for punkt in tygrysy]
    plt.scatter(xp1, yp1, color='red', marker='o')

    xp2 = [punkt.p2[0] for punkt in tygrysy]
    yp2 = [punkt.p2[1] for punkt in tygrysy]
    plt.scatter(xp2, yp2, color='red', marker='o')

    xp3 = [punkt.p3[0] for punkt in tygrysy]
    yp3 = [punkt.p3[1] for punkt in tygrysy]
    plt.scatter(xp3, yp3, color='red', marker='o')

    xp4 = [punkt.p4[0] for punkt in tygrysy]
    yp4 = [punkt.p4[1] for punkt in tygrysy]
    plt.scatter(xp4, yp4, color='blue', marker='o')

    xp5 = [punkt.p5[0] for punkt in tygrysy]
    yp5 = [punkt.p5[1] for punkt in tygrysy]
    plt.scatter(xp5, yp5, color='red', marker='o')

    xp6 = [punkt.p6[0] for punkt in tygrysy]
    yp6 = [punkt.p6[1] for punkt in tygrysy]
    plt.scatter(xp6, yp6, color='blue', marker='o')

    for i in tygrysy:
        ksztalt = []
        ksztalt.append(i.centrum)
        ksztalt.append(i.p1)
        ksztalt.append(i.p2)
        ksztalt.append(i.centrum)
        ksztalt.append(i.p3)
        ksztalt.append(i.p4)
        ksztalt.append(i.centrum)
        ksztalt.append(i.p5)
        ksztalt.append(i.p6)
        ksztalt.append(i.centrum)
        wszystkie_punkty.append(ksztalt)
        kx = [punkt[0] for punkt in ksztalt]
        ky = [punkt[1] for punkt in ksztalt]
        plt.plot(kx, ky, color='orange', linestyle='-', linewidth=2)

    otoczka_wypukla.append(otoczka_wypukla[0])
    hx = [punkt[0] for punkt in otoczka_wypukla]
    hy = [punkt[1] for punkt in otoczka_wypukla]
    plt.plot(hx, hy, color='black', linestyle='-', linewidth=2, label='Otoczka wypukla')

    plt.title('Otaczanie Tygrysow')
    plt.legend()
    plt.axis('equal')
    plt.show()


if __name__ == "__main__":

    tygrysy = []
    for _ in range(ile_tygrysow):
        tygrysy.append(Tygrys())

    for punkt in tygrysy:
        wszystkie_punkty.append(punkt.centrum)
        wszystkie_punkty.append(punkt.p1)
        wszystkie_punkty.append(punkt.p2)
        wszystkie_punkty.append(punkt.p3)
        wszystkie_punkty.append(punkt.p4)
        wszystkie_punkty.append(punkt.p5)
        wszystkie_punkty.append(punkt.p6)



    otoczka_wypukla = algorytm_jarvisa(wszystkie_punkty)
    print("Punkty nalezace do otoczki:")
    # for punkt in otoczka_wypukla:
    #     print(f"({punkt.x}, {punkt.y})")

    rysuj_plansze(tygrysy, otoczka_wypukla)

