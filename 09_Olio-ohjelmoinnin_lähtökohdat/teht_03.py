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

auto = Auto("ABC-123", 142)
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(auto.nopeus)
auto.kiihdyta(-200)
auto.tulosta_ominaisuudet()

