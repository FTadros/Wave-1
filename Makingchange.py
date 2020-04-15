cents = input("Please input the change in cents: ") #1234
cents = int(cents)

toonies = cents // 200
cents %= 200

loonies = cents // 100
cents %= 100

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

print(toonies, "toonies", loonies, "loonies", quarters, "quarters", dimes, "dimes", nickels, "nickels and ", cents, "cents")
