import sqlite3
db = sqlite3.connect('school.sql')

# xóa bảng trước rồi mới tạo
db.execute("DROP TABLE IF EXISTS student")
db.execute("CREATE TABLE student (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name VARCHAR NOT NULL)")

# thêm dữ liệu vào
db.execute("INSERT INTO student(name) VALUES ('Nguyễn Tạ Hữu Thịnh')")
db.execute("INSERT INTO student(name) VALUES ('Nguyễn Văn Rô')")
db.execute("INSERT INTO student(name) VALUES ('Nguyễn Văn A')")
db.execute("INSERT INTO student(name) VALUES ('Nguyễn Văn B')")
db.commit()

# lấy dữ liệu ra
results = db.execute("SELECT * FROM student")
type(results)
    # duyệt còng lặp for để in table 
for row in results:
    print(row)
print("-"*20)

# tìm kiếm theo name hoặc id
results = db.execute("SELECT * FROM student WHERE id = 3")
results = db.execute("SELECT * FROM student ORDER BY id DESC")
print(results)
for row in results:
    print(row)

# update dữ liệu
db.execute("UPDATE student SET name = 'VBPO' WHERE id = 3")
results = db.execute("SELECT * FROM student ORDER BY id DESC")
print("------------------")
for row in results: 
    print(row)

# delete dữ liệu
db.execute("DELETE FROM student WHERE id = 3 ")
results = db.execute("SELECT * FROM student ORDER BY id DESC")
print("------------------")
for row in results: 
    print(row)