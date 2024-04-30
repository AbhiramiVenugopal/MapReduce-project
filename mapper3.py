#!/usr/bin/python2
# coding=utf-8

import sys
for line in sys.stdin:
    
    line = line.strip()[1:-1]
    first_part, scnd_part = line.split("), (")
    word, doc_id = first_part.split(", ")
    count, total_count_in_doc = scnd_part.split(", ")
    
   
    word = word.strip("'")
    doc_id = int(doc_id)
    count = int(count)
    total_count_in_doc = int(total_count_in_doc.strip(')'))

   
    print('%s\t%d\t%d\t%d' % (word, doc_id, count, total_count_in_doc))
