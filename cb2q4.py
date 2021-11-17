#        1       i=0 n=5 sp=8 
#      2 3 2     i=1 n=5 sp=6 [2:4]     
#    3 4 5 4 3   i=2 n=5 sp=4  [3:6]    [4:2:-1]      
#  4 5 6 7 6 5 4 i=3 n=5 sp=2   [(i+1):(i+1)*2]  [6:3:-1]
#5 6 7 8 9 8 7 6 5 

def solution(n):
    lst=list(map(str,range(2*n)))  #['0','1','2','3','4','5','6','7','8','9']
    for i in range (n):
        print(" "*(2*(n-i-1))+" ".join(lst[(i+1):((i+1)*2)])+" "+" ".join(lst[2*i:i:-1]))

if __name__=="__main__":
    num=int(input("Enter the number"))
    solution(num)