
a = open("inpd3.txt")
lines = a.readlines()
board = []
for line in lines:
    l = line.strip().split()
    x = l[0]
    #print(x)
    k = list(x)
    #print(k)
    board.append(k)

largo = len(board)
ancho=len(board[0])

print(ancho, largo)

def scan(x,y,count, tablero):
    salto_x = 3
    salto_y = 1
    if x + salto_x > 30:
        x = (x+salto_x)%31
        #print(f"x:{x}")
    else:
        x += salto_x
    if y + salto_y > 322:
        print(f"final count: {count}")
        return count
    else:
        y +=salto_y
        pos = tablero[y][x]
        if pos == "#":
            count += 1
            print(f"---> x:{x} - y:{y}")
            print(count)
        else:
            print(f"x:{x} - y:{y}")    
        scan(x,y,count,tablero)    
n = scan(0,0,0,board)
print("$$$$$$$$$","\n",n)

