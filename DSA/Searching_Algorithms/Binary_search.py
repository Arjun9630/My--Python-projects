numbers = [10, 3, 7, 2, 15, 8]
numbers.sort() #sorting the list  
Search_element = int(input("Enter the element to find its index = "))

start_val = 0
end_val = len(numbers) - 1
flag = 0

while(start_val <= end_val): 
    mid_val = (start_val + end_val) // 2  

    if(numbers[mid_val] == Search_element):
        print(f"{Search_element} element found at index - {mid_val}")
        flag = 1
        break  # Exit the loop if element is found

    elif(Search_element > numbers[mid_val]):
        start_val = mid_val + 1
    else:
        end_val = mid_val - 1  

if(flag == 0):
    print(f"{Search_element} element not found in the list.")