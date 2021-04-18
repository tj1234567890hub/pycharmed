number_of_cars = input("enter numbers of cars")
magic = int(number_of_cars)
print("number of cars = ", magic)
if magic <0:
    print("how did that happen")
elif magic == 0:
    print("buy one")
elif magic >0 and magic <3:
    prinnt("buy more")
elif magic >3 and magic <7:
    print("too much")
else:
    print("donate a few cars")