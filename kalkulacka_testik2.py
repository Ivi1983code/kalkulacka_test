def kalkulacka():
    try:
        cislo1 = float(input("Zadajte prve cislo: "))
    except ValueError:
        print("Písmená sa tam nesmú zadávať, zadajte číslo.")
        return None

    operacia = input("Zadajte operaciu (+, -, *, /): ")

    try:
        cislo2 = float(input("Zadajte druhe cislo: "))
    except ValueError:
        print("Písmená sa tam nesmú zadávať, zadajte číslo.")
        return None

    if operacia == "+":
        vysledok = cislo1 + cislo2
    elif operacia == "-":
        vysledok = cislo1 - cislo2
    elif operacia == "*":
        vysledok = cislo1 * cislo2
    elif operacia == "/":
        try:
            vysledok = cislo1 / cislo2
        except ZeroDivisionError:
            print("Chcel si deliť nulou a to nejde.")
            return None
    else:
        print("Neplatná operácia.")
        return None

    return vysledok

print(f"Vysledok: {kalkulacka()}")
