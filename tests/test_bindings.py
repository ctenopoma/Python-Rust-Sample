"""Test Python bindings to Rust Fibonacci function.

This module tests the PyO3 bindings that expose the Rust fibonacci function
to Python as fibonacci_rust.
"""


def test_import_fibonacci_rust():
    """Test that fibonacci_rust can be imported from python_rust module."""
    from python_rust import fibonacci_rust
    
    assert callable(fibonacci_rust)


def test_rust_binding_basic():
    """Test basic functionality of Rust binding with known values."""
    from python_rust import fibonacci_rust
    
    # Test known Fibonacci value
    assert fibonacci_rust(10) == 55


def test_rust_binding_repeated_calls():
    """Test that multiple calls to fibonacci_rust work correctly."""
    from python_rust import fibonacci_rust
    
    # Multiple calls should all return correct values
    assert fibonacci_rust(5) == 5
    assert fibonacci_rust(10) == 55
    assert fibonacci_rust(15) == 610
    assert fibonacci_rust(20) == 6765


def test_rust_binding_base_cases():
    """Test base cases for Fibonacci sequence."""
    from python_rust import fibonacci_rust
    
    # Base cases as defined in Fibonacci sequence
    assert fibonacci_rust(0) == 0
    assert fibonacci_rust(1) == 1
    assert fibonacci_rust(2) == 1


def test_python_vs_rust_same_results():
    """Test that Python and Rust implementations return same results."""
    from python_rust import fibonacci_python, fibonacci_rust

    # Compare outputs for different Fibonacci indices
    test_values = [10, 20]
    for n in test_values:
        assert fibonacci_rust(n) == fibonacci_python(n)


def test_benchmark_runs():
    """Test that benchmark function executes without error."""
    from python_rust import benchmark

    # Should execute without raising an exception
    # Using small n to keep test fast
    benchmark(n=10, runs=1)  # type: ignore


def test_benchmark_output_format():
    """Test that benchmark prints output in expected format."""
    import io
    import sys

    from python_rust import benchmark

    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    try:
        benchmark(n=10, runs=1)  # type: ignore
    finally:
        # Restore stdout
        sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    
    # Verify output contains expected format
    assert "Fibonacci(10):" in output
    assert "Rust:" in output
    assert "Python:" in output
    assert "Speedup:" in output
    assert "s" in output  # Time unit
    assert "x" in output  # Speedup multiplier
