from math import pi
print ("VIẾT CHƯƠNG TRÌNH TÍNH DIỆN TÍCH VÀ CHU VI HÌNH TRÒN")
r = int(input("Nhập r: "))
if r > 0 :
    S = pi *r**2
    C = 2 *pi *r
    print ("Diện tích hình tròn là: ", S)
    print ("Chu vi hình tròn là: ", C)
else:
    print ("Bạn nhập bán kính sai rồi: ")