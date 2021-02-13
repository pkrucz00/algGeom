array = [3,4,2,1,3,6,5,7,4,6,3,5,10]

top1 = array[0]
top2 = array[1]
for tmp in array[2:]:
    if tmp > top1:
        top2 = top1
        top1 = tmp
    elif tmp > top2:
        top2 = tmp

print(top1, top2)
