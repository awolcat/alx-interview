#!/usr/bin/python3
"""Sript to read stdin and tally stats.
    Input format: <IP Address> - [<date>]
    "GET /projects/260 HTTP/1.1" <status code> <file size>
    Print stats after every 10 lines
    and/or on receipt of CTRL+C interrupt
"""
import sys


status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}

total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # check if the status code received exists and increment
            if status_code in status_codes.keys():
                status_codes[status_code] += 1

            # update total file size
            total_size += file_size

            # update line count
            line_count += 1

        # Print output
        if line_count % 10 == 0:
            print('File size: {}'.format(total_size))
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
