import argparse

parser = argparse.ArgumentParser(
    description='Convert roman numeral to integer')
parser.add_argument('roman_numeral', type=str,
                    help='a string repping roman numeral')

args = parser.parse_args()
roman_numeral = args.roman_numeral


def convert_to_integer():
    """
    Defines the breakpoints and cache for the converter.
    @returns:
        converter(func): does the convertion process
    """
    breakpoints = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    __cache__ = 0

    def converter(numeral):
        """
        Converts roman numeral to integer.
        Run script like python3 roman_to_integer <roman_numeral> .
        @Example:
            `python3 roman_to_integer CD`
        @params:
            numeral(str): a roman numeral to be converted e.g. MMCM
        @returns:
            __cache__(int): the resulting integer
        """
        nonlocal __cache__
        if len(numeral) < 1:
            return __cache__
        curr_val = breakpoints.get(numeral[0], 0)
        if len(numeral) < 2:
            __cache__ = __cache__ + curr_val
            return __cache__
        start_index = 1
        next_val = breakpoints.get(numeral[1], 0)
        if next_val > curr_val:
            curr_val = next_val - curr_val
            start_index += 1
        __cache__ = __cache__ + curr_val
        numeral[start_index:]
        return converter(numeral[start_index:])
    return converter
