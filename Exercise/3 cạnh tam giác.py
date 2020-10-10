from math import *
print ("======BẤT ĐĂNG THỨC TAM GIÁC======")
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        print ("Đây là 3 cạnh của tam giác")
        C = a + b + c
        S = sqrt(C*(C-a) * (C-b) * (C-c))
        print ("Chu vi tam giác là: ", C)
        print ("Diện tích tam giác là: ", S)
    else:
        print("Đây không phải là 3 cạnh tam giác")
else:
    print ("Bạn nhập cạnh sai rồi") 