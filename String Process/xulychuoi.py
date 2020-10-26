import codecs
import re
from datetime import datetime
from datetime import date
# Đọc file txt
file = codecs.open(r"C:\Users\HUU THINH\Code_Python\String Process\Input.txt",'r','utf-8')
string = file.read()


list_Address = re.findall(r"(?<=Địa chỉ:\s).*\w", string)
list_Ma_so_thue = re.findall(r"(?<=Mã số thuế:\s).*\d",string)
list_Nganh_nghe = re.findall(r"(?<=Ngành nghề chính:\s).*\w", string)
list_Ngay_thanh_lap = re.findall(r"(?<=Ngày thành lập:\s).*\d", string)

for idx_Adress,i_Address in enumerate (list_Address):
    str_Adress = str(idx_Adress+1) + '-' + str(list_Address[idx_Adress])
    # print(str_Adress)
    str_Masothue = str(idx_Adress+1) + '-' + str(list_Ma_so_thue[idx_Adress])
    # print(str_Masothue)
    str_Nganhnghe = str(idx_Adress+1) + '-' + str(list_Nganh_nghe[idx_Adress])
    str_Ngaythanhlap = str(idx_Adress+1) + '-' + str(list_Ngay_thanh_lap[idx_Adress])


    """Xử lý phần địa chỉ"""
    file1 = codecs.open(r"C:\Users\HUU THINH\Code_Python\String Process\Output-Địa chỉ.txt",'a','utf-8')
    huyen = re.sub(r"(?<!(Địa chỉ:\s))(Huyện)","H.",str_Adress)
    quan = re.sub(r"(?<!(Địa chỉ:\s))(Quận)","Q.",huyen)
    tp = re.sub(r"(?<!(Địa chỉ:\s))(Thành phố)","TP.",quan)
    # print(str(tp) + "." + "\n")  
    file1.write(str(tp) + "." + "\n")
    file1.close()

    """Xử lý phần mã số thuế"""
    file2 = codecs.open(r"C:\Users\HUU THINH\Code_Python\String Process\Output-Mã số thuế.txt",'a','utf-8')
    # print(str_Masothue + "\n")
    file2.write(str_Masothue + "\n")
    file2.close()

    """Xử lý phần ngành nghề"""
    file3 = codecs.open(r"C:\Users\HUU THINH\Code_Python\String Process\Output-Ngành nghề chính.txt",'a','utf-8')
    # print(str_Nganhnghe.upper() + ".")
    file3.write(str(str_Nganhnghe.upper())+ "." + "\n")
    file3.close()

    """Xử lý ngày thành lập"""
    file4 = codecs.open(r"C:\Users\HUU THINH\Code_Python\String Process\Output-Ngày thành lập.txt",'a','utf-8')
    dates = datetime.strptime(str_Ngaythanhlap,str(idx_Adress+1) + '-' + "%d-%m-%Y").date()
    # print(str(dates))
    # string = str_Ngaythanhlap[-2:] + str_Ngaythanhlap[4:6] + str_Ngaythanhlap[:2]
    list_format = re.sub(r"(?<=^)\d{2}|-","", str(dates))
    # print(str(idx_Adress+1) + '-' + str(list_format))
    file4.write(str(idx_Adress+1) + '-' + str(list_format) + "\n")
    file4.close()


 

