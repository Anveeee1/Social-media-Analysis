#!/usr/bin/env python
import sys

current = None
count = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    value = int(value)

    if key == current:
        count += value
    else:
        if current:
            print "%s\t%s" % (current, count)
        current = key
        count = value

if current:
    print "%s\t%s" % (current, count)
