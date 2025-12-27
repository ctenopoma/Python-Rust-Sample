"""Python-Rust Fibonacci Library.

This module provides efficient Fibonacci sequence calculations using both
Rust (via PyO3 bindings) and pure Python implementations, with performance
comparison utilities.

Attributes:
    fibonacci_rust: Rust implementation of Fibonacci (compiled extension).
    fibonacci_python: Pure Python recursive implementation (for benchmarking).
    benchmark: Performance comparison utility between implementations.

Example:
    >>> from python_rust import fibonacci_rust
    >>> fibonacci_rust(10)
    55
    >>> from python_rust import benchmark
    >>> benchmark(n=35, runs=5)
"""

from __future__ import annotations

__version__ = "0.1.0"
__author__ = "Rust-Python Team"

# Import Python implementation and benchmark utility
from .fibonacci import benchmark, fibonacci_python  # type: ignore # noqa: F401

# Import Rust implementation from compiled extension
# The compiled module exposes fibonacci function
from .python_rust import fibonacci as fibonacci_rust  # type: ignore # noqa: F401

__all__ = [
    "benchmark",
    "fibonacci_python",
    "fibonacci_rust",
]


