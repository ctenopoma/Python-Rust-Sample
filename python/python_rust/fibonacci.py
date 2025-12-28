"""Pure Python Fibonacci implementation and performance benchmark utilities.

This module provides:
- fibonacci_python: Naive recursive implementation for performance comparison
- fibonacci_python_iterative: Iterative implementation for efficient use
- benchmark: Utility to compare Rust and Python implementations

Example:
    >>> from python_rust.fibonacci import fibonacci_python
    >>> fibonacci_python(10)
    55
    >>> from python_rust.fibonacci import benchmark
    >>> benchmark(n=20, runs=3)
    Fibonacci(20):
      Rust:   0.000005s
      Python: 0.001234s
      Speedup: 246.8x
"""

from __future__ import annotations

import timeit


def fibonacci_python(n: int) -> int:
    """Calculate Fibonacci number using naive recursive algorithm.

    This is intentionally a naive, recursive implementation to provide a fair
    performance comparison baseline. The exponential time complexity O(2^n)
    demonstrates the performance benefit of the Rust implementation.

    Args:
        n: The index in the Fibonacci sequence to calculate.

    Returns:
        The nth Fibonacci number.

    Note:
        This is intentionally a slow implementation used only for benchmarking
        comparison with the Rust implementation. Do not use in production code.
        For n > 40, execution becomes impractically slow.
    """
    if n <= 1:
        return n
    return fibonacci_python(n - 1) + fibonacci_python(n - 2)


def fibonacci_python_iterative(n: int) -> int:
    """Calculate Fibonacci number using an iterative algorithm.

    This implementation runs in O(n) time and O(1) space, making it suitable
    for regular use and direct comparison with the Rust iterative version.

    Args:
        n: The index in the Fibonacci sequence to calculate.

    Returns:
        The nth Fibonacci number.
    """
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def benchmark(n: int = 35, runs: int = 5) -> None:
    """Compare execution time of Rust and Python Fibonacci implementations.

    Times both implementations and prints execution statistics showing the
    performance advantage of the Rust implementation.

    Args:
        n: The Fibonacci index to benchmark (default: 35).
           Recommended range: 20 ≤ n ≤ 40.
        runs: Number of timing iterations to average (default: 5).
              Higher values reduce timing variance but increase total time.

    Prints:
        Execution times for both implementations and the speedup ratio.
        Format:
            Fibonacci({n}):
              Rust:   {rust_time:.6f}s
              Python: {python_time:.6f}s
              Speedup: {speedup:.1f}x

    Raises:
        ImportError: If Rust extension not built. Run 'maturin develop'.

    Note:
        For accurate results, ensure system is not under heavy load.
        Larger n values (>40) make Python implementation impractically slow.
    """
    # Import here to catch build errors with helpful message
    try:
        from python_rust import fibonacci_rust  # noqa: F401
    except ImportError as e:
        msg = "Rust extension not built. Run 'maturin develop' first."
        raise ImportError(msg) from e

    # Time the Rust implementation
    rust_time = timeit.timeit(
        lambda: fibonacci_rust(n),  # type: ignore
        number=runs,
    ) / runs

    # Time the Python implementation
    python_time = timeit.timeit(
        lambda: fibonacci_python(n),
        number=runs,
    ) / runs

    # Calculate speedup
    speedup = python_time / rust_time

    # Print formatted results
    print(f"Fibonacci({n}):")
    print(f"  Rust:   {rust_time:.6f}s")
    print(f"  Python: {python_time:.6f}s")
    print(f"  Speedup: {speedup:.1f}x")


def benchmark_iterative(n: int = 35, runs: int = 5) -> None:
    """Compare execution time of Rust and Python iterative Fibonacci implementations.

    Uses the efficient Python iterative implementation to provide an apples-to-
    apples comparison with the Rust iterative binding.

    Args:
        n: The Fibonacci index to benchmark (default: 35).
           For larger n, both implementations remain fast; choose based on
           desired workload.
        runs: Number of timing iterations to average (default: 5).

    Prints:
        Execution times for both implementations and the speedup ratio.
    """
    try:
        from python_rust import fibonacci_rust  # type: ignore
    except ImportError as e:
        msg = "Rust extension not built. Run 'maturin develop' first."
        raise ImportError(msg) from e

    rust_time = timeit.timeit(
        lambda: fibonacci_rust(n),  # type: ignore
        number=runs,
    ) / runs

    python_time = timeit.timeit(
        lambda: fibonacci_python_iterative(n),
        number=runs,
    ) / runs

    speedup = python_time / rust_time

    print(f"Fibonacci({n}) iterative:")
    print(f"  Rust:   {rust_time:.6f}s")
    print(f"  Python: {python_time:.6f}s")
    print(f"  Speedup: {speedup:.1f}x")
