# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB ) #this is a number
    merged_arr = [0] * elements 
    indexA=0 #indexs to check arrA
    indexB=0 #indexs to check for arrB
    for i in range(elements):
        #check to see if they are empty arrays, is 0 greater than the length of the array
        if indexA>= len(arrA):
            merged_arr[i]=arrB[indexB]
            print(merged_arr)
            indexB+=1
        elif indexB >= len(arrB):
            merged_arr[i] = arrA[indexA]
            print(merged_arr)

            indexA+=1
        #below: if arrA index is less than arrB index places lowest number at merged_arr else do the reverse and increment the index
        elif arrA[indexA] < arrB[indexB]:
            merged_arr[i] = arrA[indexA]
            print(merged_arr)
            indexA+=1
        else:
            merged_arr[i] = arrB[indexB]
            print(merged_arr)
            indexB+=1

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr

    left=arr[:len(arr) // 2 ]
    right=arr[len(arr) // 2:]

    left = merge_sort(left)
    right= merge_sort(right)
    
    return merge(left, right)
    

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
