#!/usr/bin/python2
# coding=utf-8

import sys
import re

pattern = re.compile(r"\(\(\"([^\"]+)\",(\d+)\),(\d+)\)")

for line in sys.stdin:
    line = line.strip()
    if line:
        match = pattern.match(line)
        if match:
            word, doc_id, tf = match.groups()
            print('%s\t%s' % (word, doc_id))
        else:
            print(f"issue with input format {line}", file=sys.stderr)
