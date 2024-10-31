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
        print(f"Rekisterinumero: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} km/h, "
              f"Tämänhetkinen nopeus: {self.nopeus} km/h, Kuljettu Matka: {self.kul_matka} km")


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_ominaisuudet(self):
        super().tulosta_ominaisuudet()
        print(f"Akkukapasiteetti: {self.akkukapasiteetti} kWh")


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko

    def tulosta_ominaisuudet(self):
        super().tulosta_ominaisuudet()
        print(f"Tankin koko: {self.tankin_koko} l")


sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdyta(150)
polttomoottoriauto.kiihdyta(120)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print("\nSähköauto:")
sahkoauto.tulosta_ominaisuudet()

print("\nPolttomoottoriauto:")
polttomoottoriauto.tulosta_ominaisuudet()
