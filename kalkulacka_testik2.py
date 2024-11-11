class CustomException(Exception):
    pass


def kalkulacka():
    while True:
        prikaz = input("Napíšte 'koniec' pre ukončenie alebo stlačte Enter pre ďalšiu operáciu: ").strip().lower()
        if prikaz == "koniec":
            print("Kalkulačka bola ukončená.")
            break

        try:
            cislo1 = float(input("Zadajte prve cislo: "))
        except ValueError:
            print("Písmená sa tam nesmú zadávať, zadajte číslo.")
            continue

        operacia = input("Zadajte operaciu (+, -, *, /): ")

        try:
            cislo2 = float(input("Zadajte druhe cislo: "))
        except ValueError:
            print("Písmená sa tam nesmú zadávať, zadajte číslo.")
            continue

        try:
            if operacia == "+":
                vysledok = cislo1 + cislo2
                raise CustomException("Jedná sa o vyvolanú výnimku")
            elif operacia == "-":
                vysledok = cislo1 - cislo2
                raise CustomException("Jedná sa o vyvolanú výnimku")
            elif operacia == "*":
                vysledok = cislo1 * cislo2
                raise CustomException("Jedná sa o vyvolanú výnimku")
            elif operacia == "/":
                try:
                    vysledok = cislo1 / cislo2
                except ZeroDivisionError:
                    print("Chcel si deliť nulou a to nejde.")
                    continue
            else:
                print("Neplatná operácia.")
                continue

            print(f"Vysledok: {vysledok}")

        except CustomException as e:
            print(e)


# Spustenie kalkulačky
kalkulacka()