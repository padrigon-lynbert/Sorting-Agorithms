

lst = [4,9,2,5,3,6,7,1]

def sort(a_list):
    for i in range(len(a_list)-1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j+1]:
                
                c = a_list[j]
                a_list[j] = a_list[j+1]
                a_list[j+1] = c
    
    return a_list

print(sort(lst))

def test(): 
    a = 5
    b = 10

    c = b
    b = a
    a = c

    print(a, b)