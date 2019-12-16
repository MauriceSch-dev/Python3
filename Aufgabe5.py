bank_balance = 100
interest = 1.05
costs = 2
for x in range(10):
    bank_balance=(bank_balance*interest) - costs
    print("Nach " + str(x) + "Jahr(en): " + str(bank_balance))