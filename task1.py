#! /usr/bin/python3
import sys
import functools


def main():
    # start collecting measurement data
    lines = []
    for line in sys.stdin:
        lines.append(line)
        if len(lines) == int(lines[0]) + 1:
            break
    
    # data collected
    lines.pop(0)

    # format data, convert string to int
    format = lambda str: [int(s) for s in str.split()]
    data = list(map(format, lines))
    
    # get measurement result
    measurement = functools.reduce(lambda prev, curr: [prev[0] + curr[0], prev[1] + curr[1]], data)
    print(measurement)
    # output
    display_minutes = measurement[0]
    actual_minutes = measurement[1] / 60

    result = actual_minutes / display_minutes

    if result <= 1:
        print('measurement error')
    else:
        print(result)


if __name__ =='__main__':
    main()
