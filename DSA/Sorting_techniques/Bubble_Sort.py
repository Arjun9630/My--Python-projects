Element_list = [3, 5, 1, 7, 2, 6, 0, 9, 8, 11, 10, 15, 21, 20, 16, 13]

for i in range(0, len(Element_list)):
    swapped = False
    for j in range(0, len(Element_list)-1):
        if Element_list[j] > Element_list[j+1]:
            Element_list[j], Element_list[j+1] = Element_list[j+1], Element_list[j]
            swapped = True
    if swapped == False:
        break
print(Element_list)