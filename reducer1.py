#!/usr/bin/python2
# coding=utf-8

import sys
import os
import string
import re

prevKey = None
count = 0
keyNow = None

for line in sys.stdin:

    line = line.strip()
    if line != '':
        keyNow, count = eval(line)
        keyNow = '("%s",%s)' %(keyNow[0], keyNow[1])
        count = int(count)

        if prevKey == keyNow:
            count += count
        else:
            if prevKey:
                print ('(%s,%d)' %(prevKey, count))
            count = count
            prevKey = keyNow

if prevKey == keyNow:
    print ('(%s,%d)' % (prevKey, count))
