# 1
# 1 2   ----> i=1 n=5
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def sol(n):
    lst=list(map(str,range(1,n+1)))
    print(lst)
    for i in range(n):
        print(" ".join(lst[:i+1]))
        
        

if __name__=="__main__":
    num=int(input("Enter The number "))
    sol(num)

  