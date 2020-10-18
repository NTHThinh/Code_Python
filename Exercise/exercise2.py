
s = input("Nhập chuỗi: ")
# Chuyển chuỗi s thành list
s = s.split()
# Hàm reverse chỉ có tác dụng vs list và đảo ngược
s.reverse()
# join(s) chuyển list thành chuỗi lại
print(" ".join(s))