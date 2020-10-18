n = input("Nhập chuỗi: ")
a = list(n)
for i in range(len(n)):
    if i % 2 == 0:
        print(a[i].upper(), end='')
    if i % 2 == 1:
        print(a[i].lower(), end='')