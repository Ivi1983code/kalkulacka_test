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
        vysledok = cislo1 / cislo2

    return  vysledok

print(f"Vysledok:{kalkulacka()}")