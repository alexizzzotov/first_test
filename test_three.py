s = (1,2,3,4,5, 'hi')
summa = 0
for i in s:
    try:
        summa+=i
    except:
        pass
print(summa)
