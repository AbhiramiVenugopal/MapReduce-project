#!/usr/bin/python2
# coding=utf-8

import sys

word_counts = {}

for line in sys.stdin:
    line = line.strip()
    word, doc_id = line.split('\t')
    doc_id = int(doc_id)

    if (word, doc_id) in word_counts:
        word_counts[(word, doc_id)] += 1
    else:
        word_counts[(word, doc_id)] = 1

#print("point1")
word_per_doc = {}
for (word, doc_id), count in word_counts.items():
    if doc_id in word_per_doc:
        word_per_doc[doc_id] += count
    else:
        word_per_doc[doc_id] = count

# print(reached)
for (word, doc_id), count in word_counts.items():
    print('((%s, %d), (%d, %d))' % (word, doc_id, count, word_per_doc[doc_id]))
