class CustomException(Exception):
    pass

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
        raise CustomException("Jedná sa o vyvolanú výnimku")
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

try:
    print(f"Vysledok: {kalkulacka()}")
except CustomException as e:
    print(e)