# Selection Sort Technique
num = [2,5,3,9,1,4,6,8,7]

def selectionSort(num_list): #sort function definition
    for i in range(len(num_list)): #outer loop
        min_index = i
        for j in range(i+1,len(num_list)): #inner loop
            if(num_list[min_index]>num_list[j]): #check if value at minimum index is greater than value at j
                min_index = j
        temp = num_list[i] #swapping elements
        num_list[i] = num_list[min_index]
        num_list[min_index] = temp
    return num_list #returns updated list

if __name__ == '__main__':
    num = selectionSort(num)
    print(num)