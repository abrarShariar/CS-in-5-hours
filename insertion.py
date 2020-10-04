# def insertion_sort(num_list):
#     for i in range(1, len(num_list)):
        
#         prev_index = i - 1
#         current_index = i

#         while prev_index >= 0 and num_list[prev_index] > num_list[current_index]:
#             num_list[prev_index], num_list[current_index] = num_list[current_index], num_list[prev_index]
#             prev_index -= 1
#             current_index -= 1
    
#     return num_list

def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        key = num_list[i]
        start_index = i - 1
        while start_index >= 0 and key < num_list[start_index]:
            num_list[start_index + 1] = num_list[start_index]
            start_index -= 1

        num_list[start_index + 1] = key

    return num_list

print(insertion_sort([10,9,1,4,5,0]))
print(insertion_sort([10,9]))
print(insertion_sort([1]))
print(insertion_sort([]))




