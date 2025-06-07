
class Konto:
    def __init__(self, wlasciciel, saldo=0):
        """Inicjalizacja konta: właściciel i początkowe saldo."""
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def wplac(self, kwota):
        """Wpłata podanej kwoty na konto."""
        self.saldo += kwota
        print(f"Wpłacono {kwota}. Nowe saldo: {self.saldo}")

    def wyplac(self, kwota):
        """Wypłata podanej kwoty, jeśli środki są wystarczające."""
        if kwota <= self.saldo:
            self.saldo -= kwota
            print(f"Wypłacono {kwota}. Nowe saldo: {self.saldo}")
        else:
            print("Niewystarczająca ilość środków na koncie.")

    def pokaz_saldo(self):
        """Wyświetlenie aktualnego salda konta."""
        print(f"Aktualne saldo: {self.saldo}")


def main():
    konto = Konto("Janusz", 1550)

    while True:
        print("\nWybierz opcję:")
        print("1) Wpłata")
        print("2) Wypłata")
        print("3) Sprawdź saldo")
        print("4) Wyjście")

        wybor = input("Podaj wybór: ").strip().lower()

        if wybor in ("1", "wpłata", "wplata"):
            try:
                kwota = int(input("Podaj kwotę wpłaty: "))
                konto.wplac(kwota)
            except ValueError:
                print("Podaj poprawną liczbę.")
        elif wybor in ("2", "wypłata", "wyplata"):
            try:
                kwota = int(input("Podaj kwotę wypłaty: "))
                konto.wyplac(kwota)
            except ValueError:
                print("Podaj poprawną liczbę.")
        elif wybor in ("3", "sprawdź saldo", "sprawdz saldo", "saldo"):
            konto.pokaz_saldo()
        elif wybor in ("4", "wyjście", "wyjscie", "koniec"):
            print("Do widzenia!")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
