#! /usr/bin/python3
import sys


def is_alphabet_order(word):
    for i in range(1):
        if word[i] > word[i + 1]:
            return False
    return True


def main():
    lines = []
    # collect data
    for line in sys.stdin:
        lines.append(line)
        if len(lines) == 2:
            break

    # a = encrypted message, b = fragment
    a = lines[0].strip()
    b = lines[1].strip()

    # if fragment length is longer than encrypted message, print(0), no need to continue
    if len(b) > len(a):
        print(0)
        return None

    # possible matched fragments
    fragments = {}

    # collect all candidates that are possibly matching, insert to fragments{}
    for index, val in enumerate(a):
        if index + len(b) <= len(a):
            ele = a[index: index + len(b)]
            fragments[ele] = True
        else:
            break
    print(fragments)
    # validate each single fragment
    for key in fragments:
        fragment_dict = {}
        for index, char in enumerate(b):
            if char in fragment_dict and fragment_dict[char] != key[index]:
                # invalid fragment, mark it as false
                fragments[key] = False
                break
            elif char in fragment_dict and fragment_dict[char] == key[index]:
                continue
            else:
                fragment_dict[char] = key[index]

    # collect matched fragment
    result = list(filter(lambda key: fragments[key], fragments.keys()))

    if len(result) == 0:
        # no match
        print(0)
    elif len(result) == 1:
        # calculate fragment occured times in the encrypted message
        occured_times = a.count(result[0])
        if occured_times == 1:
            # output the substring of the encrypted message that correspond to the fragment
            print(result[0])
        else:
            # fragment occured several times, output times
            print(occured_times)
    else:
        # multiple match, check alphabet order
        result = list(filter(lambda val: is_alphabet_order(val), result))
        print(len(result))


if __name__ == '__main__':
    main()
