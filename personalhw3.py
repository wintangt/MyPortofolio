#Soal Nomor 1
print("="*50)
print("Soal Nomor Satu")
for a in range(1,6): #1,2,3,4,5
    for b in range(1, a+1): 
        print((a), end=" ")
    print()

#Soal Nomor 2
print("="*50)
print("Soal Nomor Dua")
for c in range(1,6):
    for d in range(1, c+1):
        print(d, end=" ")
    print()

#Soal Nomor 3
print("="*50)
print("Soal Nomor Tiga")
for e in range(4,-1,-1):
    for f in range(5, e,-1):
        print(f,end=" ")
    print()

#Soal Nomor 4
print("="*50)
print("Soal Nomor Empat")
for g in range(1,6):
    for h in range(g,6):
        print(g,end=" ")
    print()

#Soal Nomor 5
print("="*50)
print("Soal Nomor Lima")
for i in range(6,1,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()
print("="*50)

#Soal Nomor 6
print("="*50)
print("Soal Nomor Enam")
for k in range(1,6):
    for l in range(5, k-1,-1):
        print(l, end=" ")
    print()
print("="*50)

#Soal Nomor 7
print("="*50)
print("Soal Nomor Tujuh")
n = 9
for a1 in range(1, (n+1)//2 + 1): 
    for a2 in range((n+1)//2 - a1):
        print(" ", end = "")
    for a3 in range((a1*2)-1):
        print("*", end = "")
    print()

for a1 in range((n+1)//2 + 1, n + 1): 
    for a2 in range(a1 - (n+1)//2):
        print(" ", end = "")
    for a3 in range((n+1 - a1)*2 - 1):
        print("*", end = "")
    print()