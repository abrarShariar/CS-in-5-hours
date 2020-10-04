def bubble_sort(num_list):
    isSwapped = True
    while isSwapped:
        isSwapped = False
        for i in range(1, len(num_list)):
            if num_list[i-1] > num_list[i]:
                num_list[i-1], num_list[i] = num_list[i], num_list[i-1]
                isSwapped = True
    return num_list

print(bubble_sort([9,8,67,6,4,2]))
print(bubble_sort([]))
print(bubble_sort([1,2]))
print(bubble_sort([2,1]))
print(bubble_sort([1]))