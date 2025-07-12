import re


# print("Ex 1")

s = '39801 356 2102 1111'

pattern = r'(\d{3}) (\d{2})'

match = re.search(pattern, s)

print(match.group(1, 2), match.span())

# print("Ex 2")

# reg = re.compile("([0-9]+)\.([0-9]+)")

# s = 'pi vaut 3.14'

# res = reg.search('pi vaut 3.14')

# print(res.start(), res.end())

# print(res.group(0), res.group(1))

# print("Ex 3")

# pattern = "^a..\d t$"

# str = input("str: ")
# res = re.match(pattern, str)

# if res:
#     print('ok')
# else:
#     print('ko')

# print("Ex 4")

# pattern = "\s(\d{2})\s"
# s = "toto 12 et 25 et 356 et 45 et 1000"
# res = re.findall(pattern, s)

# print(res)
