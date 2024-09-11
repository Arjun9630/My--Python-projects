Element_list = [3, 5, 1, 7, 2, 6, 0, 9, 8, 11, 10, 15, 21, 20, 16, 13]

def selectionSort(Element_list):
    for i in range(0, len(Element_list)):
        for j in range(i + 1, len(Element_list)):
            if Element_list[i] > Element_list[j]:
                Element_list[i], Element_list[j] = Element_list[j], Element_list[i]
    return Element_list

if __name__ == '__main__':
    Element_list = selectionSort(Element_list)
    print(Element_list)