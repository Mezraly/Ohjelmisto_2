import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kul_matka = 0

    def kiihdyta(self, muutos):
        uusi_nopeus = self.nopeus + muutos
        if uusi_nopeus < 0:
            self.nopeus = 0
        elif uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = uusi_nopeus
        print(f"Uusi nopeus: {self.nopeus} km/h")

    def kulje(self, tunnit):
        self.kul_matka += self.nopeus * tunnit
        print(f"Matkaa kuljettu: {self.kul_matka} km")

    def tulosta_ominaisuudet(self):
        print(f"Rekisterinumero: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} km/h, Tämänhetkinen nopeus: {self.nopeus} km/h, Kuljettu Matka: {self.kul_matka} km")

autot = []
for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    rekisterinumero = f"ABC-{i}"
    autot.append(Auto(rekisterinumero, huippunopeus))

kilpailu = True
while kilpailu:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(1)
        if auto.kul_matka >= 10000:
            kilpailu_jatkuu = False
            break

for auto in autot:
    auto.tulosta_ominaisuudet()