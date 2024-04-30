#!/usr/bin/python2
# coding=utf-8

import sys
import math

# harcoding total no of docs
N = 20  
wordNow = None
word = None
doc_ids = {}  #dictionary


for line in sys.stdin:
   
    line = line.strip().lstrip('(').rstrip(')')
    
    
    parts = line.split()
    if len(parts) != 4:
        #troubleshooting becuz of the expecting 1 issue
        continue

    word, doc_id, count, totalInDoc = parts[0], parts[1], parts[2], parts[3]

    try:
        doc_id = int(doc_id)
        count = int(count)
        totalInDoc = int(totalInDoc)
    except ValueError:
        #skipping here
        continue

    if wordNow != word:
        if wordNow:
           
            idf = math.log(N / float(len(doc_ids))) if len(doc_ids) > 0 else 0
            for doc, counts in doc_ids.items():
                tf_idf = counts[0] * idf
                print('%s\t%d\t%f' % (wordNow, doc, tf_idf))
        wordNow = word
        doc_ids = {}

    doc_ids[doc_id] = (count, totalInDoc)


if wordNow == word and len(doc_ids) > 0:
    idf = math.log(N / float(len(doc_ids)))
    for doc, counts in doc_ids.items():
        tf_idf = counts[0] * idf
        print('%s\t%d\t%f' % (wordNow, doc, tf_idf))
