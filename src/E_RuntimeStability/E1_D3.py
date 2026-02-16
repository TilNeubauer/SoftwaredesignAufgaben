from __future__ import annotations

import numpy as np
import timeit
import matplotlib.pyplot as plt

from E1 import positive
from D3_oldPi import estimate_pi

def rand2xN(n: int = 5) -> np.ndarray:
    """Create a 2×N matrix with random numbers from uniform distribution."""
    arr = np.random.uniform(size=(2, n))
    return arr


def in_unit_circle_vec(arr: np.ndarray) -> int:
    M = 0
    for i in range(np.shape(arr)[1]):
        if arr[0, i] ** 2 + arr[1, i] ** 2 <= 1.0:
            M += 1
    return M


@positive  # checks N > 0 and M > 0
def estPi(N: int, M: int) -> float:
    return 4 * M / N


@positive(0)  # checks only N > 0
def estPi_np(N: int) -> float:
    arr = rand2xN(N)
    M = in_unit_circle_vec(arr)
    pi = estPi(N, M)
    return pi


def benchmark_pi_estimators(N_values):
    """
    Dose Pi estimation with two different methods and compare the time for computation
    Args:
        N_values: List for values to test
    """
    times_np = []
    times_py = []

    for n in N_values:
        # NumPy
        t1 = timeit.default_timer()
        estPi_np(n)
        t2 = timeit.default_timer()
        times_np.append(t2 - t1)

        # Python
        t3 = timeit.default_timer()
        estimate_pi(n)
        t4 = timeit.default_timer()
        times_py.append(t4 - t3)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(N_values, times_np, label="NumPy")
    plt.plot(N_values, times_py, label="Pure Python")
    plt.xscale("log")
    plt.xlabel("N (log scale)")
    plt.ylabel("Execution time (s)")
    plt.title("Pi Estimation Benchmark")
    plt.legend()
    plt.tight_layout()
    plt.show()

    return times_np, times_py


def main() -> None:
    Ns = [10_000, 50_000, 100_000, 200_000, 500_000, -1_000_000]
    benchmark_pi_estimators(Ns)


if __name__ == "__main__":
    main()
