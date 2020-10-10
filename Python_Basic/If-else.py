n = input("Nhập số: ")
if int(n) >= 0:
    print (n, "là số dưong")
else:
    print (n, "là số âm")

# Nhập vào một số kiểm tra xem là số âm hay số dương
print ("**************************")
num = float(input("Nhập một số: "))
if num >= 0:
    if num == 0:
        print (num, "là số không")
    else:
        print (num, "là số dương")
else:
    print (num, "là số âm")

# Tính tổng tất cả các chữ số trong danh sách A
print ("*************************")
A = [1,3,5,9,11,2,6,8,10]
tong =0   
for a in A:
    tong = tong + a
print ("Tổng của A: ", tong)

# In ra một chuỗi
print ("*************************")
chuoi = ["bố", "mẹ", "em"]
for tu in chuoi:
    print ("anh yêu", tu)
    
# Lặp qua index của mảng
print ("************************")
chuoi = ["bố", "mẹ", "em"]
for tu in range(len(chuoi)):
    print ("anh yêu", chuoi[tu])

# Ví dụ for and range
print ("***********************")
print ("for loop example")
for x in range(3,6): # x= 3,4,5,6
    print ("Value of x: ", x)
    print ("x^2= ",x*x)

# Ví dụ for duyệt trên các phàn tử của mảng
print ("***********************")
print ("Example for aray")
names = ["Tom", "Jerry", "Donald"]
for ten in names:
    print ("Name is: ", ten)

