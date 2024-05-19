import multiprocessing as mp
import random

ITERATIONS = 100000

def calculate_pi(seed):
    random.seed(seed)
    count = 0
    for _ in range(ITERATIONS // mp.cpu_count()):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            count += 1
    return count

def main():
    with mp.Pool() as pool:
        results = pool.map(calculate_pi, range(mp.cpu_count()))
        total_count = sum(results)
        pi = 4.0 * total_count / ITERATIONS
        print(f"Valor aproximado de Pi: {pi:.5f}")

if __name__ == "__main__":
    main()
