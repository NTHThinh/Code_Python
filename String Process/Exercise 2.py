import codecs
import re
import os
import inspect
import json

"""Đường dẫn file tương đối"""
CurDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(CurDir)

path = "/var/www/html/"
dirs = os.listdir(CurDir + "\\input")
for files in dirs:
    # print(files)
    file1 = codecs.open(CurDir + "\\input\\" +str(files),'r','utf-8')
    string1 = file1.read()
    string2 = file1.read()
    print(string1,string2)
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
print(xuly(string1))
print(xuly(string2))

# def xuly1(string):
#     mau_hoa_don = re.findall(r"(?<=inv:templateCode>).*(?=<\/inv:templateCode>)",string)
#     ky_hieu_hoa_don = re.findall(r"(?<=inv:invoiceSeries>).*(?=<\/inv:invoiceSeries>)",string)
#     so_hoa_don = re.findall(r"(?<=inv:invoiceNumber>).*(?=<\/inv:invoiceNumber>)",string)
#     ngay_hoa_don = re.findall(r"(?<=inv:signedDate>).*(?=<\/inv:signedDate>)",string)
#     ten_khach_hang = re.findall(r"(?<=inv:buyerLegalName>).*(?=<\/inv:buyerLegalName>)",string)
#     ma_so_thue_khach_hang = re.findall(r"(?<=inv:buyerTaxCode>).*(?=<\/inv:buyerTaxCode>)",string)
#     stt = re.findall(r"(?<=inv:lineNumber>).*(?=<\/inv:lineNumber>)",string)
#     str_stt = "stt".join(stt)
#     ten_san_pham = re.findall(r"(?<=inv:itemName>).*(?=<\/inv:itemName>)",string)
#     don_gia = re.findall(r"(?<=inv:unitPrice>).*(?=<\/inv:unitPrice>)",string)
#     str_don_gia = "don_gia".join(don_gia)
#     so_luong = re.findall(r"(?<=inv:quantity>).*(?=<\/inv:quantity>)",string)
#     str_so_luong = "so_luong".join(so_luong)
#     # thanh_tien = re.findall(r"(?<=inv:itemTotalAmountWithoutVat>).*(?=<\/inv:itemTotalAmountWithoutVat>)",string)
#     tong_tien = re.findall(r"(?<=inv:itemTotalAmountWithoutVat>).*(?=<\/inv:itemTotalAmountWithoutVat>)",string)
#     tong_thue = re.findall(r"(?<=inv:vatAmount>).*(?=<\/inv:vatAmount>)",string)
#     tong_tien_sau_thue = re.findall(r"(?<=inv:totalAmountWithVAT>).*(?=<\/inv:totalAmountWithVAT>)",string)
#     dic = {
#         "Mau_hoa_don" : "".join(mau_hoa_don),
#         "Ky_hieu_hoa_don" : "".join(ky_hieu_hoa_don),
#         "So_hoa_don" : "".join(so_hoa_don),
#         "Ngay_hoa_don" : "".join(ngay_hoa_don),
#         "Ten_khach_hang" : "".join(ten_khach_hang),
#         "Ma_so_thue_khach_hang" : "".join(ma_so_thue_khach_hang),
#         "Chi_tiet_hoa_don" : [{
#             "STT" : int(str_stt[0]),
#             "Ten_san_pham" : "".join(ten_san_pham),
#             "Don_gia" : float(str_don_gia[0]),
#             "So_luong" : float(str_so_luong[0]),
#             # "Thanh_tien" : int(thanh_tien[1])
#         }],
#         "Tong_tien" : int(tong_tien[0]),
#         "Tong_thue" : int(tong_thue[0]),
#         "Tong_tien_sau_thue" : int(tong_tien_sau_thue[0])  
#     }
#     print(dic)
# print(xuly1(string3))
# print(xuly1(string4))

# file1 = codecs.open(CurDir + "\\output\\20201027_014103_WEB_775_1_219_26_2192695202010270141039993_1.json",'a',encoding='utf-8')
# file1.write(str(dic) + "\n")



