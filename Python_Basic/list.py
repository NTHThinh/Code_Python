thislist = ["apple", "banana", "cherry"]
if "banana" in thislist:
  print("Yes")
else:
	print ("No")

# Phạm vi chỉ số chỉ định
print ("*******************")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[0:4])

# Thay đổi giá trị mặt hàng
print ("********************")
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Copy một danh sách
print("**********************")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
mylist.append("cat")
mylist.insert(2, "dog")
print("Danh sách trước khi copy: ",thislist)
print("Danh sách sau khi copy: ", mylist)

# Join two list
print("***********************")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# append list 2 into list 1
print("***********************")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

