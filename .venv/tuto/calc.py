

print("Effectuons une opération entre deux nombres")

a = input("1ère valeur: ").strip()
b = input("2nd valeur : ").strip()
op = input("opérateur (+ - * /): ").strip()

s = a + op + b
r = eval(s)

print(f'opération : {a} {op} {b} = {r}\n\n')

