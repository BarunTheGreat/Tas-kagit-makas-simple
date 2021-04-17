
import random
f = 0
g = 0
print("3 yapan kazanır")
while True :
    a = ['Kagit','Tas','Makas']
    b = random.choice(a)
    c = input("Tas Kagit Makas: ")
    c = c.lower()
    if c == 'tas':
        if b == 'Tas':
            print("Tas. Berabere!")
        elif b == 'Kagit':
            print("Kagit. Kaybettin!")
            f = f + 1
        else:
            print("Makas. Kazandin!")
            g = g + 1
    elif c == 'kagit':
        if b == 'Tas':
            print("Tas. Kazandin!")
            g = g + 1
        elif b == 'Kagit':
            print("Kagit. Berabere!")
        else:
            print("Makas. Kaybettin")
            f = f + 1
    elif c == 'makas':
        if b == 'Tas':
            print("Tas. Kaybettin!")
            f = f + 1
        elif b == 'Kagit':
            print("Kagit. Kazandin!")
            g = g + 1
        else:
            print("Makas. Berabere!")
    else:
        print("Lütfen tas kagit veya makas girisi yapiniz...")
        continue
    print("Bilgisayar ",f,"-",g," Sen")
    if (g == 3) or ( f == 3 ):
        break
    
if f == 3:
    print("Kaybettin :)")
else:
    print("Kazandin :(")