def cincobit (n):
    m = "0"
    while(len(n) != 5):
        n = m + n
    return n

def immediate (n, sinal):
    m = "0"
    while(len(n) != 12):
        n = m + n
    if(sinal==1):
        n_ = ''.join('1' if bit == '0' else '0' for bit in n)
        return n_
    return n

arquivo = open("entrada.asm", "r")
linha = arquivo.readline()

while(linha != ""):
    if(linha[0]=='a'):
        if(linha[3]=='i'): #addi
            x=bin(int(linha[6:7]))[2:]
            y=bin(int(linha[10:11]))[2:]
            if(linha[13]=='-'):
                z=bin(int(linha[13:])+1)[3:]
                sinal=1
                
            else:
                z=bin(int(linha[13:]))[2:]
                sinal=0
            x = cincobit(x)
            y = cincobit(y)
            z = immediate(z, sinal)
            s = "{}{}000{}0010011".format(z, y, x)
            print(s)
            f = open("entrada.asm", "a")
            f.write("\n{}".format(s))
            f.close()

        else: #add
            x=bin(int(linha[5:6]))[2:]
            y=bin(int(linha[9:10]))[2:]
            z=bin(int(linha[13:14]))[2:]
            x = cincobit(x)
            y = cincobit(y)
            z = cincobit(z)
            s = "0000000{}{}000{}0110011".format(z, y, x)
            print(s)
            f = open("entrada.asm", "a")
            f.write("\n{}".format(s))
            f.close()

    elif linha[0] == 'b': #bne
        x=bin(int(linha[5:6]))[2:]
        l = linha.find('(')
        if(linha[9]=='-'):
            z=bin(int(linha[9:l]))[3:]
            sinal=1

        else:
            z=bin(int(linha[9:l]))[2:]
            sinal=0
        y=bin(int(linha[l+2:l+3]))[2:]
        x = cincobit(x)
        y = cincobit(y)
        z = immediate(z, sinal)
        s = "{}{}{}001{}1100011".format(z[0:7], x, y, z[7:12])
        print(s)
        f = open("entrada.asm", "a")
        f.write("\n{}".format(s))
        f.close()

    elif linha[0] == 's':
        if linha[1] == 'w': #sw
            x=bin(int(linha[4:5]))[2:]
            l = linha.find('(')
            if(linha[7]=='-'):
                z=bin(int(linha[8:l]))[3:]
                sinal=1
            else:
                z=bin(int(linha[8:l]))[2:]
                sinal=0
            y=bin(int(linha[l+2:l+3]))[2:]
            x = cincobit(x)
            y = cincobit(y)
            z = immediate(z, sinal)
            s = "{}{}{}010{}0100011".format(z[0:7], x, y, z[7:12])
            print(s)
            f = open("entrada.asm", "a")
            f.write("\n{}".format(s))
            f.close()

        else: #sll
            x=bin(int(linha[5:6]))[2:]
            y=bin(int(linha[9:10]))[2:]
            z=bin(int(linha[13:14]))[2:]
            x = cincobit(x)
            y = cincobit(y)
            z = cincobit(z)
            s = "0000000{}{}001{}0110011".format(z, y, x)
            print(s)
            f = open("entrada.asm", "a")
            f.write("\n{}".format(s))
            f.close()

    elif linha[0] == 'l': #lw
        x=bin(int(linha[4:5]))[2:]
        y=bin(int(linha[8:9]))[2:]
        if(linha[11]=='-'):
            z=bin(int(linha[11:])+1)[3:]
            sinal=1
        else:
            z=bin(int(linha[11:]))[3:]
            sinal=0
        x = cincobit(x)
        y = cincobit(y)
        z = immediate(z, sinal)
        s = "{}{}010{}0000011".format(z, y, x)
        print(s)
        f = open("entrada.asm", "a")
        f.write("\n{}".format(s))
        f.close()

    elif linha[0] == 'x': #xor
        x=bin(int(linha[5:6]))[2:]
        y=bin(int(linha[9:10]))[2:]
        z=bin(int(linha[13:14]))[2:]
        x = cincobit(x)
        y = cincobit(y)
        z = cincobit(z)
        s = "0000000{}{}100{}0110011".format(z, y, x)
        print(s)
        f = open("entrada.asm", "a")
        f.write("\n{}".format(s))
        f.close()
        
    linha = arquivo.readline()
arquivo.close()
