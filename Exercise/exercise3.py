from collections import Counter
n = input("Nhập chuỗi: ")
dem = Counter(n)
print(dem)
print("kí tự xuất hiện nhiều nhất ", dem.most_common(1))
