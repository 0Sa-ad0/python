#1
import numpy as np

matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

result = np.matmul(matrix1, matrix2)
print(result)

#output
[[ 30  24  18]
 [ 84  69  54]
 [138 114  90]]



#2
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

result = list(map(list, zip(*matrix)))
print(result)

#output
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]





#3
import numpy as np

matrix1 = np.array([[1, 2],
                    [3, 4],
                    [5, 6]])

matrix2 = np.array([[7, 8, 9],
                    [10, 11, 12]])

result = np.dot(matrix1, matrix2)
print(result)

#output
[[ 27  30  33]
 [ 61  68  75]
 [ 95 106 117]]




#4
def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i 

    return -1  

my_list = [5, 2, 9, 1, 7, 3]

target_element = 7
result_index = linear_search(my_list, target_element)

if result_index != -1:
    print(f"Element {target_element} found at index {result_index}.")
else:
    print(f"Element {target_element} not found.")

#output
Element 7 found at index 4.




#5
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1  

    return -1  

my_list = [1, 2, 3, 5, 7, 9]

target_element = 5
result_index = binary_search(my_list, target_element)

if result_index != -1:
    print(f"Element {target_element} found at index {result_index}.")
else:
    print(f"Element {target_element} not found.")
    
#Output
Element 5 found at index 3.
