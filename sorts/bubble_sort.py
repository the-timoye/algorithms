# BUBBLE SORT: Compares adjascent values [a, b, c] and performs a swap if b < a ...

def bubble_sort(arr, sorts_count):
    """
        @description:
            Sorts a given array using the Bubble Sort approach
        @params:
            arr (LIST): A list containing items to sort
            sorts_count (INT): Holds the number of times a sort was carried out. 
                                    Used to track whether or not the array is sorted
        @returns:
            (LIST): the sorted array
    """
    if type(arr) is not list:
        return 'Your input should be a list'

    temp_arr = arr
    temp_sorts_count = sorts_count

    i = 0
    while (i < (len(temp_arr) -1)):
        if temp_arr[i] > temp_arr[i+1]:
            cache = temp_arr[i]
            temp_arr[i] = temp_arr[i+1]
            temp_arr[i+1] = cache
            temp_sorts_count = temp_sorts_count + 1
        if (i == len(temp_arr) - 2) and (temp_sorts_count > sorts_count):
            sorts_count = temp_sorts_count
            print('sorts count {}'.format(sorts_count))
            i = -1
        if (i == len(temp_arr) - 2) and (temp_sorts_count <= sorts_count):
            break
        i+=1
    
    return temp_arr

if __name__ == '__main__':
    print(bubble_sort(['a', 'b', 'd', 'p', 'c', 'e'], 0))