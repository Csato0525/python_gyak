név = "         anyáD faszÁT    "
név = név.strip()
név = név.lower()


title_név = ""
for i in range(len(név)):
    if i == 0 or név[i-1] == " ":
        title_név += név[i].upper()
    else:
        title_név += név[i].lower()

print(név)
print(title_név)
print(title_név[::-1])








#print(név.strip().title())