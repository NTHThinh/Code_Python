n = input("nhập chuỗi: ")
my_list = []
for i in n:
    if i.isnumeric() == True:
        my_list.append(i)
print (my_list)