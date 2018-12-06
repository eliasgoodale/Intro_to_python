opt_dany = "Dany"
opt_abr = "DHTFHNUQARFMQMKGSPRLRSKBCMD"
opt_fullname = "Daenerys of the House Targaryen, the First of Her Name, The Unburnt, Queen of the Andals, the Rhoynar and the First Men, Queen of Meereen, Khaleesi of the Great Grass Sea, Protector of the Realm, Lady Regnant of the Seven Kingdoms, Breaker of Chains and Mother of Dragons"

switch = input("Who goes there? ")

if (switch == opt_dany):
    print("Dany who?")
elif (switch == opt_abr or switch == opt_fullname):
    print("Welcome, Daenerys")
else:
    print("Move along, now.")
    