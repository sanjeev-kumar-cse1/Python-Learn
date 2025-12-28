# 1.. Nested If-else condition
sunnyDay = True
isAvailable = True
if sunnyDay:
    if isAvailable:
        print("Ok , let's play") #This will be output for this program
    else:
        print("No play")
else:
    print("It's rainy outside")


# 2..
sunnyDay = True
isAvailable = True
bat = False
if sunnyDay:
    if isAvailable:
        if bat:
            print("Ok , let's play")
        else:
            print("Bat is not available for play") #due to false condition , this line will be print 
    else:
        print("No play")
else:
    print("It's rainy outside")

# 3..
sunnyDay = False
isAvailable = True
bat = False
if sunnyDay:
    if isAvailable:
        if bat:
            print("Ok , let's play")
        else:
            print("Bat is not available for play") 
    else:
        print("No play")
else:
    print("It's rainy outside") #This is print 