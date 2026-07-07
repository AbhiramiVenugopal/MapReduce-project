Hadoop MapReduce TF-IDF Implementation

A multi-stage MapReduce implementation that computes Term Frequency–Inverse Document Frequency (TF-IDF) scores for a collection of text documents using Python and Hadoop Streaming.

This project demonstrates how a complex text analytics problem can be decomposed into multiple MapReduce jobs, where the output of one stage becomes the input to the next. It showcases distributed data processing concepts, text preprocessing, and the MapReduce programming model.

Project Overview

The objective of this project is to calculate TF-IDF scores for words appearing across multiple documents.

TF-IDF is a widely used metric in:

Information Retrieval
Search Engines
Document Ranking
Text Mining
Natural Language Processing (NLP)

Instead of solving the problem in a single script, the computation is broken into a sequence of MapReduce jobs similar to how large-scale data processing is performed on Hadoop clusters.

Features
Multi-stage Hadoop Streaming pipeline
Python-based Mapper and Reducer programs
Text preprocessing and normalization
Stop-word removal
Word frequency aggregation
Document frequency calculation
TF-IDF score computation
Batch execution using shell scripting
Local execution pipeline for testing

Technology Stack
Python 2
Hadoop Streaming
Hadoop MapReduce
Bash
Regular Expressions
Linux Command Line

Project Structure
.
├── mapper1.py        # Text preprocessing and word extraction
├── reducer1.py       # Term frequency aggregation
├── mapper2.py        # Prepare intermediate data
├── reducer2.py       # Calculate document statistics
├── mapper3.py        # Format data for TF-IDF stage
├── reducer3.py       # Compute TF-IDF values
├── job.sh            # Hadoop Streaming execution pipeline
├── runmain.py        # Local execution pipeline
├── README.md
└── cover.txt

Processing Pipeline
Stage 1 — Text Processing

The first mapper:

Reads the input documents
Converts text to lowercase
Removes punctuation
Splits text into individual words
Removes stop words
Emits:
((word, documentID), 1)

The first reducer aggregates identical keys to determine the number of occurrences of each word within each document.

Stage 2 — Document Statistics

The second MapReduce job reorganizes the intermediate output.

Its responsibilities include:

Grouping words by document
Counting occurrences
Calculating document-level statistics
Preparing data required for TF-IDF computation
Stage 3 — TF-IDF Calculation

The final MapReduce job computes TF-IDF scores.

For every word:

Determine how many documents contain the word.
Compute the inverse document frequency (IDF).
Combine the term frequency with the IDF value.
Output a TF-IDF score for each document containing that word.
Execution Flow
Input Documents
        │
        ▼
 Mapper 1
        │
        ▼
Reducer 1
        │
        ▼
 Mapper 2
        │
        ▼
Reducer 2
        │
        ▼
 Mapper 3
        │
        ▼
Reducer 3
        │
        ▼
 TF-IDF Output
Running on Hadoop

Update the paths inside job.sh to match your Hadoop installation.

Execute:

bash job.sh

The script performs the following:

Removes previous output directories
Executes the first Hadoop Streaming job
Executes the second Hadoop Streaming job
Executes the final Hadoop Streaming job
Produces the TF-IDF output
Running Locally

The project also includes a local execution script for testing the MapReduce pipeline without submitting Hadoop jobs.

python runmain.py

The script automatically executes:

Mapper 1
Reducer 1
Mapper 2
Reducer 2
Mapper 3
Reducer 3

while sorting intermediate files between each stage to simulate Hadoop's shuffle and sort phase.

Concepts Demonstrated

This project demonstrates practical knowledge of:

MapReduce programming model
Hadoop Streaming
Distributed data processing
Intermediate key-value pair generation
Shuffle and sort workflow
Text preprocessing
Frequency analysis
TF-IDF computation
Batch job orchestration
Data transformation pipelines
Learning Outcomes

Through this project I gained experience with:

Designing multi-stage MapReduce workflows
Breaking large computations into independent processing stages
Building custom Mapper and Reducer programs
Processing semi-structured text data
Understanding how Hadoop distributes computation across multiple jobs
Debugging data flow between MapReduce stages
Possible Future Improvements
Automatically determine the total number of documents instead of using a fixed value.
Support arbitrary numbers of input documents.
Improve TF normalization.
Add automated testing.
Containerize the project using Docker.
Upgrade to Python 3 compatibility.
Execute on a multi-node Hadoop cluster for scalability testing.
Skills Demonstrated
Python
Hadoop
MapReduce
Distributed Computing
Data Processing
Text Analytics
Linux
Shell Scripting
Regular Expressions
Software Engineering
