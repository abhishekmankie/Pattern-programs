# ********1********
# *******2*2*******
# ******3*3*3******
# *****4*4*4*4*****
# ****5*5*5*5*5****

n=5
for i in range(n+1):
    for j in range(18):
        if(i==0 and j==8 or i==1 and j==7 and j==9 or i==2 and j==6 and j==8 and j==10 or i==3 and j==5 and j==7 and j==9 or j==11 and i==4 and j==4 and j==6 and j==8 and j==10):
            print('8',end="")
        else:
            print("*")
print()    
            