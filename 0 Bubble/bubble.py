lst = [4,9,2,8,5,3,6,7,1]

def sortA(a_list):
    for i in range(len(a_list)-1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j+1]:
                
                #using temp variable
                # c = a_list[j]
                # a_list[j] = a_list[j+1]
                # a_list[j+1] = c

                #using tuple unpacking (which is advised and is native 'only' to python)
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
                
                # watch the process
                # print(a_list)
    return a_list



print(sortA(lst))

def swap_test(): 
    a = 5
    b = 10

    c = b
    b = a
    a = c

    print(a, b)