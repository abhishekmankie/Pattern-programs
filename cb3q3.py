# ********1******** i=0 , n=5 sp=8 (10-0-2)=2n-i-2=2(n-1)-i
# *******2*2*******  i=1,
# ******3*3*3******  i=2, n=5 sp=6 (10-2-2)   [1,2,3,4,5]
# *****4*4*4*4*****
# ****5*5*5*5*5****

def sol(n):
    
    for i in range(n):
        print("*"*(2*(n-1)-i)+"*".join([str(i+1)]*(i+1))+"*"*(2*(n-1)-i))
        
    
if(__name__)=="__main__":
    num=int(input("Enter the number"))
    sol(num)