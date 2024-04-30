#!/usr/bin/python2
# coding=utf-8

import sys
import os
import re

def process_document(filePath, index, stopwords):
    
    with open(filePath, "r") as file:
        for line in file:
           
            line = line.lower().strip()
            line = re.sub(r"[^\w\s]", "", line)
            words = line.split()

            for word in words:
                any_digit = any(str.isdigit(c) for c in word)
                if word not in stopwords:
                   
                    print("((%s, %d), 1)" % (repr(word), index))

def main():
    
    stopwords = open('stopwords.txt').read().split("\n")
    files_to_process = ['input1.txt', 'input2.txt', 'input3.txt']
    for index, filePath in enumerate(files_to_process, start=1):
        process_document(filePath, index, stopwords)

if __name__ == "__main__":
    main()
