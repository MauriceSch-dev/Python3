int_ZahlA = int(input("I'm a calculator! Please give me 2 numbers and a arithmetic operation! First Number?"))
int_ZahlB = int(input("Second Number?"))
str_operator = (input("Operator?"))
if str_operator == "+":
    int_Ergebnis = int_ZahlA + int_ZahlB
elif str_operator == "-":
     int_Ergebnis = int_ZahlA - int_ZahlB
elif str_operator == "*":
     int_Ergebnis = int_ZahlA*int_ZahlB
elif str_operator == "/":
     int_Ergebnis = int_ZahlA/int_ZahlB
else:
    print("Don't know the operation " + str_operator)
    int_Ergebnis = "ERROR"

print(int_Ergebnis)