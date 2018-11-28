def triangle(n):
    k=2*n - 2
    z=''
    x = 1
    li =[]
    for n_rows in range(n):
        for n_spc in range(0,k):
            z+="    "
        k-=1
        for num in range(n_rows+1):
            z+=str(x)+"      "
            li.append(x)
            x+=2
        dict_[n_rows]=li
        li=[]
    
        z += "\n"
    return z

def rowSum(n):
    sumofrow = 0
    therow = dict_[n-1]
    for item in therow:
        sumofrow += item
    return "The sum of row {} is {}".format(n,sumofrow)

#PROGRAM START
dict_ ={}
n= int(input('How many rows for the triangle :'))
print(triangle(n))
n2=int(input('Choose a row :'))
print(rowSum(n2))

    
    