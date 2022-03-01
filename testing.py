

N = 1545647
a = str(N)

five_list = []

for i in range(len(a)):
    if a[i] == "5":
        five_list.append(i)


# we got the indices of the fives:
min_value = float("-inf")
for i in five_list:
    r = a[0:i]+a[i+1:]
    
