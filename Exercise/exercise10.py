
# while True:
#     n = int(input("Nhập một số: "))
#     if n <= 100 or n > 1000:
#         print("Không hợp lệ! Mời nhập lại")
#     else:
#         tram = n//100
#         chuc = n//10%10
#         donvi = n%10
        
#         if  tram == 1:
#             print(' Một ', end='')
#         elif tram == 2:
#             print(" Hai ", end='')
#         elif tram == 3:
#             print(" Ba ", end='')
#         elif tram == 4:
#             print(" Bốn ", end='')
#         elif tram == 5:
#             print(" Năm ", end='')
#         elif tram == 6:
#             print(" Sáu ", end='')
#         elif tram == 7:
#             print(" Bảy ", end='')
#         elif tram == 8:
#             print(" Tám ", end='')
#         elif tram == 9:
#             print(" Chín ", end='')
#         print("trăm ", end='')

#         if chuc == 0:
#             print("Linh ", end='')
#         else:
#             if chuc == 2:
#                 print("Hai ", end='')
#             elif chuc == 3:
#                 print("Ba ", end='')
#             elif chuc == 4:
#                 print("Bốn ", end='')
#             elif chuc == 5:
#                 print("Năm ", end='')
#             elif chuc == 6:
#                 print("Sáu ", end='')
#             elif chuc == 7:
#                 print("Bảy ", end='')
#             elif chuc == 8:
#                 print("Tám ", end='')
#             elif chuc == 9:
#                 print("Chín ", end='')
#             print("mươi ", end='')

#         if donvi == 1:
#             print("Một")
#         if donvi == 2:
#             print("Hai")
#         elif donvi == 3:
#             print("Ba")
#         elif donvi == 4:
#             print("Bốn")
#         elif donvi == 5:
#             print("Năm")
#         elif donvi == 6:
#             print("Sáu")
#         elif donvi == 7:
#             print("Bảy")
#         elif donvi == 8:
#             print("Tám")
#         elif donvi == 9:
#             print("Chín")
#         elif 

dic_1 = {
    '1' : 'Một ',
    '2' : 'Hai ',
    '3' : 'Ba ',
    '4' : 'Bốn ',
    '5' : 'Năm ',
    '6' : 'Sáu ',
    '7' : 'Bảy ',
    '8' : 'Tám ',
    '9' : 'Chín ',
    '0' : ''
}
dic_2 = {
    '1' : 'Mười ',
    '2' : 'Hai ',
    '3' : 'Ba ',
    '4' : 'Bốn ',
    '5' : 'Năm ',
    '6' : 'Sáu ',
    '7' : 'Bảy ',
    '8' : 'Tám ',
    '9' : 'Chín ',
    '0' : 'linh '
}

dic_3 = {
    '1' : 'Một ',
    '2' : 'Hai ',
    '3' : 'Ba ',
    '4' : 'Bốn ',
    '5' : 'Năm ',
    '6' : 'Sáu ',
    '7' : 'Bảy ',
    '8' : 'Tám ',
    '9' : 'Chín ',
    '0' : ''
}
while True:
    n = input("Nhập một số: ")
    if len(n) == 3 and str(n).isnumeric() == True:
        if n.endswith("00"):
            print (dic_1[str(n)[0]] + 'trăm ')
        else:     
            print(dic_1[str(n)[0]] + 'trăm ' + dic_2[str(n)[1]]  + dic_3[str(n)[2]])
    else:
        print("Nhập không hợp lệ")


        