'''
try:
    open('info.txt','r')
except:
    print('Tādas datnes nav')
    datne = open('info.txt', 'w')

def nolasaDrukaDati():
    datne = open('info.txt')
    dati = datne.readline()
    rinda = dati.split(" ")
    print(rinda)
nolasaDrukaDati()

menesi = ['janvāris', '31', 'februāris', '28', 'aprīlis', '30']
with open('info.txt', 'w') as datne:
    for vards in menesi:
        print(vards)
        #datne.write(vards)
        #datne.write(" ")
print("nolasu uz izrukāju ierakstīto, atverot ar w")
nolasaDrukaDati()
'''
try:
    open("info.txt","w")
except:
    print("Tadas datnes nav,izveidosim")
    datne= open("info.txt","w") 





def nolasaDrukaDatni():
    datne = open("info.txt")
    dati = datne.readline()
    rinda = dati.split(" ")
    print(rinda)
nolasaDrukaDatni()

menesi = ['janvaris', '31', 'februaris', '28', 'aprilis', '30']
with open('info.txt', 'w') as datne:
    for vards in menesi:
        datne.write(vards)
        datne.write(" ")
print('nolasu u n izdrukaju,atverot ar w')
nolasaDrukaDatni() 

open('info.txt', 'a')
print('\nnolasu un izdrukāju ierakstīju, atverot a')
nolasaDrukaDatni() 

open('info.txt','w')
print("\nnolasu un izdrukāju otrreiz w")
nolasaDrukaDatni() 

datne.close()