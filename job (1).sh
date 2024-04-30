#!/bin/bash


HADOOP_STREAMING_JAR="/path/to/hadoop-streaming.jar"
INPUT_PATH1="/user/hadoop/input1"
OUTPUT_PATH1="/user/hadoop/output1"
OUTPUT_PATH2="/user/hadoop/output2"
OUTPUT_PATH3="/user/hadoop/output3"
MAPPER1_PATH="/path/to/mapper1.py"
REDUCER1_PATH="/path/to/reducer1.py"
MAPPER2_PATH="/path/to/mapper2.py"
REDUCER2_PATH="/path/to/reducer2.py"
MAPPER3_PATH="/path/to/mapper3.py"
REDUCER3_PATH="/path/to/reducer3.py"


hdfs dfs -rm -r $OUTPUT_PATH1
hdfs dfs -rm -r $OUTPUT_PATH2
hdfs dfs -rm -r $OUTPUT_PATH3


hadoop jar $HADOOP_STREAMING_JAR \
    -files $MAPPER1_PATH,$REDUCER1_PATH \
    -input $INPUT_PATH1 \
    -output $OUTPUT_PATH1 \
    -mapper "python mapper1.py" \
    -reducer "python reducer1.py"

hadoop jar $HADOOP_STREAMING_JAR \
    -files $MAPPER2_PATH,$REDUCER2_PATH \
    -input $OUTPUT_PATH1 \
    -output $OUTPUT_PATH2 \
    -mapper "python mapper2.py" \
    -reducer "python reducer2.py"


hadoop jar $HADOOP_STREAMING_JAR \
    -files $MAPPER3_PATH,$REDUCER3_PATH \
    -input $OUTPUT_PATH2 \
    -output $OUTPUT_PATH3 \
    -mapper "python mapper3.py" \
    -reducer "python reducer3.py"

echo "Hadoop jobs completed."