# MERGE SORT
# takes a given array, divides into halfs till it each item is a single-element array. Compares indexes of array bita and sorts

def mergeSort(arr): # [1, 4, 2, 6]
    new_arr = arr
    if len(new_arr) > 1: # len(arr) = 4
        midArr = len(new_arr) // 2; # midArr = 4 / 2 = 2
        lhs = new_arr[:midArr]; # [1, 4]
        rhs = new_arr[midArr:] #[2, 6]
        mergeSort(lhs); # [1, 4], midArr = 1, lhs = [1], rhs = [4]
        mergeSort(rhs) # [4]

        lhsIndex = rhsIndex = arrIndex = 0;
        while (lhsIndex < len(lhs)) and (rhsIndex < len(rhs)):
            if lhs[lhsIndex] < rhs[rhsIndex]:
                new_arr[arrIndex] = lhs[lhsIndex]
                lhsIndex+=1
            else:
                new_arr[arrIndex] = rhs[rhsIndex]
                rhsIndex+=1
            arrIndex+=1
        
        while lhsIndex < len(lhs):
            new_arr[arrIndex] = lhs[lhsIndex]
            lhsIndex += 1
            arrIndex += 1
        
        while rhsIndex < len(rhs):
            new_arr[arrIndex] = rhs[rhsIndex]
            rhsIndex += 1
            arrIndex += 1
    return new_arr

if __name__ == '__main__':
    arr = [1, 4, 2, 6, 0, 5, 9, 2]
    print(mergeSort(arr))