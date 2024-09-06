name = ("Dr. Csató Csege Károly")

titulusok = ["Prof.", "Sir", "Dr."]
titulus = ""
for t in titulusok:
    if t in name:
        szóköz_helye = name.find(" ")
        titulus = name[:szóköz_helye] + " "
        name = name[szóköz_helye +1:]
        break


# titulus = ""
# if "Dr." in name:
#     szóköz_helye = name.find(" ")
#     titulus = name[:szóköz_helye] + " "
#     name = name[szóköz_helye +1:]

#print(name)
#lista = name.split(" ")
#print(lista[0])

#vezetek, kereszt1, kereszt2 = name.split(" ")
#print(kereszt2)

# print(name.split(" ")[0])
# print(name.split()[1])

# c = 0
# for karakter in name:
#     if karakter != " ":
#         c+=1
#     else:
#         print(name[:c])
#         break

szóköz_helye = name.find(" ")
vezetéknév = name[:szóköz_helye]
keresztknév = name[szóköz_helye+1:]

print(keresztknév, vezetéknév, sep=', ')
#angol_név = keresztknév + ", " + vezetéknév
angol_név = f"{keresztknév} + {vezetéknév}"
#angol_név = angol_név.replace(" ", ", ")
print(angol_név)
teljes_név = f"{titulus}{angol_név}"
print(teljes_név)


