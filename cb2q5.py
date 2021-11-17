#     1  --> i=0, n=5  [1:i+2]
#    1 2 ---> i=1 n=5 sp--->1 2(i)-1
#   1   3 ---> i=2,n=5  sp---->3
#  1     4  ---> i=3, n=5 sp---->5
# 1 2 3 4 5  ---> i=4 n=5  [1:i+2]

def sol(n):
    lst=list(map(str,range(1,n+1))) #[1,2,3,4,5]
    

    for i in range (n):
        if (i==0 or i==n-1):
           print(" "*(n-i)+" ".join(lst[0:i+1]))
        else:
            print(" "*(n-i)+"1"+" "*(2*i-1) + str(i+1))
    
if __name__=="__main__":
    num=int(input("Enter the number"))
    sol(num)