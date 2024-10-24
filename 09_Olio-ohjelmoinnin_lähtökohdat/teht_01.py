class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nyk_nopeus = 0
        self.kul_matka = 0

    def tulosta_ominaisuudet(self):
        print(f"Rekisterinumero: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} km/h, Tämänhetkinen nopeus: {self.nyk_nopeus} km/h, Kuljettu Matka: {self.kul_matka} km")

auto = Auto("ABC-123", 142)
auto.tulosta_ominaisuudet()

