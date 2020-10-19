def isPrime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        return 1
    else:
        return 0

while True:
    n=int(input("Nhập số nguyên n: "))
    sum=0
    for i in range(1,n):
        if isPrime(i)==1:
            sum = sum+i
    print("Tổng các số nguyên tố: %d"%sum)
    print("Có muốn tiếp tục không thím? (c/k)")
    c = input()
    if c=='k' or c=='K':
        break


