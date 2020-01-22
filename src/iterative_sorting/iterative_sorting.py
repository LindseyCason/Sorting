#     # TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        while cur_index< len(arr):
            if arr[cur_index]< arr[smallest_index]:
                smallest_index=cur_index
            cur_index=cur_index+1
            print("current index",cur_index)
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    #set initial swap status
    swap = True
    while swap:
        #toggle swap
        swap=False
        for i in range(0,len(arr)-1):
            left=arr[i]
            right=arr[i+1]
        #if left is less, swap 'em and toggle swap so it recurses
            if left > right:
                arr[i] = right
                arr[i+1]=left
                swap = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr