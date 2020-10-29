import xml.etree.ElementTree as ET
import codecs
import re
import os
import inspect
import json

"""Đường dẫn file tương đối"""
CurDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(CurDir)

path = "/var/www/html/"
for filename in os.listdir(CurDir + "\\input"):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(CurDir + "\\input", filename)
    tree = ET.parse(fullname)
def xuly(string):
    mau_hoa_don = re.findall(r"(?<=InvoicePattern>).*(?=<\/InvoicePattern>)",string)
    ky_hieu_hoa_don = re.findall(r"(?<=SerialNo>).*(?=<\/SerialNo>)",string)
    so_hoa_don = re.findall(r"(?<=InvoiceNo>).*(?=<\/InvoiceNo>)",string)
    ngay_hoa_don = re.findall(r"(?<=ArisingDate>).*(?=<\/ArisingDate>)",string)
    ten_khach_hang = re.findall(r"(?<=ComName>).*(?=<\/ComName>)",string)
    ma_so_thue_khach_hang = re.findall(r"(?<=CusTaxCode>).*(?=<\/CusTaxCode>)",string)
    stt = re.findall(r"(?<=ProdType>).*(?=<\/ProdType>)",string)
    str_stt = "stt".join(stt)
    ten_san_pham = re.findall(r"(?<=ProdName>).*(?=<\/ProdName>)",string)
    don_gia = re.findall(r"(?<=ProdPrice>).*(?=<\/ProdPrice>)",string)
    str_don_gia = "don_gia".join(don_gia)
    so_luong = re.findall(r"(?<=ProdQuantity>).*(?=<\/ProdQuantity>)",string)
    str_so_luong = "so_luong".join(so_luong)
    thanh_tien = re.findall(r"(?<=Total>).*(?=<\/Total>)",string)
    tong_tien = re.findall(r"(?<=Total>).*(?=<\/Total>)",string)
    tong_thue = re.findall(r"(?<=VatAmount10>).*(?=<\/VatAmount10>)",string)
    tong_tien_sau_thue = re.findall(r"(?<=Amount>).*(?=<\/Amount>)",string)
        # Cách 2: (?<=CusTaxCode>\W\s\s\s).*(?=\W+CusTaxCode) print(string.replace("\s","")  
    dic = {
        "Mau_hoa_don" : "".join(mau_hoa_don),
        "Ky_hieu_hoa_don" : "".join(ky_hieu_hoa_don),
        "So_hoa_don" : "".join(so_hoa_don),
        "Ngay_hoa_don" : "".join(ngay_hoa_don),
        "Ten_khach_hang" : "".join(ten_khach_hang),
        "Ma_so_thue_khach_hang" : "".join(ma_so_thue_khach_hang),
        "Chi_tiet_hoa_don" : [{
            "STT" : int(str_stt),
            "Ten_san_pham" : "".join(ten_san_pham),
            "Don_gia" : int(str_don_gia),
            "So_luong" : int(str_so_luong),
            "Thanh_tien" : int(thanh_tien[1])
        }],
        "Tong_tien" : int(tong_tien[0]),
        "Tong_thue" : int(tong_thue[0]),
        "Tong_tien_sau_thue" : int(tong_tien_sau_thue[0])  
    }
    print(dic)
print(xuly(string))