# n = int(input("Entrez la valeur de n  : "))

# i = 0 

# def drw_tapis():
#     for i in range(n):
#         if i == 0 or i == n :
#             print('+',"-" * n,'+')
#         else :
#             if n >= n:
#                 print("|" + "#" * n-1 + " " + "|")
#             else:
#                 n-=1
#                 print("|" + "#" * n + " " + "#" *(-i+n) + "|")

# drw_tapis()





n = int(input("Entrez la valeur de n : "))

def drw_tapis(n):
    print("+" + "-" * n + "+") 
    for i in range(n):
        ligne = "|"
        for j in range(n):
            if j == n - i - 1: 
                ligne += " "
            else:
                ligne += "#"
        ligne += "|"
        print(ligne)
    print("+" + "-" * n + "+")

drw_tapis(n)
