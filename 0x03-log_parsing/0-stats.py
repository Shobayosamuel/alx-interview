#!/usr/bin/python3


import re
import sys


log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)')


file_sizes = []
status_code_counts = {}

try:
    line_count = 0

    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)

        if match:
            file_size = int(match.group(3))
            status_code = int(match.group(2))

            file_sizes.append(file_size)

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1

            line_count += 1

            if line_count % 10 == 0:
                total_size = sum(file_sizes)
                print(f'File size: {total_size}')
                for code in sorted(status_code_counts):
                    print(f'{code}: {status_code_counts[code]}')
                print()

except KeyboardInterrupt:
    pass

"""
total_size = sum(file_sizes)
print(f'Total file size: {total_size}')
for code in sorted(status_code_counts):
    print(f'{code}: {status_code_counts[code]}')
"""
