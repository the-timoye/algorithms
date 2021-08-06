# Insertion Sort


def insertion_sort(arr):
    """
        @description:
            It maintains a sub-array of sorted and unsorted lists (left to right)
            Sorts a list by comparing each value on with values before it.
        @params:
            arr(LIST): Array containing a list of elements (strings or integers)
        @returns:
            arr(LIST): Sorted array
    """

    if (type(arr) != list):
        return "Array should be a list"

    for i in range(1, len(arr)):
        j  = i -1
        while j > -1: 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

            else:
                j-=j
            
            j-=1




    
    return arr

if __name__ == "__main__":
    print(insertion_sort([4,3,8,2,5]))