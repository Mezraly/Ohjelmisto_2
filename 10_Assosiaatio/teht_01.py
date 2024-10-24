class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        while self.nykyinen_kerros != kohde_kerros:
            if kohde_kerros > self.nykyinen_kerros:
                self.kerros_ylos()
            else:
                self.kerros_alas()

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi nousi kerrokseen {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi laskeutui kerrokseen {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo alimmassa kerroksessa.")


# Testiohjelma
h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)
