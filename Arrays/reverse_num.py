x = 120
new_number = 0
if x<0:
    x = -x
    while(x!=0):
        y = x%10
        
        new_number = new_number*10+y
        print("new_number",new_number)

        x = x//10
        print("x",x)
    new_number = -new_number
if x>0:
    while(x!=0):
        y = x%10

        new_number = new_number*10+y
        print("new_number",new_number)

        x = x//10
        print("x",x)
print(new_number)