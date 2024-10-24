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


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissia(self, hissin_numero, kohde_kerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissin_numero} kohdekerrokseen {kohde_kerros}")
            self.hissit[hissin_numero].siirry_kerrokseen(kohde_kerros)
        else:
            print("Virheellinen hissin numero.")

    def palohalytys(self):
        print("Palohälytys! Kaikki hissit siirtyvät alimpaan kerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)

# Testiohjelma
talo = Talo(1, 10, 3)
talo.aja_hissia(0, 5)
talo.palohalytys()