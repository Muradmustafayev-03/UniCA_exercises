def strings_distance(str1: str, str2: str) -> int:
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)

    cost = 0
    if str1[-1] != str2[-1]:
        cost = 1

    d1 = strings_distance(str1[:-1], str2) + 1
    d2 = strings_distance(str1, str2[:-1]) + 1
    d3 = strings_distance(str1[:-1], str2[:-1]) + cost

    return min(d1, d2, d3)


def test_strings_distance():
    assert strings_distance('abc', 'abc') == 0
    assert strings_distance('abc', 'abcd') == 1
    assert strings_distance('qwc', 'abc') == 2
    assert strings_distance('kitten', 'sitting') == 3
    assert strings_distance('sitting', 'kitten') == 3
    print('All tests passed!\n')


def main():
    str1 = input('Enter the first string: ')
    str2 = input('Enter the second string: ')
    distance = strings_distance(str1, str2)
    print(f'The distance between "{str1}" and "{str2}" is {distance}')


if __name__ == '__main__':
    test_strings_distance()
    main()
