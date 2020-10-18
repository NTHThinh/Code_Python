# Bằng cách tạo một dictionary, với cặp key:valuetương ứng là kí tự có trong chuỗi và số lần xuất hiện kí tự đó.
# Câu điều kiện if else sẽ kiểm tra nếu i đã có trong count rồi thì mà còn lặp lại nữa thì sẽ tăng i lên một đơn vị, còn nếu chưa có trong count thì sẽ gán cho i=1.
s = input("Nhập chuỗi: ")
count = {}

for kytu in s:
    if kytu in count:
      count[kytu] += 1
    else:
       count[kytu] = 1
for kytu in sorted(count, key=count.get, reverse=False):        
      print(kytu, count[kytu])