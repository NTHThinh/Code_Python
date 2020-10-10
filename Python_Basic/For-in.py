# for letter in 'Python':
#     print ('Current letter :'+ letter)
    
# animals = ['dog', 'cat', 'elephant']
# for animal in animals:
#     print ("Current fruit :" + animal)

# print ("For loop example")
# names = ['Tom','Jery','Donald']
# for index in range(len(names)):
#     print("name= ", names[index])

#Viết chương trình hiển thị ra màn hình tổng từ 1 đến n
n = int(input("Nhập n: "))
sum = 0
for i in range(1, n+1):
    sum += i
print(" Sum = ", sum)

# Viết chương trình hiển thị ra tổng các số lẻ từ a đến b
print("******************")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
sum = 0
while a <= b:
    if a % 2 != 0:
        sum += a
    a += 1
print(sum)

# Nhập vào một chuỗi, viết chương trình hiển thị các kí tự khác kí tự y trong chuỗi
print("***************************")
s = str(input("Nhập vào một chuỗi: "))
for c in s:
    if c == "y":
        continue
    print("Ký tự cần in ra: ", c)

# Viết chương trình hiển thị ra tích của a vs các số từ 1 đến 10
print("*****BẢNG CỬU CHƯƠNG******")
n = int(input("Nhập cửu chương: "))
for i in range(1,10):
    if n <= 10:
        print(n, "*", i, "=", n*i)
    else:
        print("Nhập số nhỏ hơn 10")
        break


    