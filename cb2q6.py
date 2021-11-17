# 1        ----> i=0, n=5 
# 1 2   1  -----> i=1, n=5       [1,2,3,4,5]
# 1 2 3   2 1 ---> i=2, n=5         [1:]
# 1 2 3 4   3 2 1 ---> i=3, n=5
# 1 2 3 4 5   4 3 2 1

def sol(n):
    lst=list(map(str,range(1,n+1)))
    for i in range(n):
        if (i==0):
            print(" ".join(lst[:i+1]))
        else:
            print(" ".join(lst[:i+1])+" " +" ".join(lst[i-1::-1]))
    
if __name__=="__main__":
    num=int(input("Enter the number"))
    sol(num)