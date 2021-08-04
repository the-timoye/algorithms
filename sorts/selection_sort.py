# SELECTION SORT
# Takes the least element in an array and adds it to the very next index of the new array


def selection_sort(arr):

    temp_arr = arr[:]
    sorts_counter = 0
    temp_sorts_counter = 0

    for i in range(len(arr)):


        for j in range(i+1, len(arr)): # [10, 11, 12, 3, 1]
            if arr[i] > arr[j]:
                arr[j] = arr[i]
                arr[i] = temp_arr[j]
                temp_arr = arr[:]
                temp_sorts_counter += 1
                print(arr)
    
    # base case:
    if temp_sorts_counter == sorts_counter:
        return arr
    
    return selection_sort(arr)


if __name__ == "__main__":
    print(selection_sort([10, 11, 12, 3, 1])) 
