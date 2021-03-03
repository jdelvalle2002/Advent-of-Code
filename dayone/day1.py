l = open("inputd1.txt")
lista = l.readlines()
lista = list(map(lambda x: x.strip(), lista))
new_l = list(map(int, lista))
l.close()
#print(new_l)
for i in new_l:
    for j in new_l:
        if i + j == 2020:
            resu = i*j
            break
print("############")
print(resu)
print("@@@@@@@@@@@@")