import sys


def test_age(age):
    if int(age) >= 18:
        print('Bienvenue, tu as l\'âge requis')
    sys.exit('Désolé âge insuffisant')


# sys.stdout.write('Entrez votre âge: \r\t\t\t')
# for age in sys.stdin:
#     test_age(age)


# age = int(input('Entrez votre âge: '))
# test_age(age)

l = len(sys.argv)

print(f'Nombre d\'argument(s) {l}')

print(f'Nom du source : {sys.argv[0]}')

somme = 0

print("Liste des nombres : ", end=" ")
for a in range(1, l):
    print(sys.argv[a], end=" ")
    somme += int(sys.argv[a])

print(f'\nLa somme des nombres est {somme}')
