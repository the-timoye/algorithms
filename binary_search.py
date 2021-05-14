# Description: Binary Search involves searching a sorted array for a given element. 
# Time Complexity: O(logn)
from helpers import validate_array
def calc_mid_index(high, low):
    mid_index = low + (high - low) // 2
    return mid_index

def binary_search(elements_list, element, lower_index, highest_index):
    '''
        @desc: 
            Binary search - searches a sorted array for a given element
        @params: 
            elements_list(list) - a sorted array of integers
            element(int) - element to be searched for
            lower_index(int) - the index of the lower bound of the array
            highest_index(int) - the index of the highest bound of the array
        @returns:
            string - content depends on the result of the search
    '''

    # Check input validity
    validate_array(elements_list)
    if (type(element) is not int) or (type(lower_index) is not int) or (type(highest_index) is not int):
        checks = [element, lower_index, highest_index]
        invalid_item = lambda item: item if type(item) is not int else 'ok'
        return '(WARN): Element should be of type int. Found {}'.format(invalid_item(x for x in checks))

    mid = calc_mid_index(lower_index, highest_index)

    # Handle elements outside given array
    if (highest_index < lower_index) or (highest_index == lower_index):
        return 'Element {} not found.'.format(element)

    # Base case
    if element == elements_list[mid]:
        return '{} is in index {}'.format(element, mid)

    if element < elements_list[mid]:
        print('{} is less than {}. Element is in the lower bound'.format(element, elements_list[mid]))
        highest_index = mid - 1
        return binary_search(elements_list, element, lower_index, highest_index)

    if element > elements_list[mid]:
        print('{} is greater than {}. Element is in the upper bound'.format(element, elements_list[mid]))
        lower_index = mid + 1
        return binary_search(elements_list, element, lower_index, highest_index)
    return 'Element {} not found.'.format(element)


def main():
    arr = [1, 2, 3, 4, 6, 8, 9, 10, 13, 15, 19, 24, 29, 50]
    lower_index = 0
    highest_index = len(arr) - 1
    print(binary_search(arr, 6, lower_index, highest_index))

if __name__ == '__main__':
    main()