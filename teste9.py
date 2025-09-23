def isPrimo(n):
    count = 0
    if n < 1:
        return False
    elif n == 1:
        return True
    
    for i in range(n+1):
        if n % (i + 1) == 0:
            count +=1
            
    if count == 2:
        return True
    else: 
        return False
    
n = 4
if isPrimo(n):
    print(f'{n} é primo')
else:
    print(f'{n} nao é primo')