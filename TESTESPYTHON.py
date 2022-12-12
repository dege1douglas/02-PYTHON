#TESTESPYTHON

''' ÁREA DE TESTES - PYTHON 
DOUGLAS GOMES - 2M'''

print( ) 
n1 = int(input("NUMERADOR"))
n2 = int(input("DENOMINADOR"))


div = 0
if n1>n2:
    for i in range(n1, 0, -1):
        if n1%i==0 and n2%i==0:
            div=1
            print("Máximo divisor comum da fração:",i)            
            simpl1 = n1/i
            simple1 = n2/i
            break
else:
    for j in range(n2, 0, -1):
        if n1%j==0 and n2%1==0:
            div = j
            print("Máximo divisor comum da fração:",j)            
            simpl1 = n1/j
            simple1 = n2/j
            break
print('fração===========================> ',n1,'//',n2)
print('fração simplificada ao máx. =====> ',simpl1,'//',simple1)


#for variavel(x,y,z,y,e) in range(inicio, fim, passo)