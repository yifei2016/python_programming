#! /usr/bin/python3
import sys


def main():
    # start collecting data from user input
    lines = []
    for line in sys.stdin:
        lines.append(line)
        if len(lines) == 2:
            break

    dna = [char for char in lines[0].strip()]
    infect_dna = [char for char in lines[1].strip()]

    # data collected

    # start calculating infection start position
    infect_start_pos = -1

    for index, val in enumerate(infect_dna):
        if index < len(dna) and val != dna[index]:
            infect_start_pos = index
            break

    if infect_start_pos == -1:
        # Not found infected DNA sequence. No need to continue.
        if len(infect_dna) > len(dna):
            print(len(infect_dna) - len(dna))
        else:
            print(0)
        return None

    infect_end_pos = len(infect_dna) - 1
    dna_end_pos = len(dna) - 1

    # start calculating infection end position
    while infect_end_pos >= infect_start_pos and dna_end_pos >= infect_start_pos:
        if infect_dna[infect_end_pos] == dna[dna_end_pos]:
            infect_end_pos -= 1
            dna_end_pos -= 1
        else:
            break

    # result
    infected_dna_length = infect_end_pos - infect_start_pos + 1
    print(infected_dna_length)


if __name__ == '__main__':
    main()
