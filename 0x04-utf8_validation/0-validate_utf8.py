#!/usr/bin/python3
"""Validate UTF8"""


def validUTF8(data):
    """Write a method that determines if a given data set represents
        a valid UTF-8 encoding.

        Prototype: def validUTF8(data)
        Return: True if data is a valid UTF-8 encoding, else return False
        A character in UTF-8 can be 1 to 4 bytes long
        The data set can contain multiple characters
        The data will be represented by a list of integers
        Each integer represents 1 byte of data,
        therefore you only need to handle the 8 least significant bits
        of each integer

        e.g
        >>> print(validUTF8([229, 65, 127, 256]))
        False
    """

    binary_list = []

    if len(data) == 0:
        return False
    # Convert list of integers to list of equivalent binary
    binary_list = [bin(num).replace('0b', '0')[-8:] for num in data]
    """
    for decimal in data:
        binary = ''
        while decimal:
            binary += str(decimal % 2)
            decimal = int(decimal / 2)

        # while len(binary) < 8:
            # binary = '0' + binary
        binary_list.append(binary)
    """

    # Validate UTF8
    i = 0
    while i < len(binary_list):
        if binary_list[i][0] == '0':
            i += 1
            continue
        if (binary_list[i][:3] == '110'
                and binary_list[i + 1]
                and binary_list[i + 1][:2] == '10'):
            i += 2
            continue
        if (binary_list[i][:4] == '1110'
                and binary_list[i + 2]
                and binary_list[i + 1][:2] == '10'
                and binary_list[i + 2][:2] == '10'):
            i += 3
            continue
        if (binary_list[i][:5] == '11110'
                and binary_list[i + 3]
                and binary_list[i + 1][:2] == '10'
                and binary_list[i + 2][:2] == '10'
                and binary_list[i + 3][:2] == '10'):
            i += 4
            continue
        else:
            return False
    return True
