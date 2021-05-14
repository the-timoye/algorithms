def validate_array(elements_list):
    if type(elements_list) is not list:
        return '(WARN): Elements list should be of type list. Found {}'.format(type(elements_list))