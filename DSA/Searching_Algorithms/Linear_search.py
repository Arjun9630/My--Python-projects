#Linear search!!
flag, num = 0, [2,5,3,9,1,4,6,8,7]
search_ele = int(input("Enter the search element = "))
for i in range(len(num)):
    if(num[i] == search_ele):
        flag = 1
        print(f"\nElement {search_ele} found at index location {i}")
        break

if(flag == 0):
    print("\nElement not found!!");