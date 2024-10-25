#!/usr/bin/python3
'''reads stdin line by line and computes metrics'''
import sys
import signal


def print_stats(total_size, status_codes):
    """Prints the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """Parses a line and extracts the status code and file size
    if the format is correct."""
    try:
        parts = line.split()
        if len(parts) < 9:
            return None, None
        status_code = parts[-2]
        file_size = parts[-1]
        if status_code.isdigit() and file_size.isdigit():
            return int(status_code), int(file_size)
    except IndexError:
        pass
    return None, None


# Initialize counters and storage for metrics
total_size = 0
line_count = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def signal_handler(sig, frame):
    """Handle keyboard interruption and print stats."""
    print_stats(total_size, status_codes)
    sys.exit(0)


# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)


# Process each line from stdin
for line in sys.stdin:
    status_code, file_size = parse_line(line)

    if status_code is not None and file_size is not None:
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        line_count += 1

    if line_count % 10 == 0:
        print_stats(total_size, status_codes)

# Print final stats if the end of input is reached without interruption
print_stats(total_size, status_codes)
