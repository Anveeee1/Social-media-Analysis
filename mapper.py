#!/usr/bin/env python
import sys

positive_words = ["good", "awesome", "excellent", "nice", "amazing", "loved"]
negative_words = ["bad", "poor", "waste"]

for line in sys.stdin:
    if "id" in line:
        continue

    data = line.strip().split(',')

    if len(data) < 8:
        continue

    comment = data[7].lower()

    pos = 0
    neg = 0

    for word in positive_words:
        if word in comment:
            pos += 1

    for word in negative_words:
        if word in comment:
            neg += 1

    if pos > neg:
        print "Positive\t1"
    elif neg > pos:
        print "Negative\t1"
      
