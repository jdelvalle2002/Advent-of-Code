l = open("inputd2.txt")
lista = l.readlines()
lista = list(map(lambda x: x.strip(), lista))
new_l = list(map(int, lista))
l.close()
#print(new_l)
for i in new_l:
    for j in new_l:
        for k in new_l:
            if i + j + k == 2020:
                resu = i*j*k
                break
print("############")
print(resu)
print("@@@@@@@@@@@@")