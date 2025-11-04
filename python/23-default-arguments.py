def balance(cost, balance = 50): # balance is a default variable
    wallet =  f"${balance - cost}"
    if wallet < 0:
        return "You can not afford this"
    else:
        return wallet

cost = float(input("How much is the item? "))

balance(cost) # 1 variable as balance is a default argument
balance(cost, 60) # Uses 60 rather than 50