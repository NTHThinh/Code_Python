def luuFile (path):
    file = open (path, 'w', encoding='utf-8')
    file.writelines ('SV001, Nguyễn Văn A, 1/1/1998 \n')
    file.writelines ('SV002, Nguyễn Văn B, 2/2/1997 \n')
    file.writelines ('SV003, Nguyễn Văn C, 3/3/1999 \n')
    file.close()
luuFile('csdlsinhvien.txt')

def docFile (path):
    file = open (path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()
        print (data)
    file.close()
docFile('csdlsinhvien.txt')
