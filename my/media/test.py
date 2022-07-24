def Factor(n): # объявление функции
    Ans = []
    d = 2
    while d * d <= n: # пока счетчик меньше или равно sqrt(n)
        if n % d == 0:
            Ans.append(d) # сохраняем множитель
            n //= d # делим n на множитель
        else:
            d += 1
    if n > 1:
        Ans.append(n) # добавляем последний множитель в массив, если это не 1
    return Ans

n = int(input())
print(Factor(n))
