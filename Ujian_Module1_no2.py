def tickets(ppl=list):
    change = 0
    for item in ppl:
        if item-25 > change:
            print('No. She cannot')
            return False
        elif item > 25:
            change -= item - 25    
        change += 25
    print('Yes. It is possible')
    return True

arr =[25,25,50,50,100]
print(arr)
tickets(arr)