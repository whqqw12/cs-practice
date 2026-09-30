porog = int(input())
n = int(input())
k = 0
er = 0
pr = 0
mx = 0
cr = 0
summ = 0
for i in range(n):
    pokazanie = input()
    if pokazanie == 'error':
        er += 1
    else:
        k += 1
        summ += float(pokazanie)
    if (pokazanie != 'error') and float(pokazanie) > porog:
        pr += 1
    if (pokazanie != 'error'):
        if float(pokazanie) > mx:
            mx = float(pokazanie)
print(n,er,pr,f"{mx:.1f}",f"{summ/k:.1f}")
    

