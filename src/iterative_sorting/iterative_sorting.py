# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        while cur_index < len(arr):
            #until we get to the end of the arrays indicies
            #if the left number is smaller, set index to smaller index
            if arr[cur_index] < arr[smallest_index]:
                smallest_index = cur_index
                cur_index = cur_index +1

        #complete the swap
        #make these two on the left, now equal to the ones on the right in reverse order
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
        #if left is less, swap 'em
            if left > right:
                arr[i] = right
                arr[i+1]=left
                swap = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr