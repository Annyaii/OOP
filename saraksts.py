saraksts=['viens', 'divi', 'trīs', 'pieci']
print(saraksts)
saraksts.insert(0, 'nulle')
print(saraksts)
saraksts.reverse()
print(saraksts)
saraksts.pop(3)
print(saraksts)
saraksts.remove('divi')
print(saraksts)

saraksts2=['dzeltens', 'pelēks', 'rozā']
print(saraksts2)
saraksts2.append('melns')
print(saraksts2)
saraksts2.pop(1)
print(saraksts2)

for x in saraksts:
    print(x)