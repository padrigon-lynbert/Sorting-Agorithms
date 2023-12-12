lst = [4,9,2,8,5,3,6,7,1]

def sort(a_list):
    indexing_length = range(1, len(a_list))
    for i in indexing_length:
        value_to_sort = a_list[i]

        while a_list[i-1] > value_to_sort and i>0:
            a_list[i], a_list[i-1] = a_list[i-1], a_list[i]
            i -= 1

    return a_list

print(sort(lst))


