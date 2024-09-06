# n = 5
# print(n**2)

# # for i in range(1, n+1):
# #     print(i**2, end=" ")

# lista = []
# output = ""
# for i in range(1, n+1):
#     lista.append(i**2)
#     output  += f"{i**2}\t"

# print(output)
# print(*lista)
# while True:
#     n = input("Adj meg egy pozitív számot!")
#     if not(n.isnumeric()):
#         print("Ez nem egy szám!")
#     else:
#         n = int(n)
#         if n <= 0:
#             print("Ez nem egy pozitív szám!")
#         else:
#             output = ""
#             for i in range(1, n+1):
#                 for j in range(1, n+1):
#                     #output += f"{i*j:3.0f} "
#                     output += f"{i*j}\t"
#                 output += "\n"
                            
#             print(output)
#             break
        



#x sor és y oszlopban rakni szám négyzetét
# output = ""
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         #output += f"{i*j:3.0f} "
#         output += f"{i*j}\t"
#     output += "\n"
# print(output)

# while True:
#     n = input("Adj meg egy számot!")
#     if n.upper() == "X":
#         break
#     elif not(n.isnumeric()):
#         print("Ez nem egy szám!")
#     else:
#         n = int(n)
#         if n <= 0:
#             print("Ez nem egy pozitív szám!")
#         else:
#             while True:
#                 r = input("Adj meg egy sorszamot!")
#                 if not(n.isnumeric()):
#                     print("Ez nem egy szám!")
#                 else:
#                     c = input("Adj meg egy oszlopszámot!")
#                     if not(c.isnumeric()):
#                         print("Ez nem egy szám!")
#                     else:
#                         c = int(c)
#                         if c <= 0:
#                             print("Ez nem egy pozitív szám!")
#                     c = int(c)
#                     if n <= 0:
#                         print("Ez nem egy pozitív szám!")
#                 output = ""
#                 for sor in range(1, n+1):
#                     for oszlop in range(1, m+1):
#                         output += f"{r*c}\t"
#                     output += "\n"
                                
#                 print(output)
#                 break
#         break
