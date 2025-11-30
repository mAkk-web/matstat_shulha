# 1. Вхідні дані
n_str = input()
k, m = map(int, input().split())

# 2. Переводимо вхідне число в десяткову систему (однією командою)
num = int(n_str, k)

# 3. Обробка нуля і знака (щоб працювати з додатним числом)
if num == 0:
    print(0)
else:
    sign = '-' if num < 0 else ''
    num = abs(num)
    
    # 4. Переводимо в нову систему M
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    
    while num > 0:
        res = alphabet[num % m] + res  # Додаємо цифру (остачу) на початок
        num //= m                      # Зменшуємо число (ділимо націло)
        
    print(sign + res)