
def elementsort(input):
    emp_dict = {}
    input = sorted(input, key = lambda i:i["Id"])

    for i in range(len(input)):
        id = input[i]["Id"]
        emp_dict.append(input[i])
        for j in range(i,len(input)):
            if(input[j]["parentID"] == id):
                emp_dict.append(input[j])
        
    return input

input = [
    {
        'Id': 0,
        'location': 'Americas',
        'parentID': None
    },
    {
        'Id': 22,
        'location': 'Cali',
        'parentID': 2
    },
    {
        'Id': 3,
        'location': 'Detroit',
        'parentID': 0
    },
    {
        'Id': 211,
        'location': 'Ilionois',
        'parentID': 2
    },
    {
        'Id': 21,
        'location': 'Michigan',
        'parentID': 22
    },
    {
        'Id': 2,
        'location': 'US',
        'parentID': 0
    },
    {
        'Id': 11,
        'location': 'Britich Columbai',
        'parentID': 1
    },
    {
        'Id': 1,
        'location': 'Canada',
        'parentID': 0
    }
]

print(elementsort(input))