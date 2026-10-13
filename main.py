# 6-m
for i in range(0, 51, 5):
    if i % 5 == 0:
        print(i, end=" ")


# 13-m
text = "Men Python dasturlash tilini o'rganyapman b"

sozlar = text.split()

print("Sozlar soni:", len(sozlar))


# 15-m
numbers = [4, 7, 12, 15, 20, 9, 8]

juft_sonlar = []

for son in numbers:
    if son % 2 == 0:
        juft_sonlar.append(son)

print(juft_sonlar)


# 28-m
products = {
    "non": 4000,
    "sut": 8000,
    "shakar": 12000,
    "guruch": 18000
}

for nomi, narxi in products.items():
    if narxi > 10000:
        print(f"{nomi}: {narxi}")




# 37-m
ism = input("Ismingizni kiriting: ")

def ism_uzunlgi(ism):
    return len(ism)

print("Ismingiz soni: ",ism_uzunlgi(ism))


# 43-m
numbers = [10, 20, 30, 40, 50]

def elemetlar_soni(numbers):
    return len(numbers)

print(elemetlar_soni(numbers))
