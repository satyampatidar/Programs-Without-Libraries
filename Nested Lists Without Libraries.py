def count(l):
    global c_dict
    for element in l:
        c_dict[element] += 1

def count_all(a):
    for element in a:
        if type(element) != type([]):
            count(a)
            break
        else:
            count_all(element)

def count_elements(a):
    global c_dict
    c_dict = {1:0, 2:0, 3:0 , 4:0}
    count_all(a)
    for key, value in c_dict.items():
        print(f"No. of {key}'s: {value}")


testMat1 = [[1, 2, 3, 2, 4], [4, 3, 1], [[[2, 1, 4, 2, 3, 3, 1]]] ]
count_elements(testMat1)

testMat2 = [[[[[3, 2, 1]], [[[4,2]], [], [2]]]]]
count_elements(testMat2)
