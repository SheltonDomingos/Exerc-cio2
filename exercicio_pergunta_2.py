
a = 0
b = 1

x = int(input('Digite um número: '))

while a < x:
    print(a, end=',')
    a, b = b, a + b
    
if a == x:
    x = True

else:
    a < x
    a = False

if a == False:
    print( x, end=' --> ' 'Não pertence a sequência.')
else:
    print( a, end=' --> ' 'pertence a sequencia.')
