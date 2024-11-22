datne = open('pirkums.txt')
sum=0
for rinda in datne:
    sarakstaDati = rinda.split(" ")
    nosaukums=sarakstaDati[0]
    print('produkta nosaukums=', nosaukums)
    cena=sarakstaDati[1]
    print('cena ir ', cena)
    daudzums=sarakstaDati[2]
    print('daudzums ir',daudzums)
    dati = rinda.split(" ")
    sum += int(sarakstaDati[1])*int(sarakstaDati[2])
print("sum = ", sum)
print(datne.read())
datne.close()
