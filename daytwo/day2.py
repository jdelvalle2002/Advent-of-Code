c = 0
a = open("inpd2.txt")
lines = a.readlines()
# 13-14 f: ffffffffnfffvv
for i in lines:
    l=i.strip().split(":")
    part1, clave =  l[0],l[1]
    part1 = part1.split(" ")
    nros, letra = part1[0],part1[1]
    nros = nros.split("-")
    nros = list(map(lambda x: int(x), nros))
    contar = clave.count(letra)
    if contar in list(range(nros[0],nros[1]+1)):
        c += 1

print("############")
print(c)
print("@@@@@@@@@@@@")