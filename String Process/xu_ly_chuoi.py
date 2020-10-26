import codecs
import re
from ast import literal_eval
from datetime import datetime
from datetime import date
file = codecs.open(r"D:\Code\String Processing\Input.txt",'r','utf-8')
string = file.read()
# in ra các số của mã số thuế thông qua re

# x = re.findall(r"(?=Địa chỉ:).*(?=\r\n)",string)
# print(x)
# chuyển từ list về string rồi for ra để in
# File MÃ SỐ THUẾ
m = re.findall(r"(?<=Mã số thuế:\s).*\d",string)
file1 = codecs.open(r"D:\Code\String Processing\Output-Mã số thuế.txt",'w+','utf-8')
for idm,i in enumerate(m,start= 1):
    a = str(idm)+"-"+str(i)
    print(a)
    file1.write(str(a)+ "\n")

# File ĐỊA CHỈ
d = re.findall(r"(?<=Địa chỉ:\s).*\w", string)
file2 = codecs.open(r"D:\Code\String Processing\Output-Địa chỉ.txt",'wb','utf-8')
for idd,j in enumerate(d,start= 1):
    if d[:-1]:
        d = str(idd)+"-"+str(j)
        b = d   
        huyen = re.sub(r"(?<!(Địa chỉ:\s))(Huyện)","H.",b)
        quan = re.sub(r"(?<!(Địa chỉ:\s))(Quận)","Q.",huyen)
        tp = re.sub(r"(?<!(Địa chỉ:\s))(Thành phố)","TP.",quan)        
    print(str(tp) + ".")
    file2.write(str(tp) + "." + "\n")

# File NGÀNH NGHỀ
n = re.findall(r"(?<=Ngành nghề chính:\s).*\w", string)
file3 = codecs.open(r"D:\Code\String Processing\Output-Ngành nghề chính.txt",'wb','utf-8')
for idn,k in enumerate(n,start= 1):
    if n[:-1]:
        n = str(idn)+"-"+str(k)
        c = n   
    print(c.upper() + ".")
    file3.write(str(c.upper())+ "." + "\n")


# File ngày thành lập
ngay = re.findall(r"(?<=Ngày thành lập:\s).*\d", string)
file4 = codecs.open(r"D:\Code\String Processing\Output-Ngày thành lập.txt",'wb','utf-8')
for idl,g in enumerate(ngay,start= 1):
    ngay = str(g)
    day = re.sub(r"(\W)","",ngay)
    # print(day)
    # convert string sang datetime
    dates = datetime.strptime(day,"%d%m%Y").date()
    nam = re.sub(r"(20)","",str(dates))
    yy = re.sub(r"(\W)","",nam)
    # print(yy)
    # # lấy vị trí 2 số đầu để lượt bỏ
    # a = re.sub(r"(20)","",str(dates))
    # # print(str(a))
    # thêm số đếm trước mỗi ngày thành ập
    a = str(idl)+"-"+str(yy)
    print(a)
    file4.write(a + "\n")
    






file.close()
file2.close()
file3.close()
file4.close()



