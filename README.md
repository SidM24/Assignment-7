# Matrix Multiplication with Multithreading

The Python code benchmarks the execution time of matrix multiplication using multithreading. It generates random matrices and performs matrix multiplication with a fixed matrix using multiple threads. The number of threads used is varied, and the execution time is recorded for each configuration. Finally, it plots the relationship between the number of threads and the execution time to analyze the scalability of matrix multiplication with multithreading.

## Usage

To run the script, make sure you have Python installed. Then, simply execute the script:

-main.py

## Time taken(seconds) v/s no. of Threads:

| Thread 1 | Thread 2 | Thread 3 | Thread 4 | Thread 5 | Thread 6 | Thread 7 | Thread 8 |
|----------|----------|----------|----------|----------|----------|----------|----------|
| 2.20     | 2.07     | 1.687    | 1.547    | 1.643    | 1.677    | 1.705    | 1.72     |

![Image Description](graph.png)

## Resource Usage

![alt text](image.png)

