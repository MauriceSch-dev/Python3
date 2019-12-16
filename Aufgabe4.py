price = 500
while True:
    discount_input = input("Wie hoch ist der Rabatt?")
    discount = price / 100 * float(discount_input)
    price = price - discount
    print ("Neuer Preis: " + str(price))