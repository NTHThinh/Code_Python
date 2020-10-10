# Tạo và in ra một từ điển
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
    
# Thay đổi bằng từ khóa 
print("*********************")
dictCar = {
    "brand": "Honda",
    "model": "Honda Civic",
    "year": 1972
}
print("Trước khi thay đổi: ", dictCar)

dictCar["year"] = 2020
print(" Sau khai thay đổi: ", dictCar)

# DUYỆT QUA CÁC PHẦN TỬ CỦA KHÓA
print("**********************")
dictCar = {
    "brand": "BMW",
    "model": "BMW I8",
    "year" : "1960"
}
for x in dictCar:
    print(x, ":", dictCar.get(x))

# Kiểm tra nếu một key có tồn tại
print("***********************")
dictCar = {
    "brand": "BMW",
    "model": "BMW I8",
    "year" : 1960,
    "price": 1000000000
}
for y in dictCar:
    print(y, ":", dictCar.get(y)) # in ra các phần tử của khóa
x = str(input("nhập từ khóa: "))
if x in dictCar:
    print ("khóa " + x + " có tồn tại")
else:
    print ("khóa " + x + " không tồn tại")

# Thêm các item vào dictionary
print("**************************")
dictCar = {
    "brand": "Honda",
    "model": "Honda Civic",
    "year": 1972,
    "manufacturing": "Thái Lan",
    "price": 20000000
}
print ("Mảng trước khi in: ")
for x in dictCar: # duyệt vòng lặp for để in ra keys và value của dictionary
    print( "-",x, ":", dictCar.get(x))
print ("Độ dài của dic: ", len(dictCar))
dictCar["color"] = "yellow" # add item vào mảng
print("---------------------------")
print("Mảng sau khi in: ")
for x in dictCar:
    print( "-",x, ":", dictCar.get(x))
print ("Độ dài của dic: ", len(dictCar))

# Dictionary lồng nhau
print("****************************************")
myFamily = {
    "father" : {
        "name": "A",
        "age" : 50,
        "giới tính" : "nam"    
    },
    "mother" : {
        "name" : "B",
        "age" : 40,
        "giới tính" : "nữ"
    },
    "son" : {
        "name" : "C",
        "age" : 18,
        "giới tính" : "nam"
    }
}
for x in myFamily:
    print (x, ":", myFamily.get(x))

    
    