#Tạo ra một hàm trong python
"""
def function():
    print ("hello world")
function()
"""

# Truyền tham số cho hàm
"""
def function(name):
    print ("hello " + name )
function("thinh")
"""

# viết hàm hiển thị ra màn hình các số từ 1- 10
"""
def show():
    for i in range (1, 100):
        print (i, end=" ") # end="" có nghĩa là sử dụng hàm print và khồng xuống dòng
show()
"""

# Hàm trả về tổng của một list
"""
def sum_of_list(list):
    count = 0
    for i in list:
        count += i
    return count
print(sum_of_list([1,2,3]))
print(sum_of_list([3,4,5]))
print(sum_of_list([6,7,8]))
"""

def square(x):
    return x*x
print (square(4))

def multiply (x,y = 0):
    print("value of x=", x)
    print("value of y=", y)
    return(x,y)
print(multiply(x=4, y=2))