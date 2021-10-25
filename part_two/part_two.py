from tests import ALG_ONE_TESTS


def get_total_identical_pairs(list_of_numbers):
    """
    Given an array of integers
    Return the amount of "GOOD" pairs in the array
    Where list_of_numbers[a] == list_of_numbers[b] and a < b
    """
    #validate array values - if float or non-numeric, return 'Invalid'
    if not all(isinstance(item, int) for item in list_of_numbers):
        return "INVALID"
    tally = 0
    lstlen = len(list_of_numbers)
    for a in range(lstlen):
        for b in range(a + 1, lstlen):
             if list_of_numbers[a] == list_of_numbers[b]:
                 tally += 1
    return tally


if __name__ == "__main__":
    #Left in prints at lines 28 & 30 just to provide visual feedback.
    for test in ALG_ONE_TESTS:
        result = get_total_identical_pairs(
            test.get('list_of_numbers'),
        )
        print("RESULT: {}".format(result))
        expected_result = test.get('expected_result')
        print("EXPECTED: {}".format(expected_result))
        assert result == expected_result, "This test expected {} pairs, but it returned {} pairs".format(
            result,
            expected_result,
        )
