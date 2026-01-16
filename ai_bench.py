import time
import random

def benchmark_matrix_ops(n):
    print(f"--- Benchmarking Matrix Size: {n}x{n} ---")
    
    # Create two random matrices (Simulating AI Weights & Inputs)
    A = [[random.random() for _ in range(n)] for _ in range(n)]
    B = [[random.random() for _ in range(n)] for _ in range(n)]
    C = [[0] * n for _ in range(n)]

    start_time = time.time()
    
    # Core AI Operation: Dot Product
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
                
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"Compute Time: {duration:.4f} seconds")
    print(f"Performance: Scalable on current architecture? {'YES' if duration < 1.0 else 'OPTIMIZATION NEEDED'}")
    print("-" * 30)

if __name__ == "__main__":
    # Test scalability by increasing load
    benchmark_matrix_ops(50)  # Small Load
    benchmark_matrix_ops(100) # Medium Load