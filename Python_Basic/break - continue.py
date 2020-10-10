# Lệnh break trong vòng lặp
print ("************************")
x = int(input("nhap mot so: "))
while (x < 15):
    print ("-----------------\n")
    print ("x =", x)
    if (x == 10):
        break
    x = x + 1
    print (" x after + 1= ", x)

# Ví dụ 2 về break
print ("************************")
var = 99
while var > 0:
    print (" Gía trị của biến hiện tại: ", var)
    var = var - 2
    if var == 5:
        break

# Ví dụ lệnh continue 
print ("************************")
for letter in 'PYTHON':
    if letter == "H":
        continue
    print ("Ký tự hiện tại: ", letter)

# Ví dụ 2 lệnh continue
print ("************************")
x = int(input("Nhập một số: "))
while x < 7:
    print ("-------------\n")
    print ("x", x)
    if (x % 2 == 0):
        x = x + 1
        continue
    else:
        x = x + 1
        print (" x after + 1=", x)
        