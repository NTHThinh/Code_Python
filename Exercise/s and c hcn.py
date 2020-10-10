print("======CHƯƠNG TRÌNH TÍNH CHU VI VÀ DIỆN TÍCH HCN======")
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
if a > 0 and b > 0:
    S = a * b
    C = (a + b)*2
    print (" Diện tích hcn là: ", S)
    print (" Chu vi hcn là: ", C)
else:
    print (" Cạnh phải lớn hơn 0. Vui lòng nhập lại:")
