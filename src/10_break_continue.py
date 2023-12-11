sayac = 0

while True:
    print(sayac)
    sayac += 1
    if sayac == 5:
        break  # Döngüyü sonlandır
# Output:
# 0
# 1
# 2
# 3
# 4

for i in range(5):
    if i % 2 == 0:
        continue  # Döngüyü bir sonraki adıma atla
    print(i)

# Output:
# 1
# 3
