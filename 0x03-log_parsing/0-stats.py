#!/usr/bin/python3
"""Sript to read stdin and tally stats.
    Input format: <IP Address> - [<date>]
    "GET /projects/260 HTTP/1.1" <status code> <file size>
    Print stats after every 10 lines
    and/or on receipt of CTRL+C interrupt
"""
import sys
import signal



def string_gen(code, count):
    """Return a populated or empty string based on count"""
    if type(count) is not int or count < 1:
        return ""
    return "{}: {}\n".format(code, count)


def handler(sig, frame):
    """Handle CTRL+C signal"""
    print(out, end="")


signal.signal(signal.SIGINT, handler)


global_count = 0
file_size = 0
success_200 = 0
redirect_301 = 0
error_400 = 0
error_401 = 0
error_403 = 0
error_404 = 0
error_405 = 0
error_500 = 0
for line in sys.stdin:
    line = line.split(" ")
    global_count += 1
    size = int(line[-1])
    status = int(line[-2])
    file_size += size

    # Calculate count for each status code
    if status == 200:
        success_200 += 1
    elif status == 301:
        redirect_301 += 1
    elif status == 400:
        error_400 += 1
    elif status == 401:
        error_401 += 1
    elif status == 403:
        error_403 += 1
    elif status == 404:
        error_404 += 1
    elif status == 405:
        error_405 += 1
    elif status == 500:
        error_500 += 1
    else:
        pass

    # Output string
    out = (f"File size: {file_size}\n"
           f"{string_gen(200, success_200)}"
           f"{string_gen(301, redirect_301)}"
           f"{string_gen(400, error_400)}"
           f"{string_gen(401, error_401)}"
           f"{string_gen(403, error_403)}"
           f"{string_gen(404, error_404)}"
           f"{string_gen(405, error_405)}"
           f"{string_gen(500, error_500)}"
           )
    # Print conditionally
    if global_count % 10 == 0:
        print(out, end="")
