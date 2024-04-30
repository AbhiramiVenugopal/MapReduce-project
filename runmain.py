import subprocess

# Step 1: Term Frequency (TF) Calculation
subprocess.call("type input1.txt | python mapper1.py > mapper1_output.txt", shell=True)
subprocess.call("sort mapper1_output.txt > step1_sorted.txt", shell=True)
subprocess.call("type step1_sorted.txt | python reducer1.py > reducer1_output.txt", shell=True)

# Step 2: Document Frequency (DF) Calculation
subprocess.call("type reducer1_output.txt | python mapper2.py > mapper2_output.txt", shell=True)
subprocess.call("sort mapper2_output.txt > step2_sorted.txt", shell=True)
subprocess.call("type step2_sorted.txt | python reducer2.py > reducer2_output.txt", shell=True)

# Step 3: TF-IDF Calculation (hypothetical step, specifics depend on actual mapper3 and reducer3 implementations)
subprocess.call("type reducer2_output.txt | python mapper3.py > mapper3_output.txt", shell=True)
subprocess.call("sort mapper3_output.txt > step3_sorted.txt", shell=True)
subprocess.call("type step3_sorted.txt | python reducer3.py > reducer3_output.txt", shell=True)
