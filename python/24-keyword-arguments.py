def balance(cost, balance = 50): # balance is a default variable
    wallet =  f"${balance - cost}"
    if wallet < 0:
        return "You can not afford this"
    else:
        return wallet
cost = float(input("How much is the item? "))       
balance(balance = "70", cost = cost) # By using Keywords you can put arguments in any order

print("1","2","3","4","5","6", sep="-") # The sep keyword seperates each string with the chosen str