
# exo 1 présence d'un caractère dans une string
# s = "Je suis une chaine de caractères de test"
# c = input(f"Quel est le caractère rechercher dans {s} : ")

# print (f"Le caractère {c} est {"présent" if c in s else "introuvable"} dans la chaine cde caractères {s}")

# exo2 Insertion d'un caractère entre chaque caractère de la chaine
# Solution 1
# ch = "gaston"
# r = ""
# for i in range(0,len(ch)-1):
#     r += ch[i] + "*"
# r += ch[i+1]
# print (r)

# Solution 2
# print('*'.join(ch))

# #exo3 Inversion de chaine
# ch = "zorglub"
# # solution 1
# ch2 = ch[::-1]
# print (ch2)
# # solution 2
# ch2 = ''.join(reversed(ch))
# print (ch2)

# exo4 Affichage pyramidal sans les x caractères déjà affichés
# ch = "abcdefghijklmnopqrstuvwxyz" * 10
# ch2 = ""
# x = 1
# while x < len(ch):
#     # nb caractères avant x
#     print(ch[:x])
#     # nb caractères après x
#     ch = ch[x:]
#     x += 1

# Palindrome
# print ("Palindrome ou pas ?")
# ch1 = input("Entrez un mot : ")
# ch2 = ''.join(reversed(ch1))
# if(ch1 == ch2):
#     print(f"{ch1} est un plaindrome")
# else: 
#     print(f"{ch1} n'est pas un plaindrome")
