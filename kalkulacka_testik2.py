def kalkulacka():
    cislo1 = float(input("Zadajte prve cislo: "))
    operacia = input("Zadajte operaciu (+, -, *, /): ")
    cislo2 = float(input("Zadajte druhe cislo: "))

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