"""Type stubs for python_rust package public API."""

from __future__ import annotations

__version__: str
__author__: str

def fibonacci_rust(n: int) -> int:
    """Rust implementation of Fibonacci calculation."""
    ...

def fibonacci_rust_iterative(n: int) -> int:
    """Rust implementation of Fibonacci calculation."""
    ...

def fibonacci_python(n: int) -> int:
    """Pure Python recursive Fibonacci implementation."""
    ...

def fibonacci_python_iterative(n: int) -> int:
    """Pure Python iterative Fibonacci implementation."""
    ...

def benchmark(n: int = 35, runs: int = 5) -> None:
    """Compare Rust and Python Fibonacci implementations."""
    ...

def benchmark_iterative(n: int = 35, runs: int = 5) -> None:
    """Compare Rust and Python iterative Fibonacci implementations."""
    ...
