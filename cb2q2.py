# 1 2 3 4 5 ------>i=0 n=5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

def sol(n):
    lst=list(map(str,range(1,n+1)))
    for i in range(n):
        print(" ".join(lst[:n-i]))

if __name__=="__main__":
    num=int(input("Enter the number: "))
    sol(num)