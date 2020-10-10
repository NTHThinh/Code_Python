count = 0 
while (count < 10):
    print ("The count is :" + str(count))
    count = count + 1


# Tăng dần count lên và in giá trị của nó cho đến khi giá tri này nhỏ hơn 10
count = 0
n = 0
while (count <= 10):
    print ('so thu ', n , 'la:', count)
    n = n + 1
    count = count + 1
print ('Good bye') 

# Sử dụng while tính tổng các số
n = input()
sum = 0
i = 1
print ('Nhập n:',n)
while i <= int(n):
    sum =sum + i
    i = i + 1
print ('Sum is: ' + str(sum))

# Kết hợp while vs else
# đếm và in các số nhỏ hơn
n = input()
while i < 2:
    print (n + " nhỏ hơn 2")
    n = n + 1
else:
    print (n + " không nhỏ hơn 2")