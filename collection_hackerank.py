from collections import Counter

def pricedetect(X, N, cust):
    shoe_pair = Counter(X)
    
    price = 0
    for i in range(len(cust)):

        if cust[i][0] in shoe_pair and shoe_pair[cust[i][0]] > 0:
            price += cust[i][1]
            print(shoe_pair)
            shoe_pair.update({cust[i][0]:-1})
            #Print the price till now
            print(price)
            #Printing updated shoe_pair
            print(shoe_pair)
    
    return price

X = [2,3,4,5,6,8,7,6,5,18]
N = 6
cust = [[6,55], [6,45], [6,55], [4,40], [18,60], [10,50]]

pricedetect(X, N, cust)