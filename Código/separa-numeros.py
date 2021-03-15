x = []
neg = 0
pos = 0
cpos = 0
cneg = 0

for i in range(0,5,1):
    y = int(input("Digite um número: "))
    x+= [y]

for i in range(0,5,1):
    if(x[i]<0):
        neg += x[i]
        cneg += 1

    else:
        pos += x[i]
        cpos += 1

medn = neg/cneg
medp = pos/cpos
dif = (neg*-1)+pos
print("Números:",x)
print("Soma dos número negativos:",neg)
print("Soma dos números positivos:",pos)
print("Média dos número negativos:",medn)
print("Média dos números positivos:",medp)
print("Diferença entre os números positivos e negativos:",dif)