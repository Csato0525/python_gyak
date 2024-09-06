f = open("szallitasok.txt",encoding='UTF-8')
sorok = f.readlines()
f.close()
#ASCII

data = []
for sor in sorok:
    data.append(sor.strip().split(" "))

#print(data[1][1])

for sor in data:
    if sor[0] == "Kanatima":
        print(sor)

leghosszab = 0
elso = data[0]
for d in data:
    if int(d[-1]) >= leghosszab: # utolsó első = nélkül
        leghosszab = int(d[-1])
        elso = d
print(d)

#több elem
for d in data:
    if int(d[-1]) == leghosszab:
        print(d)
        break

for d in data:
    minősítés = ""
    if 10 <= int(d[-1]) and int(d[-1]) <= 20:
        minősítés = "Megfelelő"
    elif int(d[-1]) < 10:
        minősítés = "Lassú"
    elif int(d[-1]) > 20:
        minősítés = "Gyors"



for d in data:
    minősítés = "Gyors"
    if int(d[-1]) < 10:
        minősítés = "Lassú"
    elif int(d[-1]) < 20:
        minősítés = "Megfelelő"

print([d[0], d[1], minősítés])

#task4
for d in data:
    if "2012.06." == d[3][:8] and d[1] == "Bundország":
        print(d)

#task5
for d in data:
    if d[2][:4] != d[3][:4]:
        print(d)
        break
