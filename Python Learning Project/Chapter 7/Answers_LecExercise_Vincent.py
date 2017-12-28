months = "JanFebMarAprMayJunJulAugSepOctNovDec"

userIn = int(input("Enter a month number : "))

print(months[(userIn - 1)*3 : userIn * 3], end = "")