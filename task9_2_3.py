n_str = input()
k, m = map(int, input().split())
num = int(n_str, k)
if num == 0:
    print(0)
else:
    sign = '-' if num < 0 else ''
    num = abs(num)
    
   
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    
    while num > 0:
        res = alphabet[num % m] + res  
        num //= m                    
    print(sign + res)