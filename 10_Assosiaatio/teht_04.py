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

    def kulje(self, tunnit):
        self.kul_matka += self.nopeus * tunnit

    def tulosta_ominaisuudet(self):
        print(f"{self.rekisteritunnus:10} | {self.huippunopeus:13} km/h | {self.nopeus:9} km/h | {self.kul_matka:14.1f} km")


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisterinumero':15} | {'Huippunopeus':15} | {'Nopeus':10} | {'Kuljettu matka'}")
        print("-" * 60)
        for auto in self.autot:
            auto.tulosta_ominaisuudet()

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kul_matka >= self.pituus:
                return True
        return False


# Pääohjelma
autot = []
for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    rekisterinumero = f"ABC-{i}"
    autot.append(Auto(rekisterinumero, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
        print(f"\nTilanne {tunti} tunnin jälkeen:")
        kilpailu.tulosta_tilanne()

# Kilpailu päättynyt, tulostetaan lopputilanne
print("\nKilpailu päättynyt. Lopputilanne:")
kilpailu.tulosta_tilanne()
