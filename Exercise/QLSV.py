
class sinhvien:
    def __init__(self,mssv=None,ten=None,namsinh=None,lop=None,nmlt=None,trr=None,ktlt=None,csdl=None):
        self.ten = ten
        self.mssv = mssv
        self.namsinh = namsinh
        self.lop = lop
        self.nmlt = nmlt
        self.trr = trr
        self.ktlt = ktlt
        self.csdl = csdl
    # Hàm nhập thông tin sinh viên
    def nhaplieu(self):
        print("===== NHẬP THÔNG TIN SINH VIÊN =====")
        self.mssv = int(input("Nhập MSSV: "))
        self.ten = str(input("Nhập tên sinh viên: "))
        self.namsinh = int(input("Nhập năm sinh: "))
        self.lop = str(input("Nhập lớp: "))
        self.nmlt = int(input("Điểm nhập môn lập trình: "))
        self.trr = int(input("Điểm toán rời rạc: "))
        self.ktlt = int(input("Điểm kỹ thuật lập trình: "))
        self.csdl = int(input("Điểm cơ sở dữ liệu: "))
    # Hàm tính điểm trung bình
    def tb(self):
        trungbinh = (self.nmlt + self.trr + self.ktlt + self.csdl)/4
        print("Điểm trung bình: ", trungbinh)
    # Hàm hiển thị thông tin sinh viên
    def hienthi(self):
        print( "===== THÔNG TIN SINH VIÊN =====")
        student = {
            "Tên sinh viên" : self.ten,
            "MSSV" : self.mssv,
            "Năm sinh" : self.namsinh,
            "Lớp" : self.lop,
            "Điểm NMLT" : self.nmlt,
            "Điểm TRR" : self.trr,
            "Điểm KTLT" : self.ktlt,
            "Điểm CSDL" : self.csdl
        }
        #   Vòng lặp for để duyệt distionary in ra danh sách
        for x in student:
            print( "-",x, "==>", student.get(x))
            
        # print(self.mssv,"   ",self.ten,"    ",self.namsinh,"    ",self.lop,"    ",self.nmlt,"    ",self.trr,"    ",self.ktlt,"    ",self.csdl,"    ")
def main():
    s = sinhvien()
    while True:
        print("\n")
        print("-----CHƯƠNG TRÌNH QUẢN LÝ HỌC TẬP-----")
        print("1. Nhập thông tin sinh viên")
        print("2. In thông tin sinh viên")
        print("3. Số lượng sinh viên có điểm trung bình lớn hơn 5")
        print("4. Số lượng sinh viên có điểm trung bình nhỏ hơn 5")
        print("0. Thoat")
        
        command = int(input("======> Mời nhập lựa chọn: "))
        print("--------------------------------------")
        if command == 0:
            break
        elif command == 1:
            s.nhaplieu()
            print("Successfull")
        elif command == 2:
            s.hienthi()
            print("Hiển thị thành công")
        elif command == 3:
            s.tb()
        elif command == 4:
            s.tb()
        
if __name__== "__main__":
  main()