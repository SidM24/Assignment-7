import threading
import numpy as np
import time
import multiprocessing
import matplotlib.pyplot as plt


def matrix_multiplication(start, end, fixed_matrix, random_matrices, result):
    for i in range(start, end):
        result[i] = np.dot(fixed_matrix, random_matrices[i])


def main(num_threads):
    # Creating a result  matrix with size equal to the number of matrices that will store the result of the matrix
    # multiplication
    result = [None] * num_matrices

    chunk_size = num_matrices // num_threads
    threads = []

    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else num_matrices
        thread = threading.Thread(target=matrix_multiplication,
                                  args=(start, end, fixed_matrix, random_matrices, result))
        threads.append(thread)

    start_time = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()

    total_time = end_time - start_time
    print(f"Multiplication with {num_threads} threads took {total_time} seconds.")
    time_taken.append(total_time)


if __name__ == "__main__":
    num_of_cores = multiprocessing.cpu_count()
    print(f"The current system has {num_of_cores} cores")
    # Test different numbers of threads
    num_threads = [1, 2, 3, 4, 5, 6, 7, 8]
    time_taken = []  # To store time taken by n no. of threads
    # Multiplying 100 random matrices with a fixed matrix of size 1000 x 1000
    num_matrices = 100
    matrix_size = (1000, 1000)
    num_rows, num_cols = matrix_size

    # Array of Random Matrices
    random_matrices = []

    for _ in range(num_matrices):
        matrix = np.random.rand(*matrix_size)
        random_matrices.append(matrix)

    fixed_matrix = np.random.rand(num_rows, num_cols)

    for num_thread in num_threads:
        main(num_thread)

    plt.plot(num_threads, time_taken, marker='o')
    plt.grid()
    plt.xlabel('Number of Threads')
    plt.ylabel('Execution time')
    plt.title('Time vs Number of Threads for Matrix Multiplication')
    plt.show()
