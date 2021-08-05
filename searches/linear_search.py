# Description: Searches a list of elements sequentially to find a given element
# Time Complexity: 0(n)

from helpers import validate_array

def linear_search(elements, element):
    """
        @description:
            Searches a list of elements sequentially to find a given element
        @params:
            elements(list): a list of elements to be searched from
            element: item to be searched for
        @return:
            str
    """
    validate_array(elements)
    index = 0
    arr_length = len(elements)
    match = element == elements[index]

    while arr_length:
        if index == arr_length:
            return 'Element {} does not exist in this array'.format(element)

        print('Checking index {}'.format(index))

        if match:
            return 'Element has been found in index {}'.format(index)
        index+=1

if __name__ == '__main__':
    
    print(linear_search([1,4,2,34,35,465,34,4,23,43,34], 4))