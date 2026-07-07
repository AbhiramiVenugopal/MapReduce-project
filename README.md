# Hadoop MapReduce TF-IDF Implementation

A multi-stage **MapReduce** implementation that computes **Term Frequency–Inverse Document Frequency (TF-IDF)** scores for a collection of text documents using **Python** and **Hadoop Streaming**.

This project demonstrates how a complex text analytics problem can be decomposed into multiple MapReduce jobs, where the output of one stage becomes the input to the next. It showcases distributed data processing concepts, text preprocessing, and the MapReduce programming model.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Processing Pipeline](#processing-pipeline)
- [Execution Flow](#execution-flow)
- [Running on Hadoop](#running-on-hadoop)
- [Running Locally](#running-locally)
- [Concepts Demonstrated](#concepts-demonstrated)
- [Learning Outcomes](#learning-outcomes)
- [Future Improvements](#future-improvements)
- [Skills Demonstrated](#skills-demonstrated)

---

## Project Overview

The objective of this project is to calculate **TF-IDF (Term Frequency–Inverse Document Frequency)** scores for words appearing across multiple text documents.

TF-IDF is widely used in:

-  Search Engines
-  Information Retrieval
-  Document Ranking
-  Text Mining
-  Natural Language Processing (NLP)

Rather than solving the problem in a single script, the computation is divided into multiple MapReduce jobs, similar to how large-scale data processing is performed on Hadoop clusters.

---

## Features

- Multi-stage Hadoop Streaming pipeline
- Custom Python Mapper and Reducer programs
- Text preprocessing and normalization
- Stop-word removal
- Word frequency aggregation
- Document frequency calculation
- TF-IDF score computation
- Batch execution using shell scripting
- Local execution pipeline for testing

---

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Mapper & Reducer implementation |
| Hadoop Streaming | Distributed execution |
| Hadoop MapReduce | Parallel data processing |
| Bash | Job orchestration |
| Regular Expressions | Text cleaning |
| Linux | Execution environment |

---

## Project Structure

```text
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
```

---

## Processing Pipeline

### Stage 1 — Text Processing

The first mapper:

- Reads input documents
- Converts text to lowercase
- Removes punctuation
- Splits text into individual words
- Removes stop words

Outputs:

```text
((word, documentID), 1)
```

The first reducer aggregates identical keys to determine the frequency of each word within each document.

---

### Stage 2 — Document Statistics

The second MapReduce job reorganizes the intermediate output by:

- Grouping words by document
- Counting occurrences
- Calculating document-level statistics
- Preparing data for TF-IDF computation

---

### Stage 3 — TF-IDF Calculation

The final MapReduce job computes TF-IDF scores.

For each word:

1. Determine the number of documents containing the word.
2. Compute the Inverse Document Frequency (IDF).
3. Combine TF and IDF.
4. Output a TF-IDF score for each document.

---

## Execution Flow

```text
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
```

---

## Running on Hadoop

Update the Hadoop paths inside `job.sh`.

Execute:

```bash
bash job.sh
```

The script:

1. Removes previous output directories
2. Runs the first Hadoop Streaming job
3. Runs the second Hadoop Streaming job
4. Runs the final Hadoop Streaming job
5. Produces the TF-IDF output

---

## Running Locally

To execute the pipeline without Hadoop:

```bash
python runmain.py
```

The script sequentially runs:

- Mapper 1
- Reducer 1
- Mapper 2
- Reducer 2
- Mapper 3
- Reducer 3

Intermediate files are automatically sorted to simulate Hadoop's **Shuffle & Sort** phase.

---

## Concepts Demonstrated

This project demonstrates:

- Hadoop MapReduce programming
- Hadoop Streaming
- Distributed data processing
- Multi-stage data pipelines
- Key-value pair generation
- Shuffle & Sort workflow
- Text preprocessing
- Word frequency analysis
- TF-IDF computation
- Batch job orchestration

---

## Learning Outcomes

Through this project, I gained experience in:

- Designing multi-stage MapReduce workflows
- Breaking complex computations into independent processing stages
- Developing custom Mapper and Reducer programs
- Processing semi-structured text data
- Understanding Hadoop's distributed processing model
- Debugging data flow across multiple MapReduce jobs

---

## Future Improvements

- Automatically determine the total number of documents
- Support arbitrary-sized datasets
- Improve TF normalization
- Add automated testing
- Upgrade to Python 3
- Containerize using Docker
- Execute on a multi-node Hadoop cluster

---

## Skills Demonstrated

- Python
- Hadoop
- Hadoop Streaming
- MapReduce
- Distributed Computing
- Data Processing
- Text Analytics
- Linux
- Shell Scripting
- Regular Expressions
- Software Engineering

---

## Author

Developed as part of a Hadoop MapReduce project demonstrating distributed text processing and multi-stage data analytics using Python and Hadoop Streaming.
