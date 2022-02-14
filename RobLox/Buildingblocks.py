
from numpy import number


def setbaricad(number_line, number):
    if(number_line[number] == "b"):
        return "0"
    else:
        number_line[number] = "b"
    return number_line

def buildingblocks(op):
    number_line = list([0]*999999999)
    for i in op:
        if op[i][0] == 1:
            number_line[op[i][1]] = "b"
        
        if op[i][0] == 2:
            number = op[i][1]-op[i][2]
            while(number < op[i][1]):
                a = setbaricad(number_line,number)
                if(a!= "0"):
                    string.append("0")
                break
                
                number += 1


op = [[1,2],[1,5],[2,5,2],[2,6,3],[2,2,1],[2,3,2]]
buildingblocks(op)