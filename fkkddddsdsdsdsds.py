res=0
def cubed(numb):
    numb=int(numb)
    res = numb ** 0.5
    return res

numb=input("enter your  number")
res=cubed(numb)
print("Result is ", res)